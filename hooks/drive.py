"""Hook de MkDocs: afegeix un botó "Descarrega el PDF complet" (enllaç a Google Drive)
a les pàgines que tinguin la clau `pdf:` al seu front matter.

Si `pdf` està buit o no existeix, no es mostra cap botó.
"""
import re

BOTO = "[:material-google-drive: Descarrega el PDF complet]({url}){{ .md-button .md-button--primary target=_blank rel=noopener }}"


def on_page_markdown(markdown, page, config, files):
    url = str(page.meta.get("pdf") or "").strip()
    if not url:
        return markdown
    boto = BOTO.format(url=url)
    # Just sota el primer títol (# ...)
    nou, n = re.subn(r"^(# .+)$", lambda m: f"{m.group(1)}\n\n{boto}", markdown, count=1, flags=re.M)
    return nou if n else f"{boto}\n\n{markdown}"
