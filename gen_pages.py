"""Genera, en temps de compilació, la pàgina index.md de cada carpeta que tingui
contingut (pàgines .md) i no tingui un index.md escrit a mà.

La pàgina mostra una targeta per cada subcarpeta amb contingut i per cada pàgina .md.
Una carpeta anomenada "teoria" es fusiona amb la carpeta pare: les seves pàgines
apareixen directament dins del RA o del mòdul (al menú ho fa el fitxer .pages amb
`collapse: true`; aquí, llistant-les a la pàgina del pare).

Els títols de les carpetes es llegeixen del fitxer .pages (clau `title`); els de les
pàgines, del `title` o del primer encapçalament `# ...`. Una `description:` al
front matter d'una pàgina es mostra a la seva targeta.
"""
from pathlib import Path
import re

import mkdocs_gen_files
import yaml

DOCS = Path("docs")
FM = re.compile(r"\A---\s*\n(.*?)\n---\s*\n?", re.S)


def bonic(nom: str) -> str:
    nom = re.sub(r"^\d+[-_ ]+", "", nom)
    nom = re.sub(r"[-_]+", " ", nom).strip()
    return nom[:1].upper() + nom[1:]


def llegeix_pages(carpeta: Path) -> dict:
    fitxer = carpeta / ".pages"
    if fitxer.exists():
        try:
            return yaml.safe_load(fitxer.read_text(encoding="utf-8")) or {}
        except yaml.YAMLError:
            pass
    return {}


def titol_carpeta(carpeta: Path) -> str:
    return str(llegeix_pages(carpeta).get("title") or bonic(carpeta.name))


def meta_pagina(md: Path):
    """(títol, descripció) d'una pàgina .md"""
    text = md.read_text(encoding="utf-8")
    meta = {}
    m = FM.match(text)
    if m:
        try:
            meta = yaml.safe_load(m.group(1)) or {}
        except yaml.YAMLError:
            meta = {}
        text = text[m.end():]
    titol = meta.get("title")
    if not titol:
        h1 = re.search(r"^# (.+)$", text, re.M)
        titol = h1.group(1).strip() if h1 else bonic(md.stem)
    return str(titol), str(meta.get("description") or "")


def pagines(carpeta: Path):
    return sorted(p for p in carpeta.glob("*.md") if p.name != "index.md")


def te_contingut(carpeta: Path) -> bool:
    return next(carpeta.rglob("*.md"), None) is not None


def es_teoria(carpeta: Path) -> bool:
    return carpeta.name.lower() == "teoria" and carpeta.parent != DOCS


def subcarpetes(carpeta: Path):
    return sorted(c for c in carpeta.iterdir() if c.is_dir() and te_contingut(c))


def targeta(icona, titol, enllac, descripcio=""):
    t = f"-   [:material-{icona}: **{titol}**]({enllac})\n\n"
    if descripcio:
        t += f"    {descripcio}\n\n"
    return t


for carpeta in sorted(p for p in DOCS.rglob("*") if p.is_dir()):
    if not te_contingut(carpeta) or es_teoria(carpeta) or (carpeta / "index.md").exists():
        continue

    targetes = []
    for c in subcarpetes(carpeta):
        if es_teoria(c):
            for md in pagines(c):
                t, d = meta_pagina(md)
                targetes.append(targeta("file-document-outline", t, f"{c.name}/{md.name}", d))
            for s in subcarpetes(c):
                targetes.append(targeta("folder-open", titol_carpeta(s), f"{c.name}/{s.name}/index.md"))
        else:
            targetes.append(targeta("folder-open", titol_carpeta(c), f"{c.name}/index.md"))
    for md in pagines(carpeta):
        t, d = meta_pagina(md)
        targetes.append(targeta("file-document-outline", t, md.name, d))

    ruta = carpeta.relative_to(DOCS) / "index.md"
    with mkdocs_gen_files.open(ruta, "w") as f:
        f.write(f"# {titol_carpeta(carpeta)}\n\n")
        f.write('<div class="grid cards" markdown>\n\n')
        f.writelines(targetes)
        f.write("</div>\n")
