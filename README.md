# Material docent

Web amb MkDocs Material, publicada amb GitHub Pages.

## Com funciona
El material el tens en carpetes al teu ordinador (CICLE → 0000 Mòdul → RAx → Teoria).
El script `generar.py` llegeix aquestes carpetes i crea la web:

- `docs/` (les pàgines i els fitxers de teoria) i `mkdocs.yml` (el menú).
- Només es publica el contingut de les carpetes **Teoria**.
- Mai es publiquen les carpetes Gestio, Gestions, Ordenar, .git, examen i exercicis
  (es pot canviar a la llista `EXCLOURE` de `generar.py`).
- Si una teoria és buida, la pàgina diu "Material properament".

## Cada vegada que actualitzis material
1. Posa els fitxers a la carpeta `Teoria` de l'RA corresponent (al teu PC).
2. Executa:

       python generar.py "C:\ruta\a\la\carpeta\de\material"

3. Mira-ho en local (opcional): `mkdocs serve`
4. Puja els canvis a GitHub (`git add .`, `git commit -m "..."`, `git push`).
   La web s'actualitza sola en un parell de minuts.

Si dins de `Teoria` hi poses un `index.md`, serà la pàgina d'aquell RA
(així pots escriure el contingut directament en Markdown).

## Requisits
    pip install mkdocs-material
