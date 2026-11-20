# Seguretat Lògica i Control d'Accés

<p class="md-kicker">MÒDUL DE SEGURETAT INFORMÀTICA</p>

Material d'estudi detallat: Autenticació vs. Autorització, Subjectes i Objectes, Polítiques DAC i Matrius de Control d'Accés

## Concepte de Seguretat Lògica i Control d'Accés

<p class="md-kicker">FONAMENTS DE SEGURETAT</p>

La **seguretat lògica** complementa les mesures físiques. El seu objectiu principal és el **control d'accés als sistemes informàtics**, verificant qui és una persona abans de concedir-li permís d'accés a dades o serveis interns.

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### Identificació Prèvia

Abans d'aplicar qualsevol permís o dret, cal verificar de manera inqüestionable la identitat de l'usuari o entitat sol·licitant.

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### Cadena de Seguretat

Les mesures de control formen part de la cadena de seguretat global, evitant intromissions o accions il·lícites des de l'interior del sistema.

</div>

<div class="md-card" style="--card:#8B5CF6" markdown="1">

### Eines de Concreció

La definició dels drets d'accés s'estructura mitjançant **Matrius de Control d'Accés** i **Llistes de Control d'Accés (ACL)**.

</div>

</div>

## Autenticació vs. Autorització

<p class="md-kicker">ARQUITECTURA DEL CONTROL D'ACCÉS</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### 1. Autenticació (Pas Inicial)

**Verificació de la Identitat**

- Confirma que l'usuari, programa o entitat és qui diu ser.
- **Funció principal:** Determina si l'entitat pot creuar el perímetre i entrar al sistema o ha de quedar-se fora.
- Es basa en credencials (contrasenyes, tokens, biometria).

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### 2. Autorització i Control

**Concessió de Permisos Interns**

- Un cop autenticat l'usuari, s'avalua la **base de dades d'autorització**.
- **Funció principal:** Determina a quins recursos interns (objectes) pot accedir i quin tipus d'accés (r, w, x) té permès.
- Evita que un usuari validat accedeixi a dades no autoritzades.

</div>

</div>

## Flux de Treball en el Control d'Accés

<p class="md-kicker">MODEL DE PROCESSAMENT</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

**Usuari / Administrador**

Inicia la petició d'accés o configura les polítiques de seguretat.

</div>

<div class="md-card" style="--card:#F59E0B" markdown="1">

**Funció d'Autenticació**

Valida les credencials d'entrada contra el registre d'usuaris.

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

**Funció de Control d'Accés**

Consulta la **Base de Dades d'Autorització** i concedeix o denega l'operació sobre l'objecte.

</div>

</div>

## Entitats Clau: Subjectes i Objectes

<p class="md-kicker">COMPONENTS DEL MODEL</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### Subjecte (Entitat Activa)

És l'entitat capaç de demanar i realitzar accessos sobre els objectes del sistema.

- Quan un usuari o aplicació demana un recurs, l'accés el realitza un **procés que els representa**.
- Habitualment s'utilitza el terme "usuari" com a sinònim de subjecte.

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### Objecte (Entitat Passiva)

És qualsevol recurs del sistema que té l'accés controlat i protegit.

- Entitat dissenyada per emmagatzemar i/o rebre informació.
- **Exemples:** Fitxers, directoris, programes, bases de dades, servidors o impressores.

</div>

</div>

## Classes de Subjectes i Drets d'Accés

<p class="md-kicker">CLASSIFICACIÓ DE PERMISOS</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### Classes de Subjectes

- **Propietari:** Creador de l'objecte o usuari a qui se li ha assignat la propietat individual.
- **Grup:** Conjunt d'usuaris que comparteixen determinats privilegis d'accés comuns.
- **Altres:** Usuaris generals que no són ni propietaris ni membres del grup.

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### Tipus de Drets d'Accés

- **Lectura (r):** Visualitzar, copiar o imprimir la informació d'un recurs.
- **Escriptura (w):** Afegir, modificar o editar dades d'un recurs.
- **Execució (x):** Executar un programa o script específic.
- **Esborrament (d):** Eliminar recursos o fitxers del sistema.

</div>

</div>

## Control d'Accés Discrecional (DAC)

<p class="md-kicker">POLÍTIQUES DE CONTROL</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#8B5CF6" markdown="1">

### Concepte de DAC

El **Control d'Accés Discrecional (DAC)** és una política de seguretat basada en la **identitat del sol·licitant** i en regles que especifiquen quines accions estan permeses a cada subjecte.

<div class="md-callout" style="--card:#A855F7" markdown="1">

**Mecanisme Discrecional:** Significa que un subjecte que té permís sobre un objecte pot, **a la seva pròpia discreció**, concedir o delegar aquests mateixos permisos a altres usuaris.

</div>

</div>

<div class="md-card" style="--card:#0284C7" markdown="1">

### Exemple Pràctic

L'acció típica de crear un document en un sistema de fitxers o en el núvol (ex: Google Drive, OneDrive) i decidir compartir-lo directament amb un company assignant-li permisos de lectura o edició.

</div>

</div>

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

## De la Matriu a les Llistes ACL

<p class="md-kicker">OPTIMITZACIÓ DE MEMÒRIA</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#EF4444" markdown="1">

### Inconvenient de la Matriu

En sistemes reals amb milers d'usuaris i milions de fitxers, la matriu d'accés és immensa i conté majoritàriament cel·les buides (matriu dispersa), ocupant massa memòria.

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### Solució: Llistes ACL

En lloc de desar tota la matriu, **s'associa a cada objecte una llista (ACL)** que conté únicament els subjectes que tenen permisos sobre ell i el tipus d'accés autoritzat.

</div>

</div>

## Resum d'Estudi - Control d'Accés i DAC

La seguretat lògica s'articula primer identificant l'usuari (Autenticació) i desprès concedint permisos (Autorització) mitjançant la política **DAC**, representada formalment per la **Matriu de Control d'Accés** i implementada eficientment en sistemes reals a través de les **ACLs**.
