"""Genera, en temps de compilació, les pàgines de la web a partir de les carpetes.

- Cada carpeta amb PDF (directament o en subcarpetes) rep una pàgina index.md
  si no n'ha escrit cap l'autora a mà.
- Si la carpeta té subcarpetes amb contingut, la pàgina les llista com a targetes.
- Si la carpeta té PDF propis, la pàgina els mostra amb descàrrega i visor.
- Una carpeta anomenada "teoria" amb PDF es fusiona amb la carpeta pare:
  l'alumne veu directament els PDF dins del RA o del mòdul, sense un nivell extra.

Els títols es llegeixen del fitxer .pages de cada carpeta (clau `title`).
"""
from pathlib import Path
import re

import mkdocs_gen_files
import yaml

DOCS = Path("docs")


def bonic(nom: str) -> str:
    nom = re.sub(r"[-_]+", " ", nom).strip()
    return nom[:1].upper() + nom[1:]


def titol(carpeta: Path) -> str:
    pages = carpeta / ".pages"
    if pages.exists():
        try:
            t = (yaml.safe_load(pages.read_text(encoding="utf-8")) or {}).get("title")
            if t:
                return str(t)
        except yaml.YAMLError:
            pass
    return bonic(carpeta.name)


def pdfs_de(carpeta: Path):
    return sorted(carpeta.glob("*.pdf"))


def te_contingut(carpeta: Path) -> bool:
    return next(carpeta.rglob("*.pdf"), None) is not None


def subcarpetes(carpeta: Path):
    return sorted(c for c in carpeta.iterdir() if c.is_dir() and te_contingut(c))


def es_teoria_fusionada(carpeta: Path) -> bool:
    """Carpeta 'teoria' amb PDF directes, sense subcarpetes amb contingut,
    i el pare no té un index.md escrit a mà."""
    return (
        carpeta.name.lower() == "teoria"
        and carpeta.parent != DOCS
        and bool(pdfs_de(carpeta))
        and not subcarpetes(carpeta)
        and not (carpeta.parent / "index.md").exists()
    )


def escriu_pdfs(f, pdfs, prefix=""):
    for pdf in pdfs:
        f.write(f"## {bonic(pdf.stem)}\n\n")
        f.write(f"[:material-download: Descarrega el PDF]({prefix}{pdf.name}){{ .md-button }}\n\n")
        f.write(
            f'<iframe src="{prefix}{pdf.name}" width="100%" height="700" '
            f'style="border:1px solid var(--md-default-fg-color--lightest)"></iframe>\n\n'
        )


for carpeta in sorted(p for p in DOCS.rglob("*") if p.is_dir()):
    if not te_contingut(carpeta):
        continue
    if (carpeta / "index.md").exists() or es_teoria_fusionada(carpeta):
        continue

    fills = subcarpetes(carpeta)
    fusionades = [c for c in fills if es_teoria_fusionada(c)]
    fills = [c for c in fills if c not in fusionades]

    ruta = carpeta.relative_to(DOCS) / "index.md"
    with mkdocs_gen_files.open(ruta, "w") as f:
        f.write(f"# {titol(carpeta)}\n\n")

        if fills:
            f.write('<div class="grid cards" markdown>\n\n')
            for c in fills:
                f.write(f"-   [:material-folder-open: **{titol(c)}**]({c.name}/index.md)\n\n")
            f.write("</div>\n\n")

        escriu_pdfs(f, pdfs_de(carpeta))
        for c in fusionades:
            escriu_pdfs(f, pdfs_de(c), prefix=f"{c.name}/")
