---
description: Permisos a Linux. Grups i tipus de permisos, lectura amb ls -l, notació simbòlica i notació numèrica (octal) amb chmod.
# Enllaç de Google Drive per descarregar el PDF complet (si el deixes buit, el botó no es mostra):
pdf: ""
---

# Seguretat lògica a Linux

## Grups de permisos

Quan es crea un fitxer o directori, els permisos s'atribueixen automàticament i es divideixen en tres grups:

| Lletra | Grup | Qui és |
|:-:|---|---|
| **u** | Usuari propietari | L'usuari que va crear el fitxer. |
| **g** | Grup propietari | El grup que és propietari del fitxer. |
| **o** | Altres usuaris | La resta d'usuaris que no pertanyen al grup propietari. |
| **a** | Tots | Tots els usuaris (u + g + o). |

## Tipus de permisos

| Permís | Lletra | Què permet |
|---|:-:|---|
| **Lectura** (*read*) | `r` | Veure el contingut d'un fitxer o directori. |
| **Escriptura** (*write*) | `w` | Alterar el contingut. |
| **Execució** (*execute*) | `x` | Converteix el fitxer en executable o permet accedir a un directori (per utilitzar ordres com `cd`). |

## Notació simbòlica

### Visualització amb `ls -l`

Per veure els permisos d'un fitxer o directori es fa servir l'ordre `ls -l` (llista llarga). La primera columna, de 10 caràcters, es llegeix així:

| Caràcter | Significat |
|:-:|---|
| 1 | Tipus: fitxer (`-`), directori (`d`) o enllaç simbòlic (`l`). |
| 2–4 | Permisos de l'**usuari propietari** (u). |
| 5–7 | Permisos del **grup propietari** (g). |
| 8–10 | Permisos dels **altres usuaris** (o). |

La lletra del permís (`r`, `w`, `x`) es mostra si s'atribueix, i un guió (`-`) si no.

Exemple:

```console
yuri@yuri-laptop:/var/www/html$ ls -l
total 8
-rw-rw-r-- 1 yuri yuri   17 Out  5 17:45 info.php
drwx------ 5 yuri yuri 4096 Fev 15  2017 loja
yuri@yuri-laptop:/var/www/html$
```

### Exemples amb `chmod`

- `chmod g+w fitxer` — **afegir:** dona permís d'escriptura (`w`) al grup (`g`), sense tocar els altres permisos.
- `chmod o-r fitxer` — **treure:** treu el permís de lectura (`r`) als altres (`o`).
- `chmod u=rwx fitxer` — **establir:** estableix els permisos del propietari (`u`) exactament a `rwx`, esborrant qualsevol altre permís anterior.

## Notació numèrica (octal)

La notació numèrica és la més directa i s'utilitza per establir el conjunt complet de permisos d'una sola vegada. Es basa en assignar un valor a cada permís dins d'un grup:

| Permís | Lletra | Valor | Què permet |
|---|:-:|:-:|---|
| Lectura | `r` | **4** | Veure el contingut del fitxer o llistar el directori. |
| Escriptura | `w` | **2** | Modificar o eliminar el fitxer, o crear/esborrar fitxers al directori. |
| Execució | `x` | **1** | Executar el fitxer o entrar al directori. |
| Cap | `-` | **0** | No hi ha permisos. |

### Drets d'accés: octal, binari i permís

| Octal | Binari | Permís |
|:-:|:-:|:-:|
| 0 | 000 | `---` |
| 1 | 001 | `--x` |
| 2 | 010 | `-w-` |
| 3 | 011 | `-wx` |
| 4 | 100 | `r--` |
| 5 | 101 | `r-x` |
| 6 | 110 | `rw-` |
| 7 | 111 | `rwx` |

### Exemple 1

Propietari (*Owner*), grup (*Group*) i altres (*Other*):

| | Owner | Group | Other |
|---|:-:|:-:|:-:|
| Permisos | `rwx` | `r-x` | `r-x` |
| Càlcul | 4+2+1 | 4+0+1 | 4+0+1 |
| **Resultat** | **7** | **5** | **5** |

Per tant: `chmod 755 fitxer`

### Exemple 2

```console
yuri@yuri-laptop:/var/www/html$ ls -l
total 8
-rw-rw-r-- 1 yuri yuri   17 Out  5 17:45 info.php
```

Si mirem l'exemple anterior amb la notació numèrica, `-rw-rw-r--` (propietari `rw-` = 6, grup `rw-` = 6, altres `r--` = 4) seria:

```bash
chmod 664 info.php
```
