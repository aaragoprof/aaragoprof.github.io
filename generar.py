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


def copia_fitxers(fitxers, origen_base, desti_dir):
    """Copia fitxers a desti_dir amb noms 'nets' per a URL.
    Retorna llista de (carpeta_relativa, nom_original, nom_nou)."""
    usats = set()
    res = []
    for f in fitxers:
        rel = f.relative_to(origen_base)
        parts = [slug(norm(p)) for p in rel.parts[:-1]]
        stem, ext = f.stem, f.suffix.lower()
        nou = slug(norm(stem), 80) + ext
        rel_dest = Path(*parts) / nou if parts else Path(nou)
        k = 2
        while str(rel_dest) in usats:
            rel_dest = rel_dest.with_name(slug(norm(stem), 80) + f"-{k}" + ext)
            k += 1
        usats.add(str(rel_dest))
        dest = desti_dir / rel_dest
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(f, dest)
        carpeta_rel = " / ".join(norm(p) for p in rel.parts[:-1])
        res.append((carpeta_rel, norm(f.name), rel_dest.as_posix()))
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
    print("\nSegüent pas: mkdocs serve   (per veure-la) o fes commit i push.")


if __name__ == "__main__":
    main()