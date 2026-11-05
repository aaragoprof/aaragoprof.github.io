#!/usr/bin/env python3
"""
Genera la web (carpeta docs/) a partir de la carpeta de material que tens
al teu ordinador. Disseny de targetes: Cicle -> Mòdul -> RA -> Material.

Estructura que espera la carpeta d'origen:

    CICLE (ASIX, DAM, DAW, SMIX)
      └── 0378 Nom del mòdul
            ├── RA1 - Nom del resultat d'aprenentatge
            │     └── Teoria        <- només aquesta carpeta es publica
            └── RA2 - ...

Ús:
    python generar.py "C:\\ruta\\a\\la\\carpeta\\de\\material"

Què fa amb el contingut de cada carpeta Teoria:
  - .md            -> pàgina web amb el disseny de la web
  - .pdf           -> es converteix a pàgina (text o, si és una imatge,
                      pàgines-imatge lleugeres); el PDF NO es publica
  - .html          -> es publica tal qual (amb el seu propi disseny)
  - altres fitxers -> es copien i apareixen com a descàrrega
Si hi ha un .md o .html amb el mateix nom que un PDF, el PDF s'ignora.

Opcional: un fitxer "descripcio.txt" dins d'una carpeta de mòdul o d'RA
(fora de Teoria) es mostra com a descripció a la targeta.

Els mòduls o RA sense material surten en gris amb "Properament".
"""
import hashlib
import html
import json
import os
import posixpath
import re
import shutil
import stat
import sys
import time
import unicodedata
from pathlib import Path
from urllib.parse import quote

# ----------------------------------------------------------------------------
# CONFIGURACIÓ (edita aquí el que necessitis)
# ----------------------------------------------------------------------------
SITE_NAME = "Material docent"
SITE_EYEBROW = "Formació Professional · Informàtica"
SITE_LEDE = (
    "Materials de les assignatures que imparteixo als cicles formatius "
    "d'informàtica: ASIX, DAM, DAW i SMIX."
)
FOOTER = "Material docent · Formació Professional · Informàtica"

# Carpetes que MAI es publiquen (en qualsevol nivell; no distingeix
# majúscules ni accents).
EXCLOURE = {"gestio", "gestions", "ordenar", ".git", "examen", "exercicis"}

# Cicles: carpeta -> nom complet. L'ordre és el de la portada.
CICLES = {
    "ASIX": "Administració de Sistemes Informàtics en Xarxa",
    "DAM": "Desenvolupament d'Aplicacions Multiplataforma",
    "DAW": "Desenvolupament d'Aplicacions Web",
    "SMIX": "Sistemes Microinformàtics i Xarxes",
}

# Els PDF NO es pugen a GitHub: es converteixen a pàgina web.
CONVERTIR_PDF = True
# Extreure les imatges dels PDF amb text (ocupen espai; False = només text).
IMATGES_PDF = True
# PDF sense text (diapositives exportades com a imatge, escanejats...):
# es publiquen pàgina a pàgina com a imatges lleugeres.
PDF_SENSE_TEXT_COM_IMATGES = True
AMPLADA_PAGINA_PX = 1400
QUALITAT_JPG = 80

# Avisos de mida
AVIS_MB_FITXER = 20     # fitxer (no PDF) que es puja tal qual
AVIS_MB_TOTAL = 300     # mida total de docs/

ROOT = Path(__file__).resolve().parent
DOCS = ROOT / "docs"


# ----------------------------------------------------------------------------
# Utilitats i conversió de PDF
# ----------------------------------------------------------------------------
def norm(s):
    """Normalitza Unicode (Mac guarda els accents separats)."""
    return unicodedata.normalize("NFC", s)


def sense_accents(s):
    s = unicodedata.normalize("NFKD", s)
    return "".join(c for c in s if not unicodedata.combining(c))


def slug(s, maxlen=60):
    s = sense_accents(s).lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return (s[:maxlen].strip("-")) or "x"


def excluit(nom):
    return sense_accents(nom).lower() in EXCLOURE or nom.startswith(".")


def es_teoria(nom):
    return sense_accents(nom).lower() == "teoria"


def subcarpetes(p):
    return sorted(
        (d for d in p.iterdir() if d.is_dir() and not excluit(d.name)),
        key=lambda d: norm(d.name).lower(),
    )


def fitxers_teoria(carpeta):
    """Tots els fitxers (recursiu) d'una carpeta de teoria, sense excloure's."""
    res = []
    if not carpeta or not carpeta.is_dir():
        return res

    def rec(d):
        for e in sorted(d.iterdir(), key=lambda x: norm(x.name).lower()):
            if e.name.startswith(".") or excluit(e.name):
                continue
            if e.is_dir():
                rec(e)
            elif e.is_file():
                res.append(e)

    rec(carpeta)
    return res


def troba_teoria(carpeta):
    for d in carpeta.iterdir():
        if d.is_dir() and es_teoria(d.name):
            return d
    return None


class ConversorFaltant(Exception):
    pass


CACHE = ROOT / ".cache_pdf"
TOKEN_IMG = "@@IMG@@/"
AVISAT = []
FALLITS = []      # PDF que no s'han pogut convertir (escanejats, errors...)
GRANS = []        # fitxers no-PDF grans
STATS = {"convertits": 0, "cache": 0}


