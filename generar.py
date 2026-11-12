#!/usr/bin/env python3
r"""
Genera la web (carpeta docs/) a partir de la carpeta de material que tens
al teu ordinador. Disseny de targetes: Cicle -> Mòdul -> RA -> Material.

Estructura que espera la carpeta d'origen:

    CICLE (ASIX, DAM, DAW, SMIX)
      └── 0378 Nom del mòdul
            ├── RA1 - Nom del resultat d'aprenentatge
            │     └── Teoria        <- només aquesta carpeta es publica
            └── RA2 - ...

PDF: no es publiquen a la web per estalviar espai (es comparteixen per Google Drive). Enllaços (p. ex. una carpeta de Google Drive):
fitxer "enllacos.txt" dins de Teoria, una línia per enllaç ("Títol | https://...").

Presentacions .pptx: es converteixen a pàgina (títols, llistes, taules, imatges);
les notes del presentador i les diapositives ocultes NO es publiquen.

Ús:
    python generar.py "C:\ruta\a\la\carpeta\de\material"
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
from urllib.parse import quote, urlparse

# ----------------------------------------------------------------------------
# CONFIGURACIÓ (edita aquí el que necessitis)
# ----------------------------------------------------------------------------
SITE_NAME = "Material docent"
SITE_EYEBROW = "Formació Professional · Informàtica"
SITE_LEDE = "Material de les asignatures de ASIX DAM DAW i SMIX"
FOOTER = "Material docent · Formació Professional · Informàtica"

EXCLOURE = {"gestio", "gestions", "ordenar", ".git", "examen", "exercicis", "desktop.ini"}

CICLES = {
    "ASIX": "Administració de Sistemes Informàtics en Xarxa",
    "DAM": "Desenvolupament d'Aplicacions Multiplataforma",
    "DAW": "Desenvolupament d'Aplicacions Web",
    "SMIX": "Sistemes Microinformàtics i Xarxes",
}

CONVERTIR_PDF = True
IMATGES_PDF = True
PDF_SENSE_TEXT_COM_IMATGES = True

# Què fer amb els PDF de les carpetes Teoria:
#   "descarrega" = es publica el PDF original perquè els alumnes el descarreguin
#   "pagina"     = es converteix a pàgina web (el PDF no es publica)
#   "ambdos"     = les dues coses
#   "cap"        = no es publiquen els PDF (es comparteixen per Google Drive)
PDF_MODE = "cap"

# Presentacions PowerPoint (.pptx): es converteixen a pàgina web (el PPTX no es publica).
CONVERTIR_PPTX = True
PPTX_IMATGES = True            # extreure les imatges de les diapositives
PPTX_SALTAR_OCULTES = True     # no publicar les diapositives ocultes
PPTX_INCLOURE_NOTES = False    # les notes del presentador NO es publiquen (poden ser privades)
AMPLADA_PAGINA_PX = 1400
QUALITAT_JPG = 80

AVIS_MB_FITXER = 20     # fitxer (no PDF) que es puja tal qual
AVIS_MB_TOTAL = 300     # mida total de docs/

ROOT = Path(__file__).resolve().parent
DOCS = ROOT / "docs"


# ----------------------------------------------------------------------------
# Utilitats i conversió de PDF
# ----------------------------------------------------------------------------
def norm(s):
    return unicodedata.normalize("NFC", s)


def sense_accents(s):
    s = unicodedata.normalize("NFKD", s)
    return "".join(c for c in s if not unicodedata.combining(c))


def slug(s, maxlen=60):
    s = sense_accents(s).lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return (s[:maxlen].strip("-")) or "x"


def excluit(nom):
    n = sense_accents(nom).lower()
    return (n in EXCLOURE
            or nom.startswith(".")
            or nom.startswith("_")
            or n.endswith(".ini")
            or nom.startswith("~$"))


def es_teoria(nom):
    return sense_accents(nom).lower() == "teoria"


def subcarpetes(p):
    return sorted(
        (d for d in p.iterdir() if d.is_dir() and not excluit(d.name)),
        key=lambda d: norm(d.name).lower(),
    )


def fitxers_teoria(carpeta):
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
FALLITS = []
GRANS = []
STATS = {"convertits": 0, "cache": 0}


def _pdf_a_markdown(pdf_tmp, img_dir):
    err_import = None
    try:
        import pymupdf4llm
    except Exception as e:
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
        except Exception as e:
            print(f"  (pymupdf4llm ha fallat: {e}; provo amb markitdown)")

    if err_import and not AVISAT:
        AVISAT.append(1)
        print(
            f"  AVÍS: no puc carregar pymupdf4llm ({err_import}).\n"
            "  Faig servir un conversor més simple."
        )

    try:
        from markitdown import MarkItDown
    except Exception:
        MarkItDown = None
    if MarkItDown is not None:
        return MarkItDown().convert(str(pdf_tmp)).text_content, "markitdown"

    try:
        from pypdf import PdfReader
    except Exception:
        raise ConversorFaltant(
            "\nNo puc convertir els PDF: no es pot carregar cap conversor.\n"
            f"  Python: {sys.executable}\n"
            f"  Motiu: {err_import}\n"
        )
    pagines = [(p.extract_text() or "").strip() for p in PdfReader(str(pdf_tmp)).pages]
    return "\n\n".join(t for t in pagines if t), "pypdf"


def _reescriu_imatges(md, img_dir):
    def canvia(m):
        nom = re.split(r"[\\/]", m.group(2).strip())[-1]
        if (img_dir / nom).is_file():
            return f"![{m.group(1)}]({TOKEN_IMG}{nom})"
        return ""

    return re.sub(r"!\[([^\]]*)\]\(([^)]*)\)", canvia, md)


def _pdf_com_imatges(pdf_tmp, img_dir, titol):
    shutil.rmtree(img_dir, ignore_errors=True)
    img_dir.mkdir(parents=True)
    n = 0
    try:
        import fitz

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
    except Exception:
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
    st = pdf.stat()
    clau = hashlib.sha1(
        f"{pdf.resolve()}|{st.st_size}|{st.st_mtime_ns}|{IMATGES_PDF}".encode()
    ).hexdigest()[:16]
    cdir = CACHE / clau
    cmd, cimg = cdir / "doc.md", cdir / "img"
    if cmd.is_file():
        STATS["cache"] += 1
        return cmd.read_text(encoding="utf-8"), (cimg if cimg.is_dir() else None)

    work = cdir
    shutil.rmtree(work, ignore_errors=True)
    (work / "img").mkdir(parents=True, exist_ok=True)
    tmp_pdf = work / "doc.pdf"
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
            pass
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
    except Exception as e:
        FALLITS.append((norm(pdf.name), f"{type(e).__name__}: {e}"))
        shutil.rmtree(work, ignore_errors=True)
        return None
    STATS["convertits"] += 1
    print(f"  PDF convertit ({motor}): {norm(pdf.name)}")
    return md, (cimg if cimg.is_dir() else None)


# ----------------------------------------------------------------------------
# PPTX -> Markdown (el PPTX NO es publica: només la pàgina generada)
# ----------------------------------------------------------------------------
AVISOS_PPTX = []   # (fitxer, diapositiva, descripció) d'elements no convertits
_AVIS_LLIBRERIA_PPTX = []
FONTS_MONO = ("consolas", "courier", "mono", "menlo", "monaco", "lucida console",
              "jetbrains", "fira code", "source code", "cascadia")


def _md_text(t):
    """Escapa el text perquè el Markdown no el confongui amb format o HTML."""
    t = t.replace("\\", "\\\\")
    for c in ("*", "_", "`", "[", "]"):
        t = t.replace(c, "\\" + c)
    return t.replace("<", "&lt;").replace(">", "&gt;")


def _escapa_inici(t):
    t = re.sub(r"^(\d+)([.)])(\s)", r"\1\\\2\3", t)
    if t[:1] in ("-", "+", "#"):
        t = "\\" + t
    return t


def _envolta(t, marca):
    nucli = t.strip()
    if not nucli:
        return t
    ini = t[: len(t) - len(t.lstrip())]
    fi = t[len(t.rstrip()):]
    return f"{ini}{marca}{nucli}{marca}{fi}"


def _paragraf_md(par, treu_vinyeta=False):
    """Text d'un paràgraf amb negreta, cursiva, codi i enllaços."""
    from pptx.oxml.ns import qn
    from pptx.text.text import _Run

    trossos = []   # [text, negreta, cursiva, codi, enllaç]
    for fill in par._p:
        if fill.tag == qn("a:r"):
            run = _Run(fill, par)
            t = run.text
            if not t:
                continue
            nom = (run.font.name or "").lower()
            codi = any(m in nom for m in FONTS_MONO)
            try:
                enllac = run.hyperlink.address
            except Exception:  # noqa: BLE001
                enllac = None
            clau = [bool(run.font.bold), bool(run.font.italic), codi, enllac]
            if trossos and trossos[-1][1:] == clau:
                trossos[-1][0] += t
            else:
                trossos.append([t] + clau)
        elif fill.tag == qn("a:br"):
            trossos.append(["\n", False, False, False, None])
    if treu_vinyeta and trossos:
        trossos[0][0] = re.sub(r"^\s*[•·▪◦‣\-–]\s*", "", trossos[0][0])
    out = []
    for t, neg, curs, codi, enllac in trossos:
        if t == "\n":
            out.append("  \n")
            continue
        if codi:
            s = t.strip()
            s = f"{t[:len(t) - len(t.lstrip())]}`{s}`{t[len(t.rstrip()):]}" if s else t
        else:
            s = _md_text(t)
            if neg:
                s = _envolta(s, "**")
            if curs:
                s = _envolta(s, "*")
        if enllac and not codi and t.strip():
            nucli = s.strip()
            s = s.replace(nucli, f"[{nucli}]({enllac})", 1)
        out.append(s)
    return "".join(out).strip()


