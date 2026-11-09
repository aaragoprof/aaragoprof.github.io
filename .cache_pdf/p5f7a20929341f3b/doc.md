# Seguretat Lògica Linux - Permisos i ACLs

## Diapositiva 1

![Imatge 1](@@IMG@@/img-001.jpg){ loading=lazy }

![Imatge 2](@@IMG@@/img-002.png){ loading=lazy }

**Seguretat Lògica en Linux**

**MÒDUL D'ADMINISTRACIÓ DE SISTEMES OPERATIUS**

Material d'estudi: Grups de Permisos, Notació Simbòlica i Numèrica Octal, Comanda chmod i Llistes ACL Avançades

## Diapositiva 2

**ESTRUCTURA D'ACCÉS**

**Els 3 Grups de Permisos (u, g, o, a)**

En crear qualsevol fitxer o directori en GNU/Linux, el sistema operatiu divideix la gestió dels drets d'accés en **tres categories principals d'usuaris**:

**Usuari Propietari (u)**

**Grup Propietari (g)**

**Altres Usuaris (o)**

L'usuari concret (User) que ha creat el fitxer o a qui se li ha assignat la propietat individual.

El grup d'usuaris (Group) assignat al fitxer. Tots els membres d'aquest grup comparteixen els mateixos drets.

La resta d'usuaris del sistema (Others) que no són ni el propietari ni pertanyen al grup assignat.

**\* Comodí All (a): Representa la totalitat dels usuaris de manera simultània (Equivalent a u + g + o).**

## Diapositiva 3

**DRETS D'ACCÉS**

**Tipus de Permisos: Lectura, Escriptura i Execució**

**Lectura (r - Read)**

**Escriptura (w - Write)**

**Execució (x - Execute)**

• **Fitxers:** Permet obrir i veure el contingut intern del fitxer (ex: cat, nano).

• **Fitxers:** Permet modificar, afegir o alterar el contingut del fitxer.

• **Fitxers:** Converteix el fitxer en un programa executable o script (ex: ./script.sh).

• **Directoris:** Permet llistar el contingut dels arxius que inclou el directori (ex: ls).

• **Directoris:** Permet crear nous fitxers o eliminar fitxers existents a l'interior de la carpeta.

• **Directoris:** Permet entrar o accedir al directori (ex: cd carpeta/).

## Diapositiva 4

**VISUALITZACIÓ EN TERMINAL**

**Interpretació de la Notació Simbòlica (ls -l)**

En executar la comanda ls -l, la primera columna consta de **10 caràcters** que es llegeixen d'esquerra a dreta:

drwxr-xr-- 5 yuri yuri 4096 Feb 15 10:30 directori\_web 
 -rw-rw-r-- 1 yuri yuri 824 Oct 17 11:15 fitxer.txt

**Caràcter 1 (Tipus)**

**Caràcters 2-4 (u)**

**Caràcters 5-7 (g)**

**Caràcters 8-10 (o)**

\- Fitxer normal 
 d Directori 
 l Enllaç simbòlic

Permisos de l'**Usuari propietari**. 
 Ex: rwx o rw-

Permisos del **Grup propietari**. 
 Ex: r-x o rw-

Permisos de **Altres usuaris**. 
 Ex: r-- o ---

## Diapositiva 5

**MODIFICACIÓ DE PERMISOS**

**Modificació Simbòlica amb la Comanda chmod**

**Operadors Simbòlics**

**Exemples Pràctics**

• **+ (Afegir):** Afegeix un permís concret sense alterar els que ja existien.

\# Afegeix permís d'escriptura al grup: 
 $ chmod g+w document.txt 
 
 # Treu el permís de lectura als altres usuaris: 
 $ chmod o-r document.txt 
 
 # Assigna exactament rwx al propietari: 
 $ chmod u=rwx script.sh

• **- (Treure):** Elimina un permís concret conservant la resta intactes.

• **= (Establir):** Sobreescriu i assigna exactament els permisos indicats, esborrant els anteriors.

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

## Diapositiva 8

**CÀLCUL RESOLUT**

**Exemple de Càlcul Octal (chmod 755 i 644)**

• **Propietari (7):** 4+2+1 = rwx (Control total)

**chmod 755 (Directoris/Scripts)**

• **Propietari (6):** 4+2+0 = rw- (Llegir i modificar)

**chmod 644 (Fitxers Estàndard)**

• **Grup (5):** 4+0+1 = r-x (Llegir i accedir)

• **Grup (4):** 4+0+0 = r-- (Només lectura)

• **Altres (5):** 4+0+1 = r-x (Llegir i accedir)

• **Altres (4):** 4+0+0 = r-- (Només lectura)

$ chmod 755 /var/www/html 
 Resultat: drwxr-xr-x

$ chmod 644 document.pdf 
 Resultat: -rw-r--r--

## Diapositiva 9

**PERMISOS AVANÇATS**

**Llistes de Control d'Accés (ACL)**

**Per què calen les ACLs?**

**Instal·lació i Identificadors**

Els permisos tradicionals POSIX (u, g, o) són molt limitats: només permeten assignar un sol usuari i un sol grup a cada fitxer.

En distribucions Debian/Ubuntu cal instal·lar el paquet:

Les **ACLs (Access Control Lists)** permeten assignar permisos específics i individualitzats a múltiples usuaris i múltiples grups diferents sobre el mateix recurs.

$ sudo apt-get install acl

• u:usuari:permisos (Usuari específic)

• g:grup:permisos (Grup específic)

• m::permisos (Màscara de límit)

## Diapositiva 10

**MECANISME DE SEGURETAT**

**La Màscara (m) com a Sostre de Seguretat**

**Concepte de la Màscara (m)**

**Utilitat Pràctica de la Màscara**

La màscara defineix el **sostre o límit màxim de permisos efectius** que poden tenir tots els usuaris addicionals i grups assignats mitjançant l'ACL.

Permet restringir de cop l'accés a tots els usuaris externs d'un directori compartit sense haver d'esborrar o editar les regles ACL una per una:

Si un usuari té permís rwx a l'ACL però la màscara s'estableix en r--, el permís efectiu de l'usuari serà només de lectura (r--).

\# Bloquejar tot l'accés ACL: 
 $ setfacl -m m::--- carpeta 
 
 # Restablir el sostre màxim: 
 $ setfacl -m m::rwx carpeta

## Diapositiva 11

**EINES DE LÍNIA D'ORDRES**

**Comandes de Gestió d'ACLs (getfacl i setfacl)**

**getfacl**

**setfacl -m**

**setfacl -d**

Mostra la llista detallada d'ACLs d'un fitxer o directori (propietari, grup, usuaris addicionals i màscara).

Modifica o afegeix una nova regla d'ACL a l'element.

Defineix permisos per defecte (Default) que s'heretaran automàticament en crear nous fitxers.

$ setfacl -m u:marta:rw fitxer.txt

$ getfacl fitxer.txt

$ setfacl -d -m g:profe:rwx /dir

## Diapositiva 12

![Imatge 3](@@IMG@@/img-003.jpg){ loading=lazy }

![Imatge 4](@@IMG@@/img-004.png){ loading=lazy }

**Resum d'Estudi - Seguretat Lògica Linux**

La gestió de permisos en Linux combina la notació simbòlica/octal bàsica (u, g, o amb valors 4, 2, 1) amb el control d'accés avançat mitjançant **ACLs** (setfacl / getfacl) i la **màscara m** per a la màxima flexibilitat i seguretat.
