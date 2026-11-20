# Seguretat Lògica en Linux

<p class="md-kicker">MÒDUL D'ADMINISTRACIÓ DE SISTEMES OPERATIUS</p>

Material d'estudi: Grups de Permisos, Notació Simbòlica i Numèrica Octal, Comanda chmod i Llistes ACL Avançades

## Els 3 Grups de Permisos (u, g, o, a)

<p class="md-kicker">ESTRUCTURA D'ACCÉS</p>

En crear qualsevol fitxer o directori en GNU/Linux, el sistema operatiu divideix la gestió dels drets d'accés en **tres categories principals d'usuaris**:

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### Usuari Propietari (u)

L'usuari concret (User) que ha creat el fitxer o a qui se li ha assignat la propietat individual.

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### Grup Propietari (g)

El grup d'usuaris (Group) assignat al fitxer. Tots els membres d'aquest grup comparteixen els mateixos drets.

</div>

<div class="md-card" style="--card:#8B5CF6" markdown="1">

### Altres Usuaris (o)

La resta d'usuaris del sistema (Others) que no són ni el propietari ni pertanyen al grup assignat.

</div>

</div>

<div class="md-callout" style="--card:#16A34A" markdown="1">

**\* Comodí All (a): Representa la totalitat dels usuaris de manera simultània (Equivalent a u + g + o).**

</div>

## Tipus de Permisos: Lectura, Escriptura i Execució

<p class="md-kicker">DRETS D'ACCÉS</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### Lectura (r - Read)

- **Fitxers:** Permet obrir i veure el contingut intern del fitxer (ex: cat, nano).
- **Directoris:** Permet llistar el contingut dels arxius que inclou el directori (ex: ls).

</div>

<div class="md-card" style="--card:#F59E0B" markdown="1">

### Escriptura (w - Write)

- **Fitxers:** Permet modificar, afegir o alterar el contingut del fitxer.
- **Directoris:** Permet crear nous fitxers o eliminar fitxers existents a l'interior de la carpeta.

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### Execució (x - Execute)

- **Fitxers:** Converteix el fitxer en un programa executable o script (ex: ./script.sh).
- **Directoris:** Permet entrar o accedir al directori (ex: cd carpeta/).

</div>

</div>

## Interpretació de la Notació Simbòlica (ls -l)

<p class="md-kicker">VISUALITZACIÓ EN TERMINAL</p>

En executar la comanda ls -l, la primera columna consta de **10 caràcters** que es llegeixen d'esquerra a dreta:

<div class="md-callout" markdown="1">

drwxr-xr-- 5 yuri yuri 4096 Feb 15 10:30 directori\_web 
 -rw-rw-r-- 1 yuri yuri 824 Oct 17 11:15 fitxer.txt

</div>

<div class="md-cards" markdown="1">

<div class="md-card" markdown="1">

**Caràcter 1 (Tipus)**

\- Fitxer normal 
 d Directori 
 l Enllaç simbòlic

</div>

<div class="md-card" markdown="1">

**Caràcters 2-4 (u)**

Permisos de l'**Usuari propietari**. 
 Ex: rwx o rw-

</div>

<div class="md-card" markdown="1">

**Caràcters 5-7 (g)**

Permisos del **Grup propietari**. 
 Ex: r-x o rw-

</div>

<div class="md-card" markdown="1">

**Caràcters 8-10 (o)**

Permisos de **Altres usuaris**. 
 Ex: r-- o ---

</div>

</div>

## Modificació Simbòlica amb la Comanda chmod

<p class="md-kicker">MODIFICACIÓ DE PERMISOS</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### Operadors Simbòlics

- **+ (Afegir):** Afegeix un permís concret sense alterar els que ja existien.
- **- (Treure):** Elimina un permís concret conservant la resta intactes.
- **= (Establir):** Sobreescriu i assigna exactament els permisos indicats, esborrant els anteriors.

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### Exemples Pràctics

<div class="md-callout" markdown="1">

\# Afegeix permís d'escriptura al grup: 
 $ chmod g+w document.txt 
 
 # Treu el permís de lectura als altres usuaris: 
 $ chmod o-r document.txt 
 
 # Assigna exactament rwx al propietari: 
 $ chmod u=rwx script.sh

</div>

</div>

</div>

## Diapositiva 6

**SISTEMA NUMÈRIC**

**Notació Numèrica Octal (Valors 4, 2, 1)**

La notació numèrica assigna un valor binari/octal ponderat a cada tipus de permís individual. Sumant aquests valors s'obté un digit decimal (0-7) per a cada grup (u, g, o):

| Permís | Lletra | Valor Numèric | Significat i funció del permís |
|---|---|---|---|
| Lectura | r | 4 | Permet llegir el contingut del fitxer o llistar directori. |
| Escriptura | w | 2 | Permet editar, modificar o esborrar el fitxer/directori. |
| Execució | x | 1 | Permet executar com a programa o accedir (cd) al directori. |