def _es_vinyeta(par, forma):
    from pptx.oxml.ns import qn
    ppr = par._p.pPr
    if ppr is not None:
        if ppr.find(qn("a:buNone")) is not None:
            return False, False
        if ppr.find(qn("a:buAutoNum")) is not None:
            return True, True
        if ppr.find(qn("a:buChar")) is not None:
            return True, False
    if par.level > 0:
        return True, False
    try:
        if forma.is_placeholder:
            from pptx.enum.shapes import PP_PLACEHOLDER
            if forma.placeholder_format.type in (PP_PLACEHOLDER.BODY, PP_PLACEHOLDER.OBJECT):
                return True, False
    except Exception:  # noqa: BLE001
        pass
    return False, False


def _text_forma_md(forma):
    """Markdown del text d'una forma (paràgrafs i llistes)."""
    linies = []
    en_llista = False
    for par in forma.text_frame.paragraphs:
        t = _paragraf_md(par)
        if not t:
            continue
        vinyeta, numerada = _es_vinyeta(par, forma)
        if vinyeta:
            if not en_llista and linies:
                linies.append("")
            marca = "1. " if numerada else "- "
            linies.append("    " * min(par.level, 4) + marca + t)
            en_llista = True
        else:
            if linies:
                linies.append("")
            linies.append(_escapa_inici(t))
            en_llista = False
    return "\n".join(linies)


def _taula_md(taula):
    files = []
    for fila in taula.rows:
        cel = []
        for c in fila.cells:
            parts = [_md_text(" ".join(p.text.split())) for p in c.text_frame.paragraphs if p.text.strip()]
            cel.append((" <br> ".join(parts)).replace("|", "\\|") or " ")
        files.append(cel)
    if not files:
        return ""
    n = max(len(f) for f in files)
    files = [f + [" "] * (n - len(f)) for f in files]
    out = ["| " + " | ".join(files[0]) + " |", "|" + "|".join(["---"] * n) + "|"]
    out += ["| " + " | ".join(f) + " |" for f in files[1:]]
    return "\n".join(out)


def _grafic_md(grafic):
    plot = grafic.plots[0]
    cats = [str(c) for c in plot.categories]
    series = [(s.name or "Sèrie", list(s.values)) for s in plot.series]
    cap = "| " + " | ".join([" "] + [_md_text(str(n)) for n, _ in series]) + " |"
    sep = "|" + "|".join(["---"] * (len(series) + 1)) + "|"
    files = []
    for i, c in enumerate(cats):
        vals = [("" if i >= len(v) or v[i] is None else
                 (str(int(v[i])) if float(v[i]).is_integer() else str(v[i]))) for _, v in series]
        files.append("| " + " | ".join([_md_text(c)] + vals) + " |")
    return "\n".join([cap, sep] + files)


def _desa_imatge(blob, img_dir, n):
    import io
    from PIL import Image
    im = Image.open(io.BytesIO(blob))
    im.load()
    if im.width < 48 or im.height < 48:
        return None
    if im.width > AMPLADA_PAGINA_PX:
        h = round(im.height * AMPLADA_PAGINA_PX / im.width)
        im = im.resize((AMPLADA_PAGINA_PX, h), Image.LANCZOS)
    alfa = im.mode in ("RGBA", "LA") or (im.mode == "P" and "transparency" in im.info)
    if alfa:
        nom = f"img-{n:03d}.png"
        im.convert("RGBA").save(img_dir / nom, "PNG", optimize=True)
    else:
        nom = f"img-{n:03d}.jpg"
        im.convert("RGB").save(img_dir / nom, "JPEG", quality=QUALITAT_JPG, optimize=True)
    return nom


def _formes(formes):
    from pptx.enum.shapes import MSO_SHAPE_TYPE
    for f in formes:
        if f.shape_type == MSO_SHAPE_TYPE.GROUP:
            yield from _formes(f.shapes)
        else:
            yield f


# ---- Lectura "intel·ligent" de diapositives fetes de caixes (p. ex. Google Slides) ----
EMU_IN = 914400
BUSTIA_VINYETA = "•·▪◦‣"


def _in(v):
    return (v or 0) / EMU_IN


def _rgb_hex(forma):
    try:
        if forma.fill.type == 1:   # MSO_FILL.SOLID
            return str(forma.fill.fore_color.rgb)
    except Exception:  # noqa: BLE001
        pass
    return None


def _es_neutre(h):
    if not h or len(h) != 6:
        return True
    r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
    return max(r, g, b) - min(r, g, b) < 24


def _mida_font(forma):
    """(mida màxima en pt, tot en negreta?)"""
    mida, neg, hi_ha = 0, True, False
    for p in forma.text_frame.paragraphs:
        for r in p.runs:
            if not r.text.strip():
                continue
            hi_ha = True
            mida = max(mida, r.font.size.pt if r.font.size else 0)
            neg = neg and bool(r.font.bold)
    return mida, (neg and hi_ha)


def _text_pla(forma):
    return " ".join(forma.text_frame.text.split())


def _contenidors(formes, ample, alt):
    """Rectangles grans sense text = fons de targeta/destacat."""
    from pptx.enum.shapes import MSO_SHAPE_TYPE
    out = []
    for f in formes:
        if f.shape_type != MSO_SHAPE_TYPE.AUTO_SHAPE:
            continue
        if f.has_text_frame and f.text_frame.text.strip():
            continue
        w, h = _in(f.width), _in(f.height)
        if w < 1.2 or h < 0.35:
            continue
        if (f.width or 0) >= 0.9 * ample and (f.height or 0) >= 0.85 * alt:
            continue   # fons de la diapositiva
        out.append(dict(sh=f, l=_in(f.left), t=_in(f.top), w=w, h=h,
                        textos=[], fills=[], pare=None, color=None))
    return out