def _pdf_a_markdown(pdf_tmp, img_dir):
    """Converteix un PDF a Markdown. Prova pymupdf4llm i, si no hi és o
    falla, markitdown. Retorna (markdown, motor)."""
    err_import = None
    try:
        import pymupdf4llm  # pip install pymupdf4llm
    except Exception as e:  # noqa: BLE001  (ImportError o error en carregar-lo)
        pymupdf4llm = None
        err_import = f"{type(e).__name__}: {e}"

    if pymupdf4llm is not None:
        try:
            kw = {}
            if IMATGES_PDF:
                kw = dict(
                    write_images=True,
                    image_path=str(img_dir),
                    image_format="jpg",
                    dpi=100,
                )
            return pymupdf4llm.to_markdown(str(pdf_tmp), **kw), "pymupdf4llm"
        except Exception as e:  # noqa: BLE001
            print(f"  (pymupdf4llm ha fallat: {e}; provo amb markitdown)")

    if err_import and not AVISAT:
        AVISAT.append(1)
        print(
            f"  AVÍS: no puc carregar pymupdf4llm ({err_import}).\n"
            "  Faig servir un conversor més simple (sense títols ni taules)."
        )

    try:
        from markitdown import MarkItDown
    except Exception:  # noqa: BLE001
        MarkItDown = None
    if MarkItDown is not None:
        return MarkItDown().convert(str(pdf_tmp)).text_content, "markitdown"

    try:
        from pypdf import PdfReader
    except Exception:  # noqa: BLE001
        raise ConversorFaltant(
            "\nNo puc convertir els PDF: no es pot carregar cap conversor.\n"
            f"  Python que s'està fent servir: {sys.executable}\n"
            f"  Motiu (pymupdf4llm): {err_import}\n\n"
            "Solució: instal·la'l amb EXACTAMENT aquest Python:\n"
            f'  "{sys.executable}" -m pip install pypdf pillow\n'
        )
    pagines = [(p.extract_text() or "").strip() for p in PdfReader(str(pdf_tmp)).pages]
    return "\n\n".join(t for t in pagines if t), "pypdf"


def _reescriu_imatges(md, img_dir):
    """Deixa els enllaços d'imatge com TOKEN_IMG + nom (rutes relatives)."""
    def canvia(m):
        nom = re.split(r"[\\/]", m.group(2).strip())[-1]
        if (img_dir / nom).is_file():
            return f"![{m.group(1)}]({TOKEN_IMG}{nom})"
        return ""

    return re.sub(r"!\[([^\]]*)\]\(([^)]*)\)", canvia, md)


def _pdf_com_imatges(pdf_tmp, img_dir, titol):
    """PDF sense text: cada pàgina es desa com a JPG lleuger i el Markdown
    només les mostra en ordre. Prova PyMuPDF i, si no hi és, pypdf+Pillow."""
    shutil.rmtree(img_dir, ignore_errors=True)
    img_dir.mkdir(parents=True)
    n = 0
    try:
        import fitz  # PyMuPDF (s'instal·la amb pymupdf4llm)

        doc = fitz.open(str(pdf_tmp))
        for i, page in enumerate(doc, 1):
            z = AMPLADA_PAGINA_PX / page.rect.width
            pix = page.get_pixmap(matrix=fitz.Matrix(z, z))
            nom = img_dir / f"pagina-{i:02d}.jpg"
            try:
                nom.write_bytes(pix.tobytes("jpeg", jpg_quality=QUALITAT_JPG))
            except TypeError:
                pix.save(str(nom))
            n += 1
    except Exception:  # noqa: BLE001
        shutil.rmtree(img_dir, ignore_errors=True)
        img_dir.mkdir(parents=True)
        n = 0
        try:
            from pypdf import PdfReader
            from PIL import Image
            import io
        except ImportError:
            raise RuntimeError(
                "PDF sense text. Per publicar-lo com a imatges instal·la: "
                f'"{sys.executable}" -m pip install pymupdf4llm pypdf pillow'

            )
        for i, page in enumerate(PdfReader(str(pdf_tmp)).pages, 1):
            imgs = list(page.images)
            if not imgs:
                continue
            gran = max(imgs, key=lambda im: len(im.data))
            im = Image.open(io.BytesIO(gran.data)).convert("RGB")
            if im.width > AMPLADA_PAGINA_PX:
                h = round(im.height * AMPLADA_PAGINA_PX / im.width)
                im = im.resize((AMPLADA_PAGINA_PX, h), Image.LANCZOS)
            im.save(img_dir / f"pagina-{i:02d}.jpg", "JPEG",
                    quality=QUALITAT_JPG, optimize=True)
            n += 1
    if n == 0:
        raise RuntimeError("sense text i no he pogut extreure les pàgines com a imatge")
    cos = [f"# {titol}\n", "*Material en format diapositives.*\n"]
    for i in range(1, n + 1):
        cos.append(f"![Pàgina {i}]({TOKEN_IMG}pagina-{i:02d}.jpg){{ loading=lazy }}\n")
    return "\n".join(cos), "imatges"


