#!/usr/bin/env python3
"""
Genera la web (carpeta docs/ + mkdocs.yml) a partir de la carpeta de material
que tens al teu ordinador.

Estructura que espera la carpeta d'origen:

    CICLE (ASIX, DAM, DAW, SMIX)
      └── 0378 Nom del mòdul
            ├── RA1 - Nom del resultat d'aprenentatge
            │     └── Teoria        ← només aquesta carpeta es publica
            └── RA2 - ...

Ús:
    python generar.py "C:\\ruta\\a\\la\\carpeta\\de\\material"

Si una carpeta de teoria és buida (o no existeix), a la web apareix
"Material properament". Quan hi posis fitxers i tornis a executar el
script, apareixen sols. Si dins de teoria hi poses un index.md, aquest
serà la pàgina de l'RA (així pots escriure en Markdown).
"""
import hashlib
import json
import os
import re
import shutil
import stat
import time
import sys
import unicodedata
from pathlib import Path

# ----------------------------------------------------------------------------
# CONFIGURACIÓ (edita aquí el que necessitis)
# ----------------------------------------------------------------------------
SITE_NAME = "Material docent"

# Carpetes que MAI es publiquen (en qualsevol nivell; no distingeix
# majúscules ni accents).
EXCLOURE = {"gestio", "gestions", "ordenar", ".git", "examen", "exercicis"}

# Cicles: carpeta -> nom complet. L'ordre és el del menú.
CICLES = {
    "ASIX": "Administració de Sistemes Informàtics en Xarxa",
    "DAM": "Desenvolupament d'Aplicacions Multiplataforma",
    "DAW": "Desenvolupament d'Aplicacions Web",
    "SMIX": "Sistemes Microinformàtics i Xarxes",
}

# Els PDF NO es pugen a GitHub: es converteixen a Markdown (text + imatges).
CONVERTIR_PDF = True
# Extreure les imatges dels PDF (ocupen espai; posa False per només text).
IMATGES_PDF = True
# Si un PDF no té text (diapositives exportades com a imatge, escanejats...),
# es publica pàgina a pàgina com a imatges lleugeres en lloc de descartar-lo.
PDF_SENSE_TEXT_COM_IMATGES = True
AMPLADA_PAGINA_PX = 1400   # amplada de cada pàgina-imatge
QUALITAT_JPG = 80

# Mida màxima (en MB) dels fitxers NO-PDF que es copien tal qual; avisa si en passa.
AVIS_MB_FITXER = 20
# Avisa si la web (carpeta docs) passa d'aquesta mida total (MB).
AVIS_MB_TOTAL = 300

PROPERAMENT = (
    '!!! info "Material properament"\n'
    "    El material d'aquest apartat estarà disponible aviat.\n"
)

ROOT = Path(__file__).resolve().parent
DOCS = ROOT / "docs"


# ----------------------------------------------------------------------------
# Utilitats
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