def _color_contenidor(c, formes):
    """Color d'accent de la targeta: la línia fina de dalt o de l'esquerra."""
    from pptx.enum.shapes import MSO_SHAPE_TYPE
    for f in formes:
        if f is c["sh"] or f.shape_type != MSO_SHAPE_TYPE.AUTO_SHAPE:
            continue
        w, h, l, t = _in(f.width), _in(f.height), _in(f.left), _in(f.top)
        vora_dalt = h < 0.1 and w > c["w"] * 0.8 and abs(t - c["t"]) < 0.06 and abs(l - c["l"]) < 0.1
        vora_esq = w < 0.1 and h > c["h"] * 0.8 and abs(l - c["l"]) < 0.06 and abs(t - c["t"]) < 0.1
        if vora_dalt or vora_esq:
            hx = _rgb_hex(f)
            if hx and not _es_neutre(hx):
                return "#" + hx
    return None


def _items_text(forma, permet_titol):
    """Paràgrafs d'una caixa de text -> [(top, left, tipus, text)]. tipus: h3 | li | p"""
    out = []
    top, left = _in(forma.top), _in(forma.left)
    mida, neg = _mida_font(forma)
    for i, par in enumerate(forma.text_frame.paragraphs):
        brut = "".join(r.text for r in par.runs).strip()
        if not brut:
            continue
        es_li = brut[0] in BUSTIA_VINYETA or _es_vinyeta(par, forma)[0]
        t = (top + i * 1e-4, left)
        if permet_titol and i == 0 and mida >= 12 and neg and not es_li:
            out.append((t[0], t[1], "h3", _md_text(_text_pla(forma))))
            permet_titol = False
            continue
        md = _paragraf_md(par, treu_vinyeta=es_li)
        if not md:
            continue
        out.append((t[0], t[1], "li" if es_li else "p", md if es_li else _escapa_inici(md)))
    return out


def _uneix_items(items):
    """Uneix [(top,left,tipus,text)] en Markdown: les viñetes seguides formen una llista."""
    blocs, llista = [], []

    def buida():
        nonlocal llista
        if llista:
            blocs.append("\n".join(llista))
            llista = []

    for _, _, tipus, text in items:
        if tipus == "li":
            llista.append("- " + text)
            continue
        buida()
        blocs.append(("### " + text) if tipus == "h3" else text)
    buida()
    return "\n\n".join(b for b in blocs if b.strip())


def _md_contenidor(c, formes):
    es_destacat = c["pare"] is not None or (len(c["textos"]) == 1 and not c["fills"] and c["w"] >= 8.0)
    items = []
    primer = min(c["textos"], key=lambda f: (_in(f.top), _in(f.left))) if c["textos"] else None
    for f in c["textos"]:
        items += _items_text(f, permet_titol=(not es_destacat and f is primer))
    for n in c["fills"]:
        items.append((n["t"], n["l"], "raw_p", _md_contenidor(n, formes)))
    items.sort(key=lambda x: (x[0], x[1]))
    items = [(a, b, "p" if k == "raw_p" else k, t) for a, b, k, t in items]
    cos = _uneix_items(items)
    estil = f' style="--card:{c["color"]}"' if c["color"] else ""
    classe = "md-callout" if es_destacat else "md-card"
    return f'<div class="{classe}"{estil} markdown="1">\n\n{cos}\n\n</div>'


def _bloc_especial(f, num, ctx):
    """Imatge, taula o gràfic -> Markdown (o None si s'ha d'ometre)."""
    from pptx.enum.shapes import MSO_SHAPE_TYPE
    import hashlib as _h
    try:
        if f.shape_type == MSO_SHAPE_TYPE.PICTURE or (f.is_placeholder and hasattr(f, "image")):
            if _in(f.width) < 1.5 and _in(f.height) < 1.5:
                return None   # icona o insígnia decorativa
            if (f.width or 0) >= 0.9 * ctx["ample"] and (f.height or 0) >= 0.9 * ctx["alt"]:
                return None   # imatge de fons
            blob = f.image.blob
            if _h.sha1(blob).hexdigest() in ctx["decoratives"] or not PPTX_IMATGES:
                return None
            nom = _desa_imatge(blob, ctx["img_dir"], ctx["n_img"] + 1)
            if not nom:
                return None
            ctx["n_img"] += 1
            try:
                alt = f._element.xpath(".//p:cNvPr")[0].get("descr") or ""
            except Exception:  # noqa: BLE001
                alt = ""
            alt = re.sub(r"[\[\]\n]", " ", alt).strip()
            if not alt or re.search(r"\.(png|jpe?g|gif|bmp|tiff?|emf|wmf)$", alt, re.I):
                alt = f"Imatge {ctx['n_img']}"
            return f"![{alt}]({TOKEN_IMG}{nom}){{ loading=lazy }}"
        if getattr(f, "has_table", False) and f.has_table:
            return _taula_md(f.table)
        if getattr(f, "has_chart", False) and f.has_chart:
            try:
                return _grafic_md(f.chart)
            except Exception:  # noqa: BLE001
                AVISOS_PPTX.append((ctx["nom"], num, "gràfic no convertible"))
                return None
        if f.shape_type in (MSO_SHAPE_TYPE.MEDIA, MSO_SHAPE_TYPE.EMBEDDED_OLE_OBJECT,
                            MSO_SHAPE_TYPE.LINKED_OLE_OBJECT):
            AVISOS_PPTX.append((ctx["nom"], num, "vídeo/àudio/objecte incrustat"))
        elif getattr(f, "_element", None) is not None and f._element.tag.endswith("graphicFrame"):
            AVISOS_PPTX.append((ctx["nom"], num, "SmartArt o diagrama (no es publica)"))
    except Exception as e:  # noqa: BLE001
        AVISOS_PPTX.append((ctx["nom"], num, f"element omès ({type(e).__name__})"))
    return None