def converteix_pdf(pdf):
    """Retorna (markdown_amb_token, carpeta_imatges_o_None) o None si falla.
    Fa servir una memòria cau a .cache_pdf perquè no tardi cada vegada."""
    st = pdf.stat()
    clau = hashlib.sha1(
        f"{pdf.resolve()}|{st.st_size}|{st.st_mtime_ns}|{IMATGES_PDF}".encode()
    ).hexdigest()[:16]
    cdir = CACHE / clau
    cmd, cimg = cdir / "doc.md", cdir / "img"
    if cmd.is_file():
        STATS["cache"] += 1
        return cmd.read_text(encoding="utf-8"), (cimg if cimg.is_dir() else None)

    # Treballem directament a la carpeta final de la memòria cau (sense
    # renombrar carpetes, que a Windows falla si OneDrive o l'antivirus
    # tenen fitxers oberts). doc.md s'escriu l'últim: si no hi és, la
    # conversió es considera incompleta i es repeteix.
    work = cdir
    shutil.rmtree(work, ignore_errors=True)
    (work / "img").mkdir(parents=True, exist_ok=True)
    tmp_pdf = work / "doc.pdf"  # nom simple perquè les imatges no portin espais
    try:
        shutil.copy2(pdf, tmp_pdf)
        md, motor = _pdf_a_markdown(tmp_pdf, work / "img")
        md = _reescriu_imatges(md, work / "img")
        text_pla = re.sub(r"!\[[^\]]*\]\([^)]*\)|\s+", "", md)
        if len(text_pla) < 40:
            if not PDF_SENSE_TEXT_COM_IMATGES:
                raise RuntimeError("sense text (PDF escanejat o només imatges?)")
            md, motor = _pdf_com_imatges(tmp_pdf, work / "img", norm(pdf.stem))
        try:
            tmp_pdf.unlink(missing_ok=True)
        except OSError:
            pass  # si Windows el té obert, no passa res
        try:
            if not any((work / "img").iterdir()):
                (work / "img").rmdir()
        except OSError:
            pass
        (work / "doc.md").write_text(md, encoding="utf-8")
    except ConversorFaltant as e:
        shutil.rmtree(work, ignore_errors=True)
        print(e)
        sys.exit(1)
    except Exception as e:  # noqa: BLE001
        FALLITS.append((norm(pdf.name), f"{type(e).__name__}: {e}"))
        shutil.rmtree(work, ignore_errors=True)
        return None
    STATS["convertits"] += 1
    print(f"  PDF convertit ({motor}): {norm(pdf.name)}")
    return md, (cimg if cimg.is_dir() else None)