def copia_fitxers(fitxers, origen_base, desti_dir):
    """Copia fitxers a desti_dir amb noms 'nets' per a URL. Els PDF es
    converteixen a .md (no es copien).
    Retorna llista de (carpeta_relativa, nom_original, nom_nou)."""
    usats = set()
    res = []
    for f in fitxers:
        rel = f.relative_to(origen_base)
        parts = [slug(norm(p)) for p in rel.parts[:-1]]
        stem, ext = f.stem, f.suffix.lower()
        es_pdf = CONVERTIR_PDF and ext == ".pdf"
        if es_pdf and any(
            x.suffix.lower() == ".md" and norm(x.stem) == norm(f.stem)
            for x in f.parent.iterdir()
        ):
            continue  # ja hi ha la versió en Markdown: tindrà prioritat
        if es_pdf:
            ext = ".md"
        nou = slug(norm(stem), 80) + ext
        rel_dest = Path(*parts) / nou if parts else Path(nou)
        k = 2
        while str(rel_dest) in usats:
            rel_dest = rel_dest.with_name(slug(norm(stem), 80) + f"-{k}" + ext)
            k += 1
        dest = desti_dir / rel_dest

        if es_pdf:
            r = converteix_pdf(f)
            if r is None:
                continue
            md, cimg = r
            usats.add(str(rel_dest))
            img_nom = rel_dest.stem + "-img"
            if cimg is not None:
                shutil.copytree(cimg, dest.parent / img_nom, dirs_exist_ok=True)
            md = md.replace(TOKEN_IMG, img_nom + "/")
            if not re.match(r"\s*#\s", md):
                md = f"# {norm(stem)}\n\n" + md
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text(md, encoding="utf-8")
            nom_vist = norm(stem)
        else:
            usats.add(str(rel_dest))
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(f, dest)
            nom_vist = norm(f.name)
            if f.stat().st_size > AVIS_MB_FITXER * 1024 * 1024:
                GRANS.append((norm(f.name), f.stat().st_size // (1024 * 1024)))
        carpeta_rel = " / ".join(norm(p) for p in rel.parts[:-1])
        res.append((carpeta_rel, nom_vist, rel_dest.as_posix()))
    return res


def llista_fitxers_md(copiats):
    """Genera llistat Markdown de fitxers, agrupat per subcarpeta."""
    out = []
    grups = {}
    for carpeta, orig, nou in copiats:
        grups.setdefault(carpeta, []).append((orig, nou))
    for carpeta in sorted(grups):
        if carpeta:
            out.append(f"\n**{carpeta}**\n")
        for orig, nou in grups[carpeta]:
            out.append(f"- [{orig}]({nou})")
    return "\n".join(out) + "\n"


def escriu(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


# ----------------------------------------------------------------------------
# Construcció del contingut
# ----------------------------------------------------------------------------
def processa_ra(ra_dir, desti, titol):
    """Genera la pàgina d'un RA. Retorna True si té contingut."""
    teoria = troba_teoria(ra_dir) if ra_dir else None
    fitxers = fitxers_teoria(teoria)
    desti.mkdir(parents=True, exist_ok=True)

    if not fitxers:
        escriu(desti / "index.md", f"# {titol}\n\n{PROPERAMENT}")
        return False

    copiats = copia_fitxers(fitxers, teoria, desti)
    if not copiats:
        escriu(desti / "index.md", f"# {titol}\n\n{PROPERAMENT}")
        return False
    ja_hi_ha_index = any(nou == "index.md" for _, _, nou in copiats)
    if not ja_hi_ha_index:
        llistat = llista_fitxers_md(copiats)
        escriu(desti / "index.md", f"# {titol}\n\n## Teoria\n{llistat}")
    return True


def processa_modul(mod_dir, desti, codi, nom):
    """Genera un mòdul. Retorna (titol, nav_items, te_contingut)."""
    titol = f"{codi} {nom}"
    teoria_mod = troba_teoria(mod_dir)

    # RAs: carpetes RAx dins del mòdul, o dins de la teoria del mòdul
    ras = [d for d in subcarpetes(mod_dir) if re.match(r"(?i)^ra\s*\d+", d.name)]
    if teoria_mod:
        ras += [
            d for d in subcarpetes(teoria_mod) if re.match(r"(?i)^ra\s*\d+", d.name)
        ]

    # Fitxers de teoria a nivell de mòdul (fora de les carpetes RA)
    fitxers_mod = [
        f
        for f in fitxers_teoria(teoria_mod)
        if not re.match(r"(?i)^ra\s*\d+", f.relative_to(teoria_mod).parts[0])
        or len(f.relative_to(teoria_mod).parts) == 1
    ]

    nav = []
    files_ra = []
    te_contingut = False
    usats = set()
    for ra in ras:
        m = re.match(r"(?i)^ra\s*(\d+)", ra.name)
        s = f"ra{int(m.group(1))}"
        while s in usats:
            s += "b"
        usats.add(s)
        ra_titol = norm(ra.name).strip()
        # Teoria de l'RA: subcarpeta "teoria" si existeix; si no, la mateixa carpeta
        base = ra if troba_teoria(ra) else None
        if base is None and teoria_mod and ra.parent == teoria_mod:
            # RA dins de teoria del mòdul: tot el contingut és teoria
            tmp = ra
            fit = fitxers_teoria(tmp)
            (desti / s).mkdir(parents=True, exist_ok=True)
            if fit:
                cop = copia_fitxers(fit, tmp, desti / s)
                escriu(
                    desti / s / "index.md",
                    f"# {ra_titol}\n\n## Teoria\n{llista_fitxers_md(cop)}",
                )
                ok = True
            else:
                escriu(desti / s / "index.md", f"# {ra_titol}\n\n{PROPERAMENT}")
                ok = False
        else:
            ok = processa_ra(ra, desti / s, ra_titol)
        files_ra.append((s, ra_titol, ok))
        te_contingut = te_contingut or ok
        nav.append((ra_titol, f"{s}/index.md"))

    # Pàgina del mòdul
    cos = [f"# {titol}\n"]
    if fitxers_mod:
        cop = copia_fitxers(fitxers_mod, teoria_mod, desti)
        cos.append("## Teoria\n" + llista_fitxers_md(cop))
        te_contingut = True
    if files_ra:
        cos.append("## Resultats d'aprenentatge\n")
        cos.append("| RA | Estat |\n|----|-------|")
        for s, t, ok in files_ra:
            estat = "✅ Disponible" if ok else "🚧 Properament"
            cos.append(f"| [{t}]({s}/index.md) | {estat} |")
        cos.append("")
    if not files_ra and not fitxers_mod:
        cos.append(PROPERAMENT)
    escriu(desti / "index.md", "\n".join(cos) + "\n")
    return titol, nav, te_contingut


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

    nav_cicles = []
    ignorades = []
    resum = []

    for cicle, nom_complet in CICLES.items():
        c_dir = next(
            (d for d in origen.iterdir() if d.is_dir() and d.name.upper() == cicle),
            None,
        )
        c_slug = cicle.lower()
        (DOCS / c_slug).mkdir(parents=True, exist_ok=True)
        moduls = []
        if c_dir:
            for m in subcarpetes(c_dir):
                mm = re.match(r"^(\d{4})\s+(.+)$", norm(m.name).strip())
                if not mm:
                    ignorades.append(f"{cicle}/{norm(m.name)}")
                    continue
                moduls.append((m, mm.group(1), mm.group(2)))

        nav_mods = []
        files = []
        for m, codi, nom in moduls:
            ms = f"{codi}-{slug(nom, 40)}"
            titol, nav, ok = processa_modul(m, DOCS / c_slug / ms, codi, nom)
            files.append((titol, f"{ms}/index.md", ok))
            nav_mods.append((titol, ms, nav))
            resum.append((cicle, titol, ok))

        cos = [f"# {cicle}\n", f"{nom_complet}.\n"]
        if files:
            cos.append("| Mòdul | Estat |\n|-------|-------|")
            for t, link, ok in files:
                cos.append(
                    f"| [{t}]({link}) | {'✅ Disponible' if ok else '🚧 Properament'} |"
                )
            cos.append("")
        else:
            cos.append(PROPERAMENT)
        escriu(DOCS / c_slug / "index.md", "\n".join(cos) + "\n")
        nav_cicles.append((cicle, c_slug, nav_mods))

    # Portada
    targetes = "\n".join(
        f"- **[{c}]({c.lower()}/index.md)**\n\n    {n}\n" for c, n in CICLES.items()
    )
    escriu(
        DOCS / "index.md",
        f"# {SITE_NAME}\n\n"
        "Benvinguts! Aquí trobareu el material dels mòduls que imparteixo "
        "als cicles formatius d'informàtica.\n\n"
        f'<div class="grid cards" markdown>\n\n{targetes}\n</div>\n',
    )

    # mkdocs.yml
    q = lambda s: json.dumps(s, ensure_ascii=False)
    y = [
        f"site_name: {q(SITE_NAME)}",
        'site_description: "Material de mòduls d\'ASIX, DAM, DAW i SMIX"',
        "theme:",
        "  name: material",
        "  language: ca",
        "  features:",
        "    - navigation.tabs",
        "    - navigation.indexes",
        "    - navigation.top",
        "    - content.code.copy",
        "    - search.highlight",
        "markdown_extensions:",
        "  - admonition",
        "  - attr_list",
        "  - md_in_html",
        "  - tables",
        "  - toc:",
        "      permalink: true",
        "nav:",
        "  - Inici: index.md",
    ]
    for cicle, c_slug, mods in nav_cicles:
        y.append(f"  - {q(cicle)}:")
        y.append(f"      - {c_slug}/index.md")
        for titol, ms, nav in mods:
            y.append(f"      - {q(titol)}:")
            y.append(f"          - {c_slug}/{ms}/index.md")
            for t, p in nav:
                y.append(f"          - {q(t)}: {c_slug}/{ms}/{p}")
    escriu(ROOT / "mkdocs.yml", "\n".join(y) + "\n")

    # Resum per pantalla
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
    print("\nSegüent pas: mkdocs serve   (per veure-la) o fes commit i push.")


if __name__ == "__main__":
    main()