def _slide_layout(sl, formes, ctx, num):
    """Reconstrueix una diapositiva feta de targetes. Retorna None si no en té."""
    from pptx.enum.shapes import MSO_SHAPE_TYPE, PP_PLACEHOLDER
    ample, alt = ctx["ample"], ctx["alt"]
    cont = _contenidors(formes, ample, alt)
    fons = any(f.shape_type == MSO_SHAPE_TYPE.PICTURE and (f.width or 0) >= 0.9 * ample
               and (f.height or 0) >= 0.9 * alt for f in formes)
    if not cont and not fons:
        return None

    def es_peu(f):
        try:
            return f.is_placeholder and f.placeholder_format.type in (
                PP_PLACEHOLDER.SLIDE_NUMBER, PP_PLACEHOLDER.FOOTER, PP_PLACEHOLDER.DATE)
        except Exception:  # noqa: BLE001
            return False

    textos = [f for f in formes if f.has_text_frame and f.text_frame.text.strip() and not es_peu(f)
              and not any(f is c["sh"] for c in cont)]

    def dins(c, x, y):
        return c["l"] <= x <= c["l"] + c["w"] and c["t"] <= y <= c["t"] + c["h"]

    for c in cont:
        cx, cy = c["l"] + c["w"] / 2, c["t"] + c["h"] / 2
        pares = [p for p in cont if p is not c and p["w"] * p["h"] > c["w"] * c["h"] and dins(p, cx, cy)]
        if pares:
            c["pare"] = min(pares, key=lambda p: p["w"] * p["h"])
            c["pare"]["fills"].append(c)
        c["color"] = _color_contenidor(c, formes)

    lliures = []
    for f in textos:
        x, y = _in(f.left) + _in(f.width) / 2, _in(f.top) + _in(f.height) / 2
        cands = [c for c in cont if dins(c, x, y)]
        if cands:
            min(cands, key=lambda c: c["w"] * c["h"])["textos"].append(f)
        else:
            lliures.append(f)

    # Capçalera: etiqueta petita + títol (a dalt, fora de targetes)
    if cont:
        cap = sorted([f for f in lliures if _in(f.top) < 1.4], key=lambda f: _in(f.top))
        resta = [f for f in lliures if f not in cap]
    else:
        cap = sorted(lliures, key=lambda f: _in(f.top))
        resta = []
    kicker = titol = None
    extra = []
    if cap:
        mides = [_mida_font(f)[0] for f in cap]
        i_t = mides.index(max(mides))
        titol = _text_pla(cap[i_t])
        if i_t > 0 and mides[i_t - 1] < mides[i_t]:
            kicker = _text_pla(cap[i_t - 1])
        usades = {i_t, i_t - 1 if (i_t > 0 and mides[i_t - 1] < mides[i_t]) else -99}
        extra = [f for j, f in enumerate(cap) if j not in usades]
    resta += extra

    # Blocs (ordenats per posició)
    elements = []
    tops = sorted([c for c in cont if c["pare"] is None], key=lambda c: (c["t"], c["l"]))
    files, actual = [], []
    for c in tops:
        if actual and abs(c["t"] - actual[0]["t"]) <= 0.3:
            actual.append(c)
        else:
            if actual:
                files.append(actual)
            actual = [c]
    if actual:
        files.append(actual)
    for fila in files:
        fila.sort(key=lambda c: c["l"])
        blocs = [_md_contenidor(c, formes) for c in fila]
        if len(fila) >= 2:
            md = '<div class="md-cards" markdown="1">\n\n' + "\n\n".join(blocs) + "\n\n</div>"
        else:
            md = blocs[0]
        elements.append((fila[0]["t"], fila[0]["l"], "p", md))
    for f in resta:
        for it in _items_text(f, permet_titol=False):
            elements.append(it)
    for f in formes:
        if f.has_text_frame and f.text_frame.text.strip():
            continue
        md = _bloc_especial(f, num, ctx)
        if md:
            elements.append((_in(f.top), _in(f.left), "p", md))
    elements.sort(key=lambda x: (round(x[0] / 0.15), x[1], x[0]))
    return dict(cover=not cont, titol=titol, kicker=kicker, blocs=_uneix_items(elements))