## Diapositiva 7

**CÀLCUL DE COMBINACIONS**

**Combinacions Octals de Permisos**

| Valor Octal | Símbol | Suma de Valors |
|---|---|---|
| 0 | --- | Cap permís assignat (0+0+0) |
| 1 | --x | Només Execució (1) |
| 2 | -w- | Només Escriptura (2) |
| 3 | -wx | Escriptura + Execució (2+1) |

| Valor Octal | Símbol | Suma de Valors |
|---|---|---|
| 4 | r-- | Només Lectura (4) |
| 5 | r-x | Lectura + Execució (4+1) |
| 6 | rw- | Lectura + Escriptura (4+2) |
| 7 | rwx | Tots els permisos (4+2+1) |

## Exemple de Càlcul Octal (chmod 755 i 644)

<p class="md-kicker">CÀLCUL RESOLUT</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### chmod 755 (Directoris/Scripts)

- **Propietari (7):** 4+2+1 = rwx (Control total)
- **Grup (5):** 4+0+1 = r-x (Llegir i accedir)
- **Altres (5):** 4+0+1 = r-x (Llegir i accedir)

<div class="md-callout" markdown="1">

$ chmod 755 /var/www/html 
 Resultat: drwxr-xr-x

</div>

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### chmod 644 (Fitxers Estàndard)

- **Propietari (6):** 4+2+0 = rw- (Llegir i modificar)
- **Grup (4):** 4+0+0 = r-- (Només lectura)
- **Altres (4):** 4+0+0 = r-- (Només lectura)

<div class="md-callout" markdown="1">

$ chmod 644 document.pdf 
 Resultat: -rw-r--r--

</div>

</div>

</div>

## Llistes de Control d'Accés (ACL)

<p class="md-kicker">PERMISOS AVANÇATS</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#8B5CF6" markdown="1">

### Per què calen les ACLs?

Els permisos tradicionals POSIX (u, g, o) són molt limitats: només permeten assignar un sol usuari i un sol grup a cada fitxer.

Les **ACLs (Access Control Lists)** permeten assignar permisos específics i individualitzats a múltiples usuaris i múltiples grups diferents sobre el mateix recurs.

</div>

<div class="md-card" style="--card:#0284C7" markdown="1">

### Instal·lació i Identificadors

En distribucions Debian/Ubuntu cal instal·lar el paquet:

<div class="md-callout" markdown="1">

$ sudo apt-get install acl

</div>

- u:usuari:permisos (Usuari específic)
- g:grup:permisos (Grup específic)
- m::permisos (Màscara de límit)

</div>

</div>

## La Màscara (m) com a Sostre de Seguretat

<p class="md-kicker">MECANISME DE SEGURETAT</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#EF4444" markdown="1">

### Concepte de la Màscara (m)

La màscara defineix el **sostre o límit màxim de permisos efectius** que poden tenir tots els usuaris addicionals i grups assignats mitjançant l'ACL.

Si un usuari té permís rwx a l'ACL però la màscara s'estableix en r--, el permís efectiu de l'usuari serà només de lectura (r--).

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### Utilitat Pràctica de la Màscara

Permet restringir de cop l'accés a tots els usuaris externs d'un directori compartit sense haver d'esborrar o editar les regles ACL una per una:

<div class="md-callout" markdown="1">

\# Bloquejar tot l'accés ACL: 
 $ setfacl -m m::--- carpeta 
 
 # Restablir el sostre màxim: 
 $ setfacl -m m::rwx carpeta

</div>

</div>

</div>

## Comandes de Gestió d'ACLs (getfacl i setfacl)

<p class="md-kicker">EINES DE LÍNIA D'ORDRES</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### getfacl

Mostra la llista detallada d'ACLs d'un fitxer o directori (propietari, grup, usuaris addicionals i màscara).

<div class="md-callout" markdown="1">

$ getfacl fitxer.txt

</div>

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### setfacl -m

Modifica o afegeix una nova regla d'ACL a l'element.

<div class="md-callout" markdown="1">

$ setfacl -m u:marta:rw fitxer.txt

</div>

</div>

<div class="md-card" style="--card:#8B5CF6" markdown="1">

### setfacl -d

Defineix permisos per defecte (Default) que s'heretaran automàticament en crear nous fitxers.

<div class="md-callout" markdown="1">

$ setfacl -d -m g:profe:rwx /dir

</div>

</div>

</div>

## Resum d'Estudi - Seguretat Lògica Linux

La gestió de permisos en Linux combina la notació simbòlica/octal bàsica (u, g, o amb valors 4, 2, 1) amb el control d'accés avançat mitjançant **ACLs** (setfacl / getfacl) i la **màscara m** per a la màxima flexibilitat i seguretat.
