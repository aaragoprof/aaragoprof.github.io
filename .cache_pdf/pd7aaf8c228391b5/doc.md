# Seguretat Lògica - Control d'Accés, DAC i Matrius

## Diapositiva 1

![Imatge 1](@@IMG@@/img-001.jpg){ loading=lazy }

![Imatge 2](@@IMG@@/img-002.png){ loading=lazy }

**Seguretat Lògica i Control d'Accés**

**MÒDUL DE SEGURETAT INFORMÀTICA**

Material d'estudi detallat: Autenticació vs. Autorització, Subjectes i Objectes, Polítiques DAC i Matrius de Control d'Accés

## Diapositiva 2

**FONAMENTS DE SEGURETAT**

**Concepte de Seguretat Lògica i Control d'Accés**

La **seguretat lògica** complementa les mesures físiques. El seu objectiu principal és el **control d'accés als sistemes informàtics**, verificant qui és una persona abans de concedir-li permís d'accés a dades o serveis interns.

**Identificació Prèvia**

**Cadena de Seguretat**

**Eines de Concreció**

Abans d'aplicar qualsevol permís o dret, cal verificar de manera inqüestionable la identitat de l'usuari o entitat sol·licitant.

Les mesures de control formen part de la cadena de seguretat global, evitant intromissions o accions il·lícites des de l'interior del sistema.

La definició dels drets d'accés s'estructura mitjançant **Matrius de Control d'Accés** i **Llistes de Control d'Accés (ACL)**.

## Diapositiva 3

**ARQUITECTURA DEL CONTROL D'ACCÉS**

**Autenticació vs. Autorització**

**1. Autenticació (Pas Inicial)**

**2. Autorització i Control**

**Verificació de la Identitat**

• Confirma que l'usuari, programa o entitat és qui diu ser.

**Concessió de Permisos Interns**

• Un cop autenticat l'usuari, s'avalua la **base de dades d'autorització**.

• **Funció principal:** Determina si l'entitat pot creuar el perímetre i entrar al sistema o ha de quedar-se fora.

• **Funció principal:** Determina a quins recursos interns (objectes) pot accedir i quin tipus d'accés (r, w, x) té permès.

• Es basa en credencials (contrasenyes, tokens, biometria).

• Evita que un usuari validat accedeixi a dades no autoritzades.

## Diapositiva 4

**MODEL DE PROCESSAMENT**

**Flux de Treball en el Control d'Accés**

**Usuari / Administrador**

Inicia la petició d'accés o configura les polítiques de seguretat.

**Funció d'Autenticació**

Valida les credencials d'entrada contra el registre d'usuaris.

**Funció de Control d'Accés**

Consulta la **Base de Dades d'Autorització** i concedeix o denega l'operació sobre l'objecte.

## Diapositiva 5

**COMPONENTS DEL MODEL**

**Entitats Clau: Subjectes i Objectes**

**Subjecte (Entitat Activa)**

**Objecte (Entitat Passiva)**

És l'entitat capaç de demanar i realitzar accessos sobre els objectes del sistema.

És qualsevol recurs del sistema que té l'accés controlat i protegit.

• Entitat dissenyada per emmagatzemar i/o rebre informació.

• Quan un usuari o aplicació demana un recurs, l'accés el realitza un **procés que els representa**.

• **Exemples:** Fitxers, directoris, programes, bases de dades, servidors o impressores.

• Habitualment s'utilitza el terme "usuari" com a sinònim de subjecte.

## Diapositiva 6

**CLASSIFICACIÓ DE PERMISOS**

**Classes de Subjectes i Drets d'Accés**

**Classes de Subjectes**

**Tipus de Drets d'Accés**

• **Propietari:** Creador de l'objecte o usuari a qui se li ha assignat la propietat individual.

• **Lectura (r):** Visualitzar, copiar o imprimir la informació d'un recurs.

• **Escriptura (w):** Afegir, modificar o editar dades d'un recurs.

• **Grup:** Conjunt d'usuaris que comparteixen determinats privilegis d'accés comuns.

• **Execució (x):** Executar un programa o script específic.

• **Altres:** Usuaris generals que no són ni propietaris ni membres del grup.

• **Esborrament (d):** Eliminar recursos o fitxers del sistema.

## Diapositiva 7

**POLÍTIQUES DE CONTROL**

**Control d'Accés Discrecional (DAC)**

**Concepte de DAC**

**Exemple Pràctic**

El **Control d'Accés Discrecional (DAC)** és una política de seguretat basada en la **identitat del sol·licitant** i en regles que especifiquen quines accions estan permeses a cada subjecte.

L'acció típica de crear un document en un sistema de fitxers o en el núvol (ex: Google Drive, OneDrive) i decidir compartir-lo directament amb un company assignant-li permisos de lectura o edició.

**Mecanisme Discrecional:** Significa que un subjecte que té permís sobre un objecte pot, **a la seva pròpia discreció**, concedir o delegar aquests mateixos permisos a altres usuaris.

## Diapositiva 8

**IMPLEMENTACIÓ DEL DAC**

**La Matriu de Control d'Accés**

La **Matriu de Control d'Accés** és l'eina formal més freqüent per implementar la política DAC. S'organitza com una taula bidimensional:

| Components | Representació en la Matriu | Funció de la Cel·la |
|---|---|---|
| Files | Subjectes (Usuaris, Grups, Processos) | Cada fila correspon a una entitat activa del sistema que pot sol·licitar accés. |
| Columnes | Objectes (Fitxers, Directoris, Dispositius) | Cada columna correspon a un recurs passiu del sistema amb accés protegit. |
| Intersecció (Cel·les) | Drets d'Accés (r, w, x, d) | Indica el conjunt exacter d'operacions permeses al subjecte de la fila sobre l'objecte de la columna. |

## Diapositiva 9

**EXEMPLE DE MATRIU**

**Exemple Pràctic de Matriu de Control d'Accés**

Nomenclatura standard: **r** = Lectura, **w** = Escriptura, **x** = Execució, **o** = Propietari (Owner)

| Subjectes \\ Objectes | Fitxer1.txt | Fitxer2.exec | Programa\_A | Impressora\_1 |
|---|---|---|---|---|
| Usuari\_1 (Propietari) | r, w, o | r, w, x, o | r, x | w (imprimir) |
| Usuari\_2 (Grup) | r | r, x | x | - |
| Usuari\_3 (Altres) | - | - | x | - |

## Diapositiva 10

**OPTIMITZACIÓ DE MEMÒRIA**

**De la Matriu a les Llistes ACL**

En sistemes reals amb milers d'usuaris i milions de fitxers, la matriu d'accés és immensa i conté majoritàriament cel·les buides (matriu dispersa), ocupant massa memòria.

**Inconvenient de la Matriu**

**Solució: Llistes ACL**

En lloc de desar tota la matriu, **s'associa a cada objecte una llista (ACL)** que conté únicament els subjectes que tenen permisos sobre ell i el tipus d'accés autoritzat.

## Diapositiva 11

![Imatge 3](@@IMG@@/img-003.jpg){ loading=lazy }

![Imatge 4](@@IMG@@/img-004.png){ loading=lazy }

**Resum d'Estudi - Control d'Accés i DAC**

La seguretat lògica s'articula primer identificant l'usuari (Autenticació) i desprès concedint permisos (Autorització) mitjançant la política **DAC**, representada formalment per la **Matriu de Control d'Accés** i implementada eficientment en sistemes reals a través de les **ACLs**.