def _pptx_a_markdown(path_pptx, img_dir, titol_fitxer, nom_fitxer):
    from pptx import Presentation
    from pptx.enum.shapes import MSO_SHAPE_TYPE, PP_PLACEHOLDER
    import hashlib as _h

    prs = Presentation(str(path_pptx))
    diapos = list(prs.slides)

    # Imatges que es repeteixen a 3+ diapositives = logos/decoració: s'ometen
    comptes = {}
    for sl in diapos:
        vistes = set()
        for f in _formes(sl.shapes):
            if f.shape_type == MSO_SHAPE_TYPE.PICTURE:
                try:
                    hsh = _h.sha1(f.image.blob).hexdigest()
                except Exception:  # noqa: BLE001
                    continue
                if hsh not in vistes:
                    vistes.add(hsh)
                    comptes[hsh] = comptes.get(hsh, 0) + 1
    decoratives = {h for h, c in comptes.items() if c >= 3 and len(diapos) >= 4}

    ctx = dict(ample=prs.slide_width, alt=prs.slide_height, decoratives=decoratives,
               img_dir=img_dir, n_img=0, nom=nom_fitxer)
    blocs = []
    titol_doc = titol_fitxer
    primera = True

    for num, sl in enumerate(diapos, 1):
        if PPTX_SALTAR_OCULTES and sl._element.get("show") == "0":
            continue
        formes = list(_formes(sl.shapes))

        # 1) Diapositiva feta de targetes/caixes
        try:
            lay = _slide_layout(sl, formes, ctx, num)
        except Exception as e:  # noqa: BLE001
            AVISOS_PPTX.append((nom_fitxer, num, f"disseny no reconegut ({type(e).__name__}); es llegeix en ordre simple"))
            lay = None
        if lay is not None:
            if lay["cover"] and primera and lay["titol"]:
                titol_doc = lay["titol"]
                if lay["kicker"]:
                    blocs.append(f'<p class="md-kicker">{html.escape(lay["kicker"], quote=False)}</p>')
            else:
                blocs.append("## " + _md_text(lay["titol"]) if lay["titol"] else f"## Diapositiva {num}")
                if lay["kicker"]:
                    blocs.append(f'<p class="md-kicker">{html.escape(lay["kicker"], quote=False)}</p>')
            if lay["blocs"]:
                blocs.append(lay["blocs"])
            primera = False
            if PPTX_INCLOURE_NOTES:
                blocs += _notes_md(sl)
            continue

        # 2) Diapositiva "clàssica" (títol i contingut en marcadors)
        titol_sl, forma_titol, es_portada = None, None, False
        try:
            if sl.shapes.title is not None and sl.shapes.title.has_text_frame:
                forma_titol = sl.shapes.title
                titol_sl = " ".join(forma_titol.text_frame.text.split()) or None
                es_portada = forma_titol.placeholder_format.type == PP_PLACEHOLDER.CENTER_TITLE
        except Exception:  # noqa: BLE001
            pass
        if primera and es_portada and titol_sl:
            titol_doc = titol_sl
        elif titol_sl:
            blocs.append("## " + _md_text(titol_sl))
        else:
            blocs.append(f"## Diapositiva {num}")
        primera = False

        resta = [f for f in formes if not (forma_titol is not None and f.shape_id == forma_titol.shape_id)]
        resta.sort(key=lambda f: ((f.top or 0) // 365760, f.left or 0))
        ometre = (PP_PLACEHOLDER.SLIDE_NUMBER, PP_PLACEHOLDER.FOOTER, PP_PLACEHOLDER.DATE)
        for f in resta:
            try:
                if f.is_placeholder and f.placeholder_format.type in ometre:
                    continue
            except Exception:  # noqa: BLE001
                pass
            md = _bloc_especial(f, num, ctx)
            if md:
                blocs.append(md)
                continue
            try:
                if f.has_text_frame and f.text_frame.text.strip():
                    t = _text_forma_md(f)
                    if t:
                        blocs.append(t)
            except Exception as e:  # noqa: BLE001
                AVISOS_PPTX.append((nom_fitxer, num, f"element omès ({type(e).__name__})"))
        if PPTX_INCLOURE_NOTES:
            blocs += _notes_md(sl)

    return f"# {_md_text(titol_doc)}\n\n" + "\n\n".join(b for b in blocs if b.strip()) + "\n"


def _notes_md(sl):
    try:
        if sl.has_notes_slide:
            n = sl.notes_slide.notes_text_frame.text.strip()
            if n:
                cos = "\n".join("    " + _md_text(l) if l.strip() else "" for l in n.splitlines())
                return ['!!! note "Notes del professor"\n' + cos]
    except Exception:  # noqa: BLE001
        pass
    return []


def converteix_pptx(pptx):
    """Retorna (markdown_amb_token, carpeta_imatges_o_None) o None si falla."""
    st = pptx.stat()
    opcions = f"{PPTX_IMATGES}|{PPTX_INCLOURE_NOTES}|{PPTX_SALTAR_OCULTES}|v2"
    clau = "p" + hashlib.sha1(
        f"{pptx.resolve()}|{st.st_size}|{st.st_mtime_ns}|{opcions}".encode()
    ).hexdigest()[:15]
    cdir = CACHE / clau
    cmd, cimg = cdir / "doc.md", cdir / "img"
    if cmd.is_file():
        STATS["cache"] += 1
        return cmd.read_text(encoding="utf-8"), (cimg if cimg.is_dir() else None)

    try:
        import pptx as _p  # noqa: F401
        from PIL import Image  # noqa: F401
    except Exception as e:  # noqa: BLE001
        ordre = f'"{sys.executable}" -m pip install python-pptx pillow'
        if not _AVIS_LLIBRERIA_PPTX:
            _AVIS_LLIBRERIA_PPTX.append(1)
            print(f"\n  AVÍS: no es poden convertir els PPTX ({type(e).__name__}: {e}).\n  Instal·la: {ordre}\n")
        FALLITS.append((norm(pptx.name), f"Falta python-pptx/pillow. Instal·la: {ordre}"))
        return None

    shutil.rmtree(cdir, ignore_errors=True)
    (cdir / "img").mkdir(parents=True, exist_ok=True)
    try:
        md = _pptx_a_markdown(pptx, cdir / "img", norm(pptx.stem), norm(pptx.name))
        text_pla = re.sub(r"!\[[^\]]*\]\([^)]*\)(\{[^}]*\})?|[#\s]+", "", md)
        if len(text_pla) < 5 and not any((cdir / "img").iterdir()):
            raise RuntimeError("la presentació no té contingut convertible")
        try:
            if not any((cdir / "img").iterdir()):
                (cdir / "img").rmdir()
        except OSError:
            pass
        (cdir / "doc.md").write_text(md, encoding="utf-8")
    except Exception as e:  # noqa: BLE001
        FALLITS.append((norm(pptx.name), f"{type(e).__name__}: {e}"))
        shutil.rmtree(cdir, ignore_errors=True)
        return None
    STATS["convertits"] += 1
    print(f"  PPTX convertit: {norm(pptx.name)}")
    return md, (cimg if cimg.is_dir() else None)


def escriu(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def esborra_docs():
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
                    shutil.rmtree(DOCS, onexc=_treu_readonly)
                except TypeError:
                    shutil.rmtree(DOCS, onerror=_treu_readonly)
            return
        except Exception:
            time.sleep(1)
    print("No puc esborrar la carpeta 'docs'. Tanca terminals o exploradors oberts.")
    sys.exit(1)


# ----------------------------------------------------------------------------
# DISSENY CSS INTEGRAL
# ----------------------------------------------------------------------------
CSS = r''':root {
  --bg: #F8FAFC;
  --surface: #FFFFFF;
  --ink: #0F172A;
  --muted: #64748B;
  --border: #E2E8F0;
  --primary: #1E40AF;
  --primary-hover: #1E3A8A;
  --accent: #2563EB;
  --accent-soft: #EFF6FF;
  --accent-border: #BFDBFE;
  --sidebar-w: 290px;
  --topbar-h: 64px;
  --font-display: "Space Grotesk", -apple-system, sans-serif;
  --font-body: "Inter", -apple-system, sans-serif;
  --font-mono: "JetBrains Mono", monospace;
}

* { box-sizing: border-box; margin: 0; padding: 0; }
html { scroll-behavior: smooth; }
body { font-family: var(--font-body); color: var(--ink); background: var(--bg); line-height: 1.6; -webkit-font-smoothing: antialiased; }

/* Barra Superior Fija con Buscador */
.topbar {
  position: fixed; top: 0; left: 0; right: 0; height: var(--topbar-h);
  background: rgba(255, 255, 255, 0.95); backdrop-filter: blur(8px);
  border-bottom: 1px solid var(--border); display: flex; align-items: center;
  justify-content: space-between; padding: 0 1.5rem; z-index: 1000;
  box-shadow: 0 1px 3px rgba(0,0,0,0.03);
}
.topbar-brand { display: flex; align-items: center; gap: 0.75rem; text-decoration: none; color: var(--ink); font-weight: 700; font-family: var(--font-display); font-size: 1.1rem; }
.topbar-brand svg { width: 22px !important; height: 22px !important; flex-shrink: 0; color: var(--accent); }

.search-container { position: relative; width: 320px; }
.search-container input {
  width: 100%; padding: 0.5rem 1rem 0.5rem 2.4rem; border-radius: 999px;
  border: 1px solid var(--border); background: var(--bg); font-size: 0.85rem;
  color: var(--ink); outline: none; transition: all 0.2s ease;
}
.search-container input:focus { border-color: var(--accent); background: #FFF; box-shadow: 0 0 0 3px rgba(37,99,235,0.15); }
.search-container svg { position: absolute; left: 0.85rem; top: 50%; transform: translateY(-50%); width: 16px !important; height: 16px !important; color: var(--muted); }

/* Layout Base */
.wrap { max-width: 1120px; margin: 0 auto; padding: calc(var(--topbar-h) + 2rem) 1.5rem 3rem; }

/* Cabecera Hero con Degradado */
.hero {
  background: linear-gradient(135deg, #1E3A8A 0%, #2563EB 50%, #3B82F6 100%);
  color: #FFF; border-radius: 20px; padding: 3.5rem 2.5rem 3rem;
  box-shadow: 0 10px 30px -10px rgba(30,58,138,0.3); margin-bottom: 2.5rem;
}
.hero .back { display: inline-flex; align-items: center; gap: 0.4rem; color: #93C5FD; font-family: var(--font-mono); font-size: 0.82rem; text-decoration: none; margin-bottom: 1.2rem; transition: color 0.2s; }
.hero .back:hover { color: #FFF; }
.hero .eyebrow { font-family: var(--font-mono); font-size: 0.78rem; text-transform: uppercase; letter-spacing: 0.12em; color: #BFDBFE; display: flex; align-items: center; gap: 0.5rem; }
.hero h1 { font-family: var(--font-display); font-size: clamp(2rem, 4vw, 3rem); font-weight: 700; line-height: 1.15; margin-top: 0.6rem; color: #FFF; }
.hero .lede { color: #E0F2FE; font-size: 1.1rem; max-width: 65ch; margin-top: 1rem; opacity: 0.95; }

/* Grid de Tarjetas */
.section-title { font-family: var(--font-mono); font-size: 0.8rem; letter-spacing: 0.1em; text-transform: uppercase; color: var(--muted); margin: 2rem 0 1rem; }
.grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 1.25rem; }
.card {
  position: relative; background: var(--surface); border: 1px solid var(--border);
  border-radius: 16px; padding: 1.5rem; text-decoration: none; color: inherit;
  display: flex; flex-direction: column; transition: all 0.25s ease;
  overflow: hidden;
}
.card:hover:not(.disabled) { transform: translateY(-4px); border-color: var(--accent-border); box-shadow: 0 12px 30px -10px rgba(37,99,235,0.15); }
.card-top { display: flex; align-items: center; justify-content: space-between; gap: 0.75rem; margin-bottom: 1rem; }
.card-icon { width: 36px !important; height: 36px !important; border-radius: 10px; background: var(--accent-soft); color: var(--primary); display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
.card-icon svg { width: 18px !important; height: 18px !important; stroke: currentColor; fill: none; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
.aea-code { font-family: var(--font-mono); font-weight: 600; font-size: 0.82rem; color: var(--primary); background: var(--accent-soft); padding: 0.3rem 0.65rem; border-radius: 8px; border: 1px solid var(--accent-border); }
.tags .tag { font-family: var(--font-mono); font-size: 0.72rem; padding: 0.25rem 0.55rem; border-radius: 6px; white-space: nowrap; }
.tag.ra { background: #DCFCE7; color: #166534; }
.tag.soon { background: #F1F5F9; color: #64748B; }
.card h2 { font-family: var(--font-display); font-weight: 600; font-size: 1.2rem; line-height: 1.3; margin-bottom: 0.4rem; }
.card p { color: var(--muted); font-size: 0.92rem; flex: 1; }
.open { margin-top: 1.25rem; font-family: var(--font-mono); font-size: 0.82rem; font-weight: 600; color: var(--accent); display: inline-flex; align-items: center; gap: 0.4rem; }
.open .arrow { transition: transform 0.2s ease; }
.card:hover .open .arrow { transform: translateX(4px); }
.card.disabled { opacity: 0.6; cursor: not-allowed; background: #F8FAFC; }

/* Lista de Recursos */
.resource-list { border: 1px solid var(--border); border-radius: 14px; background: var(--surface); overflow: hidden; margin-bottom: 1.5rem; }
.resource { display: flex; align-items: center; gap: 1rem; padding: 1rem 1.2rem; text-decoration: none; color: inherit; border-bottom: 1px solid var(--border); transition: background 0.15s; }
.resource:last-child { border-bottom: none; }
.resource:hover { background: var(--accent-soft); }
.resource-icon { width: 32px !important; height: 32px !important; border-radius: 10px; background: var(--accent-soft); color: var(--accent); display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
.resource-icon svg { width: 16px !important; height: 16px !important; stroke: currentColor; fill: none; stroke-width: 2; }
.resource-body { flex: 1; min-width: 0; display: flex; align-items: center; gap: 0.75rem; flex-wrap: wrap; }
.resource-type { font-family: var(--font-mono); font-size: 0.72rem; color: var(--primary); background: #DBEAFE; padding: 0.2rem 0.5rem; border-radius: 6px; }
.resource-title { font-weight: 500; font-size: 0.95rem; color: var(--ink); }

/* Layout de Apunte con Menú Lateral */
.apunt-layout { display: flex; margin-top: var(--topbar-h); min-height: calc(100vh - var(--topbar-h)); }
.sidebar {
  width: var(--sidebar-w); background: var(--surface); border-right: 1px solid var(--border);
  padding: 2rem 1.25rem; position: fixed; top: var(--topbar-h); bottom: 0; overflow-y: auto;
}
.sidebar-head { font-family: var(--font-mono); font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.1em; color: var(--muted); margin-bottom: 1rem; padding-left: 0.5rem; }
.sidebar-menu { list-style: none; }
.sidebar-menu a {
  display: flex; align-items: center; gap: 0.6rem; padding: 0.65rem 0.75rem; border-radius: 10px;
  text-decoration: none; color: var(--muted); font-size: 0.88rem; font-weight: 500; transition: all 0.15s; margin-bottom: 0.25rem;
}
.sidebar-menu a:hover { background: var(--accent-soft); color: var(--accent); }
.sidebar-menu a.active { background: var(--accent-soft); color: var(--primary); font-weight: 600; border: 1px solid var(--accent-border); }

.apunt-content { margin-left: var(--sidebar-w); flex: 1; padding: 2.5rem 3.5rem 4rem; max-width: 960px; }
.apunt-header { margin-bottom: 2rem; padding-bottom: 1.5rem; border-bottom: 1px solid var(--border); }
.apunt-eyebrow { font-family: var(--font-mono); font-size: 0.78rem; text-transform: uppercase; color: var(--accent); margin-bottom: 0.4rem; }

/* Prosa */
.prose { background: var(--surface); border: 1px solid var(--border); border-radius: 16px; padding: 2.5rem; }
.prose > * + * { margin-top: 1.1rem; }
.prose h1 { font-family: var(--font-display); font-size: 2rem; color: var(--ink); margin-bottom: 0.5rem; }
.prose h2 { font-family: var(--font-display); font-size: 1.4rem; padding-top: 1.5rem; border-top: 1px solid var(--border); margin-top: 2rem; }
.prose h3 { font-family: var(--font-display); font-size: 1.15rem; margin-top: 1.5rem; }
.prose p, .prose li { color: #334155; line-height: 1.65; }
.prose ul, .prose ol { padding-left: 1.4rem; }
.prose a { color: var(--accent); font-weight: 500; }
.prose code { font-family: var(--font-mono); font-size: 0.85em; background: #F1F5F9; color: #0F172A; padding: 0.15em 0.4em; border-radius: 6px; }
.prose pre { background: #0F172A; color: #F8FAFC; border-radius: 12px; padding: 1.25rem; overflow-x:auto; }
.prose pre code { background: none; color: inherit; padding: 0; }
.prose img { max-width: 100%; height: auto; border-radius: 12px; border: 1px solid var(--border); margin: 1.5rem 0; }

/* Botones Anterior / Siguiente */
.pager { display: flex; justify-content: space-between; gap: 1rem; margin-top: 2.5rem; padding-top: 1.5rem; border-top: 1px solid var(--border); }
.pager-btn {
  display: inline-flex; align-items: center; gap: 0.6rem; padding: 0.75rem 1.25rem;
  border-radius: 10px; border: 1px solid var(--border); background: var(--surface);
  text-decoration: none; color: var(--ink); font-weight: 500; font-size: 0.88rem;
  transition: all 0.2s ease;
}
.pager-btn:hover { border-color: var(--accent); color: var(--accent); background: var(--accent-soft); transform: translateY(-1px); }

.empty { background: var(--surface); border: 1px dashed var(--border); border-radius: 16px; padding: 2.5rem; color: var(--muted); text-align: center; }
.empty strong { display: block; font-family: var(--font-display); font-size: 1.15rem; color: var(--ink); margin-bottom: 0.4rem; }
footer { margin-top: 4rem; padding-top: 1.5rem; border-top: 1px solid var(--border); color: var(--muted); font-size: 0.82rem; font-family: var(--font-mono); text-align: center; }

@media (max-width: 768px) {
  .grid { grid-template-columns: 1fr; }
  .apunt-layout { flex-direction: column; }
  .sidebar { position: relative; width: 100%; height: auto; top: 0; border-right: none; border-bottom: 1px solid var(--border); }
  .apunt-content { margin-left: 0; padding: 1.5rem; }
  .search-container { width: 180px; }
}

/* --- Diapositives convertides des de PPTX --- */
.md-kicker { font-family: var(--font-mono); font-weight: 600; font-size: .72rem; letter-spacing: .14em; text-transform: uppercase; color: var(--accent); margin: .1rem 0 1.1rem !important; }
.md-cards { display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 1rem; margin: 1.2rem 0; }
.md-card { --card: var(--accent); background: #F8FAFC; border: 1px solid var(--border); border-top: 3px solid var(--card); border-radius: 12px; padding: 1.1rem 1.25rem 1.15rem; min-width: 0; }
.md-card > :first-child { margin-top: 0 !important; }
.md-card h3 { margin: 0 0 .55rem !important; font-size: 1.05rem; color: var(--card); color: color-mix(in srgb, var(--card) 70%, #0F172A); }
.md-card p { margin: .45rem 0; font-size: .95rem; }
.md-card ul { margin: .45rem 0 .2rem 0; padding-left: 1.15rem; font-size: .93rem; }
.md-card li + li { margin-top: .3rem; }
.md-callout { --card: var(--accent); border-left: 4px solid var(--card); background: var(--accent-soft); background: color-mix(in srgb, var(--card) 8%, #fff); padding: .9rem 1.15rem; border-radius: 0 12px 12px 0; margin: 1.1rem 0; font-weight: 500; }
.md-callout p { margin: 0; }
.md-card .md-callout { margin: .8rem 0 0; font-size: .9rem; }
'''

esc = html.escape
MARCADOR_DIAPOSITIVES = "Material en format diapositives."

ICONES = {
    "diapositives": '<rect x="3" y="4" width="18" height="12" rx="1"/><line x1="8" y1="20" x2="16" y2="20"/><line x1="12" y1="16" x2="12" y2="20"/>',
    "pagina": '<path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><polyline points="14 3 14 8 19 8"/><line x1="9" y1="13" x2="15" y2="13"/><line x1="9" y1="17" x2="15" y2="17"/>',
    "html": '<polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/>',
    "fitxer": '<path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/>',
}
ETIQUETES = {"diapositives": "Diapositives", "pagina": "Pàgina", "html": "Interactiu", "fitxer": "Fitxer"}
ICONES["pdf"] = ICONES["fitxer"]
ETIQUETES["pdf"] = "PDF"
ICONES["drive"] = '<path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/>'
ETIQUETES["drive"] = "Google Drive"
ICONES["enllac"] = '<path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/>'
ETIQUETES["enllac"] = "Enllaç"
TIPUS_DESCARREGA = ("pdf", "fitxer", "drive", "enllac")
PRIORITAT_TIPUS = {"diapositives": 0, "pagina": 0, "html": 1, "pdf": 2, "fitxer": 3, "drive": 4, "enllac": 4}


def llegeix_enllacos(f):
    """Fitxer enllacos.txt: una línia per enllaç ('Títol | https://...' o només l'URL)."""
    out = []
    for linia in f.read_text(encoding="utf-8-sig", errors="replace").splitlines():
        l = linia.strip()
        if not l or l.startswith("#"):
            continue
        if "|" in l:
            titol, url = [x.strip() for x in l.rsplit("|", 1)]
        else:
            titol, url = "", l
        if not re.match(r"^https?://", url, re.I):
            continue
        es_drive = "drive.google.com" in url or "docs.google.com" in url
        if not titol:
            titol = "Carpeta de Google Drive" if "drive.google.com/drive" in url else (
                "Google Drive" if es_drive else urlparse(url).netloc)
        out.append((titol, url, "drive" if es_drive else "enllac"))
    return out
EXT_IMATGE = {".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".ico"}


def natural(s):
    s = sense_accents(norm(s)).lower()
    return [int(t) if t.isdigit() else t for t in re.split(r"(\d+)", s)]


def rel_href(destino, des_de_dir):
    r = os.path.relpath(str(destino), str(des_de_dir)).replace(os.sep, "/")
    return quote(r, safe="/#")


def prefix_de(path):
    prof = len(Path(path).relative_to(DOCS).parts) - 1
    return "../" * prof


def barra_superior(pre=""):
    return f"""
<header class="topbar">
  <a class="topbar-brand" href="{pre}index.html">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 14l9-5-9-5-9 5 9 5z"/><path d="M12 14l6.16-3.422a12.083 12.083 0 01.665 6.479A11.952 11.952 0 0112 20.055a11.952 11.952 0 01-6.824-2.998 12.078 12.078 0 01.665-6.479L12 14z"/></svg>
    <span>Portal Docent</span>
  </a>
  <div class="search-container">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
    <input type="text" id="site-search" placeholder="Cercar material o temari..." onkeyup="filtrarContingut()">
  </div>
</header>
"""


def pagina(path, titol, cos, es_apunt=False, sidebar_html=""):
    pre = prefix_de(path)
    topbar = barra_superior(pre)

    if es_apunt:
        body_content = f"""
{topbar}
<div class="apunt-layout">
  <aside class="sidebar">
    {sidebar_html}
  </aside>
  <main class="apunt-content">
    {cos}
    <footer>{esc(FOOTER)}</footer>
  </main>
</div>
"""
    else:
        body_content = f"""
{topbar}
<div class="wrap">
{cos}
  <footer>{esc(FOOTER)}</footer>
</div>
"""

    return f"""<!DOCTYPE html>
<html lang="ca">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(titol)} · {esc(SITE_NAME)}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{pre}assets/style.css">
</head>
<body>
{body_content}
<script>
function filtrarContingut() {{
  let input = document.getElementById('site-search').value.toLowerCase();
  let items = document.querySelectorAll('.card, .resource');
  items.forEach(item => {{
    let text = item.innerText.toLowerCase();
    item.style.display = text.includes(input) ? '' : 'none';
  }});
}}
</script>
</body>
</html>
"""


def capcalera(eyebrow, h1_html, lede=None, back=None):
    b = f'<a class="back" href="{back[0]}">← {esc(back[1])}</a>\n    ' if back else ""
    l = f'\n    <p class="lede">{esc(lede)}</p>' if lede else ""
    return f"""  <section class="hero">
    {b}<div class="eyebrow">{esc(eyebrow)}</div>
    <h1>{h1_html}</h1>{l}
  </section>
"""


def titol_h1(codi, titol):
    return f'{esc(codi)} <span style="opacity:0.6">—</span> {esc(titol)}'


def targeta(codi, titol, desc, href, tag=None, disabled=False):
    t = f'<span class="tags"><span class="tag {"soon" if disabled else "ra"}">{esc(tag)}</span></span>' if tag else ""
    d = f"<p>{esc(desc)}</p>" if desc else ''
    icona = f"""<div class="card-icon">
        <svg viewBox="0 0 24 24"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg>
      </div>"""
    cont = f"""      <div class="card-top">
        {icona}
        <span class="aea-code">{esc(codi)}</span>
        {t}
      </div>
      <h2>{esc(titol)}</h2>
      {d}"""
    if disabled:
        return f"""    <div class="card disabled" aria-disabled="true">
{cont}
      <span class="open" style="color:var(--muted)">Properament</span>
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


def md_a_html(text):
    try:
        import markdown
    except Exception:
        print(
            "\nFalta la llibreria 'markdown'. Instal·la-la amb:\n"
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


def te_germa_publicable(f):
    """Hi ha una versió millor amb el mateix nom? (.md/.html; i per als PDF, també .pptx)"""
    exts = [".md", ".html", ".htm"]
    if f.suffix.lower() == ".pdf" and CONVERTIR_PPTX:
        exts.append(".pptx")
    for x in f.parent.iterdir():
        if x.suffix.lower() in exts and slug(norm(x.stem)) == slug(norm(f.stem)):
            return True
    return False


def processa_material(fitxers, base, desti, index_path, nom_pagina_tornar, eyebrow):
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

    elements_generats = []
    for f in sorted(fitxers, key=lambda x: natural(str(x.relative_to(base)))):
        rel = f.relative_to(base)
        dirs = [norm(p) for p in rel.parts[:-1]]
        grup = " / ".join(dirs)
        rel_dir = "/".join(dirs)
        out_dir = desti.joinpath(*dirs) if dirs else desti
        ext = f.suffix.lower()
        stem = norm(f.stem)

        if sense_accents(f.name).lower() in ("enllacos.txt", "links.txt"):
            for titol_e, url_e, tipus_e in llegeix_enllacos(f):
                res.append(dict(grup=grup, titol=titol_e, url=url_e, path=None, tipus=tipus_e, nova=True))
            continue

        if ext in EXT_IMATGE:
            out_dir.mkdir(parents=True, exist_ok=True)
            nom = lliure(rel_dir, norm(f.name))
            shutil.copy2(f, out_dir / nom)
            continue

        if ext == ".pdf" and PDF_MODE in ("descarrega", "ambdos"):
            out_dir.mkdir(parents=True, exist_ok=True)
            nom_pdf = lliure(rel_dir, norm(f.name))
            shutil.copy2(f, out_dir / nom_pdf)
            if f.stat().st_size > AVIS_MB_FITXER * 1024 * 1024:
                GRANS.append((norm(f.name), f.stat().st_size // (1024 * 1024)))
            res.append(dict(grup=grup, titol=stem, path=out_dir / nom_pdf, tipus="pdf", nova=True))
            if PDF_MODE == "descarrega":
                continue

        if ext == ".pdf" and CONVERTIR_PDF and PDF_MODE in ("pagina", "ambdos"):
            if te_germa_publicable(f):
                continue
            r = converteix_pdf(f)
            if r is None:
                continue
            md, cimg = r
            nom = lliure(rel_dir, slug(stem, 80) + ".html")
            path = out_dir / nom
            tipus = "diapositives" if MARCADOR_DIAPOSITIVES in md else "pagina"
            elements_generats.append({
                "orig": f, "path": path, "stem": stem, "ext": ext, "md": md, "cimg": cimg,
                "out_dir": out_dir, "nom": nom, "grup": grup, "tipus": tipus, "titol": stem, "nova": False
            })
            res.append(dict(grup=grup, titol=stem, path=path, tipus=tipus, nova=False))
            continue

        if ext == ".pptx" and CONVERTIR_PPTX:
            if te_germa_publicable(f):
                continue
            r = converteix_pptx(f)
            if r is None:
                continue
            md, cimg = r
            titol = titol_md(md, stem)
            nom = lliure(rel_dir, slug(stem, 80) + ".html")
            path = out_dir / nom
            elements_generats.append({
                "orig": f, "path": path, "stem": stem, "ext": ext, "md": md, "cimg": cimg,
                "out_dir": out_dir, "nom": nom, "grup": grup, "tipus": "diapositives", "titol": titol, "nova": False
            })
            res.append(dict(grup=grup, titol=titol, path=path, tipus="diapositives", nova=False))
            continue

        if ext == ".md":
            text = f.read_text(encoding="utf-8-sig", errors="replace")
            titol = titol_md(text, stem)
            text = assegura_h1(text, titol)
            nom = lliure(rel_dir, slug(stem, 80) + ".html")
            path = out_dir / nom
            elements_generats.append({
                "orig": f, "path": path, "stem": stem, "ext": ext, "md": text, "cimg": None,
                "out_dir": out_dir, "nom": nom, "grup": grup, "tipus": "pagina", "titol": titol, "nova": False
            })
            res.append(dict(grup=grup, titol=titol, path=path, tipus="pagina", nova=False))
            continue

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

    res.sort(key=lambda r: (natural(r["grup"]), PRIORITAT_TIPUS.get(r["tipus"], 5), natural(r["titol"])))

    num_elems = len(elements_generats)
    for idx, el in enumerate(elements_generats):
        out_dir = el["out_dir"]
        path = el["path"]
        md = el["md"]

        if el["cimg"] is not None:
            img_nom = Path(el["nom"]).stem + "-img"
            shutil.copytree(el["cimg"], out_dir / img_nom, dirs_exist_ok=True)
            md = md.replace(TOKEN_IMG, quote(img_nom) + "/")

        cos_html, h2 = md_a_html(md)

        menu_items = []
        for r_item in res:
            if r_item["tipus"] in ("pagina", "diapositives", "html"):
                is_active = (r_item["path"] == path)
                active_cls = ' class="active"' if is_active else ''
                menu_items.append(f'<li><a href="{rel_href(r_item["path"], path.parent)}"{active_cls}><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/></svg> {esc(r_item["titol"])}</a></li>')

        sidebar_html = f"""
<div class="sidebar-head">Material del RA</div>
<ul class="sidebar-menu">
  {"".join(menu_items)}
</ul>
"""

        pager_html = '<nav class="pager">'
        if idx > 0:
            ant = elements_generats[idx - 1]
            pager_html += f'<a class="pager-btn" href="{rel_href(ant["path"], path.parent)}">← {esc(ant["titol"])}</a>'
        else:
            pager_html += '<span></span>'

        if idx < num_elems - 1:
            sig = elements_generats[idx + 1]
            pager_html += f'<a class="pager-btn" href="{rel_href(sig["path"], path.parent)}">{esc(sig["titol"])} →</a>'
        pager_html += '</nav>'

        header_apunt = f"""
<div class="apunt-header">
  <a class="back" href="{rel_href(index_path, path.parent)}" style="color:var(--accent); text-decoration:none; font-family:var(--font-mono); font-size:0.8rem;">← {esc(nom_pagina_tornar)}</a>
  <div class="apunt-eyebrow" style="margin-top:0.5rem;">{esc(eyebrow)}</div>
</div>
"""
        full_content = f"""
{header_apunt}
<article class="prose">
  {cos_html}
</article>
{pager_html}
"""
        escriu(path, pagina(path, el["titol"], full_content, es_apunt=True, sidebar_html=sidebar_html))

    return res


def llista_recursos(res, pagina_dir):
    out = []
    grups = []
    for r in res:
        if r["grup"] not in grups:
            grups.append(r["grup"])
    for g in sorted(grups, key=natural):
        if g:
            out.append(f'  <h3 class="section-title">{esc(g)}</h3>')
        del_grup = [r for r in res if r["grup"] == g]
        contingut = [r for r in del_grup if r["tipus"] not in TIPUS_DESCARREGA]
        baixades = [r for r in del_grup if r["tipus"] in TIPUS_DESCARREGA]
        for llista, titol in ((contingut, None), (baixades, "Descàrregues i enllaços" if contingut else None)):
            if not llista:
                continue
            if titol:
                out.append(f'  <h3 class="section-title">{titol}</h3>')
            out.append('  <div class="resource-list">')
            for r in llista:
                href = esc(r["url"], quote=True) if r.get("url") else rel_href(r["path"], pagina_dir)
                out.append(recurs(r["titol"], href, r["tipus"], r["nova"]))
            out.append("  </div>")
    return "\n".join(out) + "\n"


def llegeix_descripcio(carpeta):
    for x in carpeta.iterdir():
        if x.is_file() and sense_accents(x.name).lower() == "descripcio.txt":
            return " ".join(x.read_text(encoding="utf-8-sig", errors="replace").split())
    return ""


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

    h_index = DOCS / "index.html"
    cos = capcalera(SITE_EYEBROW, esc(SITE_NAME), SITE_LEDE) + '  <main class="grid">\n'
    for cicle, c_nom, c_index, moduls in cicles_info:
        n_ok = sum(1 for m in moduls if m["ok"])
        tag = f"{n_ok} mòdul{'s' if n_ok != 1 else ''}" if n_ok else "Properament"
        cos += targeta(cicle, c_nom, "", rel_href(c_index, DOCS), tag=tag, disabled=not n_ok)
    cos += "  </main>\n"
    escriu(h_index, pagina(h_index, SITE_NAME, cos))

    print("\nWeb generada amb èxit! Els fitxers .ini (com desktop.ini) s'han ignorat.")
    if STATS["convertits"] or STATS["cache"]:
        print(f"Presentacions/PDF convertits ara: {STATS['convertits']} · reutilitzats de la memòria cau: {STATS['cache']}")
    if FALLITS:
        print("\nNO convertits (no apareixen a la web):")
        for n, e in FALLITS:
            print(f"  - {n}: {e}")
    if AVISOS_PPTX:
        print("\nElements de PPTX que no s'han pogut convertir (revisa'ls):")
        for n, d, e in AVISOS_PPTX:
            print(f"  - {n}, diapositiva {d}: {e}")


if __name__ == "__main__":
    main()