def escriu(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def esborra_docs():
    """Esborra docs/ de forma robusta a Windows (fitxers de només lectura,
    carpetes bloquejades un instant per l'antivirus o OneDrive...)."""
    def _treu_readonly(func, path, exc):
        try:
            os.chmod(path, stat.S_IWRITE)
            func(path)
        except Exception:
            raise

    for intent in range(5):
        try:
            if DOCS.exists():
                try:
                    shutil.rmtree(DOCS, onexc=_treu_readonly)  # Python 3.12+
                except TypeError:
                    shutil.rmtree(DOCS, onerror=_treu_readonly)  # més antic
            return
        except Exception:
            time.sleep(1)
    print(
        "\nNo puc esborrar la carpeta 'docs'. Tanca 'mkdocs serve' si el tens "
        "en marxa,\ntanca qualsevol terminal o finestra de l'Explorador que "
        "tingui oberta una carpeta dins de 'docs',\ni torna-ho a provar. "
        "(Si persisteix, esborra la carpeta 'docs' a mà.)"
    )
    sys.exit(1)


CSS = r''':root{
  --bg:#F6F8FB;--surface:#FFFFFF;--ink:#1A2230;--muted:#5A6677;--hairline:#E3E8EF;
  --accent:#2563EB;--accent-soft:#E6EEFD;--slate-soft:#EDF1F6;--slate-ink:#3A4658;
  --display:"Space Grotesk",-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;
  --body:"Inter",-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;
  --mono:"JetBrains Mono",ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;
}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{font-family:var(--body);color:var(--ink);background:var(--bg);line-height:1.55;-webkit-font-smoothing:antialiased;padding:clamp(1.5rem,5vw,4.5rem) clamp(1.25rem,5vw,3rem) 3rem}
.wrap{max-width:1080px;margin:0 auto}

.back{font-family:var(--mono);font-size:.78rem;color:var(--muted);text-decoration:none;display:inline-flex;align-items:center;gap:.4rem;transition:color .2s ease;margin-bottom:1.1rem}
.back:hover,.back:focus-visible{color:var(--accent)}
.eyebrow{font-family:var(--mono);font-size:.74rem;letter-spacing:.16em;text-transform:uppercase;color:var(--accent);display:flex;align-items:center;gap:.55rem}
.eyebrow::before{content:"";width:1.6rem;height:2px;background:var(--accent);display:inline-block;flex-shrink:0}
h1{font-family:var(--display);font-weight:700;font-size:clamp(2.1rem,5.5vw,3.4rem);letter-spacing:-.02em;line-height:1.05;margin:1.1rem 0 0}
h1 .code{color:var(--accent)}
.lede{color:var(--muted);font-size:clamp(1rem,1.6vw,1.18rem);max-width:60ch;margin-top:1.1rem}
.rule{height:1px;background:var(--hairline);margin:clamp(2rem,5vw,3rem) 0}
.section-title{font-family:var(--mono);font-size:.78rem;letter-spacing:.12em;text-transform:uppercase;color:var(--muted);margin:0 0 1rem}
.section-title:not(:first-child){margin-top:2.4rem}

/* Targetes */
.grid{display:grid;grid-template-columns:repeat(2,1fr);gap:clamp(.9rem,2vw,1.4rem)}
.card{position:relative;display:flex;flex-direction:column;background:var(--surface);border:1px solid var(--hairline);border-radius:16px;padding:1.6rem 1.6rem 1.4rem;text-decoration:none;color:inherit;overflow:hidden;transition:transform .22s ease,border-color .22s ease,box-shadow .22s ease}
.card::before{content:"";position:absolute;left:0;top:0;bottom:0;width:4px;background:var(--accent);transform:scaleY(0);transform-origin:top;transition:transform .26s ease}
a.card:hover,a.card:focus-visible{transform:translateY(-4px);border-color:#D6DEE8;box-shadow:0 14px 34px -18px rgba(26,34,48,.34);outline:none}
a.card:hover::before,a.card:focus-visible::before{transform:scaleY(1)}
a.card:focus-visible{box-shadow:0 0 0 3px var(--accent-soft),0 14px 34px -18px rgba(26,34,48,.34)}
.card-top{display:flex;align-items:center;justify-content:space-between;gap:.75rem;margin-bottom:1rem}
.aea-code{font-family:var(--mono);font-weight:600;font-size:.8rem;letter-spacing:.04em;color:#fff;background:var(--ink);padding:.32rem .6rem;border-radius:7px}
.tags{display:flex;gap:.4rem;flex-wrap:wrap;justify-content:flex-end}
.tag{font-family:var(--mono);font-size:.7rem;padding:.28rem .55rem;border-radius:6px;white-space:nowrap}
.tag.ra{background:var(--accent-soft);color:#1D4ED8}
.tag.soon{background:var(--slate-soft);color:var(--slate-ink)}
.card h2{font-family:var(--display);font-weight:600;font-size:1.18rem;letter-spacing:-.01em;line-height:1.25}
.card p{color:var(--muted);font-size:.93rem;margin-top:.55rem;flex:1}
.card .spacer{flex:1}
.open{margin-top:1.25rem;font-family:var(--mono);font-size:.8rem;font-weight:600;color:var(--accent);display:inline-flex;align-items:center;gap:.4rem}
.open .arrow{transition:transform .22s ease}
a.card:hover .open .arrow,a.card:focus-visible .open .arrow{transform:translateX(4px)}
.card.disabled{cursor:not-allowed;background:#FAFBFC;opacity:.62;filter:grayscale(.4)}
.card.disabled .aea-code{background:#9aa4b2}
.card.disabled .open{color:#9aa4b2}

/* Llista de recursos */
.resource-list{border-top:1px solid var(--hairline);margin-bottom:.5rem}
.resource{display:flex;align-items:center;gap:1rem;padding:1.05rem .35rem;border-bottom:1px solid var(--hairline);text-decoration:none;color:inherit;transition:background .18s ease}
.resource:hover,.resource:focus-visible{background:var(--surface);outline:none}
.resource-icon{flex-shrink:0;width:38px;height:38px;border-radius:10px;background:var(--slate-soft);display:flex;align-items:center;justify-content:center;color:var(--slate-ink)}
.resource-icon svg{width:18px;height:18px;stroke:currentColor;fill:none;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round}
.resource-body{flex:1;min-width:0;display:flex;align-items:baseline;gap:.55rem;flex-wrap:wrap}
.resource-type{font-family:var(--mono);font-size:.7rem;color:var(--accent);background:var(--accent-soft);padding:.2rem .5rem;border-radius:6px;white-space:nowrap;flex-shrink:0}
.resource-title{font-weight:500;font-size:.96rem;color:var(--ink);min-width:0;word-break:break-word}
.empty{background:var(--surface);border:1px dashed #C9D2DE;border-radius:16px;padding:2rem 1.6rem;color:var(--muted);text-align:center}
.empty strong{display:block;font-family:var(--display);font-size:1.15rem;color:var(--ink);margin-bottom:.3rem}

/* Pàgines de contingut */
.toc{display:flex;flex-wrap:wrap;gap:.45rem;align-items:center;margin:0 0 1.8rem;font-family:var(--mono);font-size:.74rem}
.toc span{color:var(--muted);margin-right:.3rem;text-transform:uppercase;letter-spacing:.1em}
.toc a{color:var(--slate-ink);background:var(--surface);border:1px solid var(--hairline);padding:.3rem .65rem;border-radius:999px;text-decoration:none}
.toc a:hover{color:var(--accent);border-color:var(--accent)}
.prose{background:var(--surface);border:1px solid var(--hairline);border-radius:16px;padding:clamp(1.4rem,4vw,2.6rem);font-size:1rem}
.prose>*+*{margin-top:1rem}
.prose h1{font-size:clamp(1.8rem,4.2vw,2.5rem);margin:0 0 .4rem}
.prose h2{font-family:var(--display);font-weight:600;font-size:1.55rem;letter-spacing:-.01em;line-height:1.2;margin-top:2.4rem;padding-top:1.6rem;border-top:1px solid var(--hairline)}
.prose h3{font-family:var(--display);font-weight:600;font-size:1.15rem;margin-top:1.6rem}
.prose h4{font-weight:600;margin-top:1.3rem}
.prose p,.prose li{color:#2b3546}
.prose ul,.prose ol{padding-left:1.4rem}
.prose li+li{margin-top:.35rem}
.prose a{color:var(--accent)}
.prose strong{color:var(--ink)}
.prose em{color:var(--muted)}
.prose code{font-family:var(--mono);font-size:.86em;background:var(--slate-soft);color:var(--slate-ink);padding:.12em .4em;border-radius:5px}
.prose pre{background:#0F1724;color:#E6EDF5;border-radius:12px;padding:1.1rem 1.3rem;overflow-x:auto;line-height:1.5}
.prose pre code{background:none;color:inherit;padding:0;font-size:.85rem}
.prose img{max-width:100%;height:auto;display:block;border-radius:12px;border:1px solid var(--hairline);box-shadow:0 10px 30px -22px rgba(26,34,48,.5);margin-top:1.4rem}
.prose table{border-collapse:collapse;width:100%;font-size:.93rem;display:block;overflow-x:auto}
.prose th{background:var(--ink);color:#fff;text-align:left;font-weight:600;padding:.65rem .85rem}
.prose td{padding:.6rem .85rem;border-bottom:1px solid var(--hairline)}
.prose tr:nth-child(even) td{background:#FAFBFD}
.prose blockquote{border-left:4px solid var(--accent);background:var(--accent-soft);padding:.8rem 1.1rem;border-radius:0 10px 10px 0}
.prose hr{border:0;height:1px;background:var(--hairline)}
.admonition{border-left:4px solid #3b82c4;background:#EEF5FC;border-radius:0 12px 12px 0;padding:.85rem 1.15rem}
.admonition>*+*{margin-top:.6rem}
.admonition-title{font-family:var(--mono);font-size:.74rem;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:#2b6aa3}
.admonition.tip,.admonition.success,.admonition.example{border-color:#1f9d55;background:#EDF8F1}
.admonition.tip .admonition-title,.admonition.success .admonition-title,.admonition.example .admonition-title{color:#17783f}
.admonition.warning,.admonition.danger,.admonition.failure{border-color:#d9534f;background:#FDF0EF}
.admonition.warning .admonition-title,.admonition.danger .admonition-title,.admonition.failure .admonition-title{color:#b03a37}
.admonition.abstract,.admonition.question{border-color:var(--accent);background:var(--accent-soft)}
.admonition.abstract .admonition-title,.admonition.question .admonition-title{color:#1D4ED8}

footer{margin-top:clamp(2.5rem,6vw,4rem);padding-top:1.5rem;border-top:1px solid var(--hairline);color:var(--muted);font-size:.82rem;font-family:var(--mono);letter-spacing:.01em}
@media (max-width:680px){.grid{grid-template-columns:1fr}}
@media (prefers-reduced-motion:reduce){*{transition:none !important;scroll-behavior:auto}}
'''


# ----------------------------------------------------------------------------
# Disseny: HTML, targetes i pàgines
# ----------------------------------------------------------------------------
esc = html.escape
MARCADOR_DIAPOSITIVES = "Material en format diapositives."

ICONES = {
    "diapositives": '<rect x="3" y="4" width="18" height="12" rx="1"/><line x1="8" y1="20" x2="16" y2="20"/><line x1="12" y1="16" x2="12" y2="20"/>',
    "pagina": '<path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><polyline points="14 3 14 8 19 8"/><line x1="9" y1="13" x2="15" y2="13"/><line x1="9" y1="17" x2="15" y2="17"/>',
    "html": '<polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/>',
    "fitxer": '<path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/>',
}
ETIQUETES = {"diapositives": "Diapositives", "pagina": "Pàgina", "html": "Interactiu", "fitxer": "Fitxer"}
EXT_IMATGE = {".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".ico"}


def natural(s):
    s = sense_accents(norm(s)).lower()
    return [int(t) if t.isdigit() else t for t in re.split(r"(\d+)", s)]


def rel_href(destino, des_de_dir):
    """Ruta relativa (codificada per a URL) des d'una carpeta fins a un fitxer."""
    r = os.path.relpath(str(destino), str(des_de_dir)).replace(os.sep, "/")
    return quote(r, safe="/#")


def prefix_de(path):
    prof = len(Path(path).relative_to(DOCS).parts) - 1
    return "../" * prof


def pagina(path, titol, cos):
    pre = prefix_de(path)
    return f"""<!DOCTYPE html>
<html lang="ca">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(titol)} · {esc(SITE_NAME)}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{pre}assets/style.css">
</head>
<body>
<div class="wrap">
{cos}
  <footer>{esc(FOOTER)}</footer>
</div>
</body>
</html>
"""


def capcalera(eyebrow, h1_html, lede=None, back=None):
    b = f'<a class="back" href="{back[0]}">← {esc(back[1])}</a>\n    ' if back else ""
    l = f'\n    <p class="lede">{esc(lede)}</p>' if lede else ""
    return f"""  <header>
    {b}<div class="eyebrow">{esc(eyebrow)}</div>
    <h1>{h1_html}</h1>{l}
  </header>

  <div class="rule"></div>
"""


def titol_h1(codi, titol):
    return f'{esc(codi)} <span class="code">—</span> {esc(titol)}'


def targeta(codi, titol, desc, href, tag=None, disabled=False):
    t = f'<span class="tags"><span class="tag {"soon" if disabled else "ra"}">{esc(tag)}</span></span>' if tag else ""
    d = f"<p>{esc(desc)}</p>" if desc else '<div class="spacer"></div>'
    cont = f"""      <div class="card-top">
        <span class="aea-code">{esc(codi)}</span>
        {t}
      </div>
      <h2>{esc(titol)}</h2>
      {d}"""
    if disabled:
        return f"""    <div class="card disabled" aria-disabled="true">
{cont}
      <span class="open">Properament</span>
    </div>
"""
    return f"""    <a class="card" href="{href}">
{cont}
      <span class="open">Obrir <span class="arrow">→</span></span>
    </a>
"""


def recurs(titol, href, tipus, nova_pestanya=False):
    tgt = ' target="_blank" rel="noopener"' if nova_pestanya else ""
    return f"""    <a class="resource" href="{href}"{tgt}>
      <span class="resource-icon" aria-hidden="true"><svg viewBox="0 0 24 24">{ICONES[tipus]}</svg></span>
      <span class="resource-body">
        <span class="resource-type">{ETIQUETES[tipus]}</span>
        <span class="resource-title">{esc(titol)}</span>
      </span>
    </a>
"""


def properament_caixa(text="El material d'aquest apartat estarà disponible aviat."):
    return f"""  <div class="empty"><strong>Material properament</strong>{esc(text)}</div>
"""


# ----------------------------------------------------------------------------
# Markdown -> HTML
# ----------------------------------------------------------------------------
def md_a_html(text):
    try:
        import markdown
    except Exception:  # noqa: BLE001
        print(
            "\nFalta la llibreria 'markdown'. Instal·la-la amb EXACTAMENT aquest Python:\n"
            f'  "{sys.executable}" -m pip install markdown\n'
        )
        sys.exit(1)
    md = markdown.Markdown(
        extensions=["tables", "fenced_code", "admonition", "attr_list",
                    "md_in_html", "sane_lists", "toc"],
        extension_configs={"toc": {"permalink": False}},
    )
    cos = md.convert(text)
    h2 = []

    def recull(tokens):
        for t in tokens:
            if t["level"] == 2:
                h2.append((t["id"], t["name"]))
            recull(t.get("children", []))

    recull(getattr(md, "toc_tokens", []))
    return cos, h2


def titol_md(text, defecte):
    m = re.search(r"^#\s+(.+?)\s*#*\s*$", text, re.M)
    return re.sub(r"[`*_]", "", m.group(1)).strip() if m else defecte


def assegura_h1(text, titol):
    if re.search(r"^#\s+\S", text, re.M):
        return text
    return f"# {titol}\n\n{text}"


def pagina_contingut(path, md_text, titol, back_href, back_text, eyebrow):
    cos, h2 = md_a_html(md_text)
    toc = ""
    if len(h2) >= 3:
        enllacos = "".join(f'<a href="#{esc(i)}">{esc(re.sub(r"<[^>]+>", "", n))}</a>' for i, n in h2)
        toc = f'  <nav class="toc"><span>Contingut</span>{enllacos}</nav>\n'
    cap = f"""  <header>
    <a class="back" href="{back_href}">← {esc(back_text)}</a>
    <div class="eyebrow">{esc(eyebrow)}</div>
  </header>
  <div class="rule"></div>
"""
    return pagina(path, titol, f"{cap}{toc}  <article class=\"prose\">\n{cos}\n  </article>\n")


# ----------------------------------------------------------------------------
# Material d'un RA / mòdul
# ----------------------------------------------------------------------------
def te_germa_publicable(f):
    """Hi ha un .md/.html amb el mateix nom (sense espais/tildes) al costat?"""
    for x in f.parent.iterdir():
        if x.suffix.lower() in (".md", ".html", ".htm") and slug(norm(x.stem)) == slug(norm(f.stem)):
            return True
    return False


def processa_material(fitxers, base, desti, index_path, nom_pagina_tornar, eyebrow):
    """Genera les pàgines/còpies d'un conjunt de fitxers de teoria.
    base: carpeta d'origen (Teoria); desti: carpeta de sortida.
    index_path: pàgina a la qual tornen les pàgines de contingut.
    Retorna llista de dicts {grup, titol, path, tipus, nova}."""
    res = []
    usats = {"index.html"}

    def lliure(rel_dir, nom):
        n, k = nom, 2
        stem, ext = os.path.splitext(nom)
        while (rel_dir + "/" + n).lower() in usats:
            n = f"{stem}-{k}{ext}"
            k += 1
        usats.add((rel_dir + "/" + n).lower())
        return n

    for f in sorted(fitxers, key=lambda x: natural(str(x.relative_to(base)))):
        rel = f.relative_to(base)
        dirs = [norm(p) for p in rel.parts[:-1]]
        grup = " / ".join(dirs)
        rel_dir = "/".join(dirs)
        out_dir = desti.joinpath(*dirs) if dirs else desti
        ext = f.suffix.lower()
        stem = norm(f.stem)

        # --- imatges: es copien (per als .md propis) però no es llisten
        if ext in EXT_IMATGE:
            out_dir.mkdir(parents=True, exist_ok=True)
            nom = lliure(rel_dir, norm(f.name))
            shutil.copy2(f, out_dir / nom)
            continue

        # --- PDF -> pàgina (el PDF no es publica)
        if ext == ".pdf" and CONVERTIR_PDF:
            if te_germa_publicable(f):
                continue
            r = converteix_pdf(f)
            if r is None:
                continue
            md, cimg = r
            nom = lliure(rel_dir, slug(stem, 80) + ".html")
            out_dir.mkdir(parents=True, exist_ok=True)
            img_nom = Path(nom).stem + "-img"
            if cimg is not None:
                shutil.copytree(cimg, out_dir / img_nom, dirs_exist_ok=True)
            md = md.replace(TOKEN_IMG, quote(img_nom) + "/")
            md = assegura_h1(md, stem)
            path = out_dir / nom
            escriu(path, pagina_contingut(
                path, md, stem, rel_href(index_path, path.parent),
                nom_pagina_tornar, eyebrow))
            tipus = "diapositives" if MARCADOR_DIAPOSITIVES in md else "pagina"
            res.append(dict(grup=grup, titol=stem, path=path, tipus=tipus, nova=False))
            continue

        # --- Markdown -> pàgina
        if ext == ".md":
            text = f.read_text(encoding="utf-8-sig", errors="replace")
            titol = titol_md(text, stem)
            text = assegura_h1(text, titol)
            nom = lliure(rel_dir, slug(stem, 80) + ".html")
            path = out_dir / nom
            escriu(path, pagina_contingut(
                path, text, titol, rel_href(index_path, path.parent),
                nom_pagina_tornar, eyebrow))
            res.append(dict(grup=grup, titol=titol, path=path, tipus="pagina", nova=False))
            continue

        # --- HTML propi: es publica tal qual
        out_dir.mkdir(parents=True, exist_ok=True)
        nom = lliure(rel_dir, norm(f.name))
        shutil.copy2(f, out_dir / nom)
        if ext in (".html", ".htm"):
            t = re.search(r"<title>(.*?)</title>", f.read_text(encoding="utf-8", errors="replace"), re.I | re.S)
            titol = html.unescape(t.group(1)).strip() if t and t.group(1).strip() else stem
            res.append(dict(grup=grup, titol=titol, path=out_dir / nom, tipus="html", nova=True))
        else:
            if f.stat().st_size > AVIS_MB_FITXER * 1024 * 1024:
                GRANS.append((norm(f.name), f.stat().st_size // (1024 * 1024)))
            res.append(dict(grup=grup, titol=norm(f.name), path=out_dir / nom, tipus="fitxer", nova=True))
    res.sort(key=lambda r: (natural(r["grup"]), natural(r["titol"])))
    return res


def llista_recursos(res, pagina_dir):
    """HTML de la llista de recursos, agrupada per subcarpeta."""
    out = []
    grups = []
    for r in res:
        if r["grup"] not in grups:
            grups.append(r["grup"])
    for g in sorted(grups, key=natural):
        if g:
            out.append(f'  <h3 class="section-title">{esc(g)}</h3>')
        out.append('  <div class="resource-list">')
        for r in res:
            if r["grup"] == g:
                out.append(recurs(r["titol"], rel_href(r["path"], pagina_dir), r["tipus"], r["nova"]))
        out.append("  </div>")
    return "\n".join(out) + "\n"


def llegeix_descripcio(carpeta):
    for x in carpeta.iterdir():
        if x.is_file() and sense_accents(x.name).lower() == "descripcio.txt":
            return " ".join(x.read_text(encoding="utf-8-sig", errors="replace").split())
    return ""


# ----------------------------------------------------------------------------
# Construcció de mòduls, cicles i portada
# ----------------------------------------------------------------------------
RE_RA = re.compile(r"(?i)^ra\s*(\d+)\s*[-–—:._)]*\s*(.*)$")


def construeix_modul(m_dir, c_slug, c_nom, codi, nom):
    ms = f"{codi}-{slug(nom, 40)}"
    mod_dir = DOCS / c_slug / ms
    mod_index = mod_dir / "index.html"
    cicle_index = DOCS / c_slug / "index.html"
    teoria_mod = troba_teoria(m_dir)
    eyebrow_mod = f"{c_nom} · M{codi}"

    ras_dirs = [d for d in subcarpetes(m_dir) if RE_RA.match(norm(d.name))]
    if teoria_mod:
        ras_dirs += [d for d in subcarpetes(teoria_mod) if RE_RA.match(norm(d.name))]
    ras_dirs.sort(key=lambda d: natural(d.name))

    # Material a nivell de mòdul (fora de les carpetes RA)
    nom_ras = {norm(d.name) for d in ras_dirs}
    fit_mod = []
    if teoria_mod:
        fit_mod = [f for f in fitxers_teoria(teoria_mod)
                   if norm(f.relative_to(teoria_mod).parts[0]) not in nom_ras]
    mat_mod = processa_material(
        fit_mod, teoria_mod, mod_dir, mod_index,
        f"Tornar a M{codi}", eyebrow_mod) if fit_mod else []

    ras = []
    usats = set()
    for ra in ras_dirs:
        m = RE_RA.match(norm(ra.name))
        n = int(m.group(1))
        s = f"ra{n}"
        while s in usats:
            s += "b"
        usats.add(s)
        titol_ra = (m.group(2) or "").strip()
        ra_dir_out = mod_dir / s
        ra_index = ra_dir_out / "index.html"
        t = troba_teoria(ra)
        if t is None and teoria_mod and ra.parent == teoria_mod:
            t = ra
        fit = fitxers_teoria(t) if t else []
        mat = processa_material(
            fit, t, ra_dir_out, ra_index, f"Tornar a RA{n}",
            f"{c_nom} · M{codi} · RA{n}") if fit else []
        desc = llegeix_descripcio(ra)
        # pàgina de l'RA
        cap = capcalera(
            f"{c_nom} · M{codi} · RA{n}",
            titol_h1(f"RA{n}", titol_ra or f"Resultat d'aprenentatge {n}"),
            desc or None,
            (rel_href(mod_index, ra_dir_out), f"Tornar a M{codi}"))
        if mat:
            cos = cap + llista_recursos(mat, ra_dir_out)
        else:
            cos = cap + properament_caixa()
        escriu(ra_index, pagina(ra_index, f"RA{n} · {titol_ra or nom}", cos))
        ras.append(dict(n=n, titol=titol_ra or f"RA{n}", index=ra_index, mat=mat, desc=desc))

    # pàgina del mòdul
    desc_mod = llegeix_descripcio(m_dir)
    cap = capcalera(
        eyebrow_mod, titol_h1(f"M{codi}", nom),
        desc_mod or "Resultats d'aprenentatge i material del mòdul.",
        (rel_href(cicle_index, mod_dir), f"Tornar a {c_nom.split(' · ')[0]}"))
    cos = cap
    if mat_mod:
        cos += '  <h2 class="section-title">Material general</h2>\n' + llista_recursos(mat_mod, mod_dir)
    if ras:
        cos += '  <h2 class="section-title">Resultats d\'aprenentatge</h2>\n  <main class="grid">\n'
        for r in ras:
            ok = bool(r["mat"])
            cos += targeta(
                f"RA{r['n']}", r["titol"], r["desc"],
                rel_href(r["index"], mod_dir), tag=(f"{len(r['mat'])} material{'s' if len(r['mat']) != 1 else ''}" if ok else "Properament"),
                disabled=not ok)
        cos += "  </main>\n"
    elif not mat_mod:
        cos += properament_caixa()
    escriu(mod_index, pagina(mod_index, f"M{codi} {nom}", cos))
    return dict(codi=codi, nom=nom, index=mod_index, ras=ras, mat=mat_mod,
                desc=desc_mod, ok=bool(mat_mod) or any(r["mat"] for r in ras))


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    origen = Path(sys.argv[1]).expanduser()
    if not origen.is_dir():
        print(f"No trobo la carpeta: {origen}")
        sys.exit(1)

    esborra_docs()
    DOCS.mkdir()
    escriu(DOCS / "assets" / "style.css", CSS)
    escriu(DOCS / ".nojekyll", "")

    ignorades = []
    resum = []
    cicles_info = []

    for cicle, c_nom in CICLES.items():
        c_dir = next((d for d in origen.iterdir() if d.is_dir() and d.name.upper() == cicle), None)
        c_slug = cicle.lower()
        c_index = DOCS / c_slug / "index.html"
        moduls = []
        if c_dir:
            for m in sorted(subcarpetes(c_dir), key=lambda d: natural(d.name)):
                mm = re.match(r"^(\d{4})\s+(.+)$", norm(m.name).strip())
                if not mm:
                    ignorades.append(f"{cicle}/{norm(m.name)}")
                    continue
                moduls.append(construeix_modul(m, c_slug, f"{cicle}", mm.group(1), mm.group(2)))
        for md_ in moduls:
            resum.append((cicle, f"M{md_['codi']} {md_['nom']}", md_["ok"]))

        # pàgina del cicle
        cap = capcalera(
            f"Cicle {cicle}", titol_h1(cicle, c_nom),
            f"Mòduls de {cicle} amb el seu material.",
            (rel_href(DOCS / "index.html", c_index.parent), "Tornar a l'inici"))
        if moduls:
            cos = cap + '  <main class="grid">\n'
            for md_ in moduls:
                n_ok = sum(1 for r in md_["ras"] if r["mat"])
                if not md_["ok"]:
                    tag = "Properament"
                elif n_ok:
                    tag = f"{n_ok}/{len(md_['ras'])} RA"
                else:
                    tag = "Material"
                cos += targeta(f"M{md_['codi']}", md_["nom"], md_["desc"],
                               rel_href(md_["index"], c_index.parent), tag=tag, disabled=not md_["ok"])
            cos += "  </main>\n"
        else:
            cos = cap + properament_caixa(f"Encara no hi ha mòduls publicats a {cicle}.")
        escriu(c_index, pagina(c_index, f"{cicle} · {c_nom}", cos))
        cicles_info.append((cicle, c_nom, c_index, moduls))

    # portada
    h_index = DOCS / "index.html"
    cos = capcalera(SITE_EYEBROW, esc(SITE_NAME), SITE_LEDE) + '  <main class="grid">\n'
    for cicle, c_nom, c_index, moduls in cicles_info:
        n_ok = sum(1 for m in moduls if m["ok"])
        tag = f"{n_ok} mòdul{'s' if n_ok != 1 else ''}" if n_ok else "Properament"
        cos += targeta(cicle, c_nom, "", rel_href(c_index, DOCS), tag=tag, disabled=not n_ok)
    cos += "  </main>\n"
    escriu(h_index, pagina(h_index, SITE_NAME, cos))

    # resum per pantalla
    print("\nWeb generada. Resum:")
    for cicle, titol, ok in resum:
        print(f"  [{'amb material' if ok else 'properament'}] {cicle} · {titol}")
    if ignorades:
        print("\nCarpetes NO publicades (no segueixen el patró '0000 Nom del mòdul'):")
        for i in ignorades:
            print("  -", i)
    mida = sum(f.stat().st_size for f in DOCS.rglob("*") if f.is_file()) / 1048576
    print(f"\nMida de la web (docs): {mida:.1f} MB")
    if mida > AVIS_MB_TOTAL:
        print(f"  ATENCIÓ: passa de {AVIS_MB_TOTAL} MB. GitHub Pages admet 1 GB com a màxim.")
    if STATS["convertits"] or STATS["cache"]:
        print(f"PDF convertits ara: {STATS['convertits']} · reutilitzats de la memòria cau: {STATS['cache']}")
    if FALLITS:
        print("\nPDF NO convertits (no apareixen a la web):")
        for n, e in FALLITS:
            print(f"  - {n}: {e}")
    if GRANS:
        print(f"\nFitxers (no PDF) de més de {AVIS_MB_FITXER} MB que es pujaran tal qual:")
        for n, mb in GRANS:
            print(f"  - {n} ({mb} MB)")
    print("\nSegüent pas: obre docs/index.html al navegador per veure-la, o puja els canvis amb GitHub Desktop.")


if __name__ == "__main__":
    main()