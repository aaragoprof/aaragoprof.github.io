# Monitoratge de Xarxes 2: BYOD i MDM

<p class="md-kicker">MÒDUL DE SEGURETAT I MONITORATGE</p>

Material d'estudi: Gestió de Dispositius Personals en Entorns Corporatius, Vectors d'Intrusió i Solucions de Control MDM

## BYOD (Bring Your Own Device): Concepte i Evolució

<p class="md-kicker">NOU ENTORN DE TREBALL</p>

Tradicionalment, les empreses adquirien i configuraven cada equips. Amb el model **BYOD**, els empleats utilitzen els seus propis dispositius personals (portàtils, smartphones, tauletes) per fer feina.

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### Canvi de Paradigmàtica

Transició d'equips 100% corporatius homogenis a una xarxa heterogènia plena de dispositius personals de diferents fabricants i sistemes operatius.

</div>

<div class="md-card" style="--card:#F59E0B" markdown="1">

### Connexió a Recursos Interns

El dispositiu privat s'ha de connectar directament als serveis crítics de l'empresa: correu, servidors de fitxers i aplicacions internes.

</div>

<div class="md-card" style="--card:#8B5CF6" markdown="1">

### Barreja de Dades

En un mateix aparell conviuen fotos personals, aplicacions d'oci i documents confidencials o dades de clients.

</div>

</div>

## Coexistència de Dades Personals i Corporatives

<p class="md-kicker">DILEMA PRIVACITAT VS SEGURETAT</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### Àmbit Personal

- Fotografies, vídeos i fitxers privats.
- Xarxes socials i aplicacions d'oci.
- Drets de privacitat indiscutibles per a l'empleat.

</div>

<div class="md-card" style="--card:#EF4444" markdown="1">

### Àmbit Corporatiu

- Documents confidencials, bases de dades i claus d'accés.
- Correu corporatiu i eines de comunicació interna.
- Requisits de compliment de protecció de dades (RGPD).

</div>

</div>

## BYOD Amplia el Vector d'Intrusió a la Xarxa

<p class="md-kicker">AVALUACIÓ DE RISCS</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#EF4444" markdown="1">

### Programari no Controlat

L'usuari pot tenir instal·lades aplicacions amb vulnerabilitats, eines sense actualitzar o jocs amb malware ocult.

</div>

<div class="md-card" style="--card:#F59E0B" markdown="1">

### Fuga de Dades per Pèrdua

Si el mòbil o el portàtil privat es perd o és robat, qualsevol persona pot accedir a la informació interna si no està xifrat.

</div>

<div class="md-card" style="--card:#8B5CF6" markdown="1">

### Enginyeria Social i Phishing

Els dispositius personals tenen menys filtres i proteccions contra enganys de Phishing que els equips gestionats per TI.

</div>

</div>

## Per què un Tallafoc Bàsic no és Suficient?

<p class="md-kicker">INSUFICIÈNCIA DE PROTECCIONS TRADICIONALS</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#EF4444" markdown="1">

### El Límit del Perímetre

Un tallafoc (Firewall) tradicional protegeix la frontera de la xarxa, però quan un usuari connecta el seu dispositiu infectat per VPN o Wi-Fi interna, **l'amenaça ja està dins del perímetre**.

</div>

<div class="md-card" style="--card:#0284C7" markdown="1">

### L'Objectiu: Assegurar els Actius

Cal exercir un control actiu directament sobre l'extrem (endpoint) sense violar la privacitat de l'usuari.

<div class="md-callout" style="--card:#0284C7" markdown="1">

**Així neix la necessitat dels sistemes MDM (Mobile Device Management).**

</div>

</div>

</div>

## MDM (Mobile Device Management): La Solució Corporativa

<p class="md-kicker">EINES DE CONTROL</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#16A34A" markdown="1">

### Definició de MDM

Programari centralitzat que permet als administradors de TI monitoritzar, gestionar i aplicar polítiques de seguretat en els dispositius mòbils que accedeixen a la xarxa.

- Automatitza la configuració d'equips remots.
- Distribueix aplicacions autoritzades de forma segura.

</div>

<div class="md-card" style="--card:#0284C7" markdown="1">

### Equilibri entre Control i Privacitat

Permet a l'empresa protegir les seves dades **sense poder veure ni accedir a les fotos, xats o aplicacions personals** de l'empleat.

</div>

</div>

## Funcionalitat MDM: Contenidors Segurs

<p class="md-kicker">AÏLLAMENT DE DADES</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### Separació Lògica a l'Ordinador/Mòbil

L'MDM crea un **"espai de treball xifrat i aïllat"** (sandbox) dins del dispositiu personal.

- Les aplicacions corporatives (Outlook, Teams, Drives) funcionen dins del contenidor.
- Es bloqueja la possibilitat de copiar/enganxar dades de l'espai corporatiu cap a l'espai personal.

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### Protecció contra Malware Personal

Si un usuari descarrega una aplicació infectada al seu entorn personal, el malware **no pot creuar la frontera del contenidor segur** per extreure fitxers de l'empresa.

</div>

</div>

## Funcionalitat MDM: Esborrat Remot (Wipe)

<p class="md-kicker">RESPOSTA DAVANT DE PÈRDUES</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#EF4444" markdown="1">

### Esborrat Corporatiu Selectiu

Si l'empleat perd el telèfon o deixa l'empresa, l'administrador pot enviar una ordre d'esborrat que destrueix **únicament les dades de l'empresa**.

<div class="md-callout" style="--card:#EF4444" markdown="1">

**Les fotos i documents personals de l'usuari no es veuen afectats.**

</div>

</div>

<div class="md-card" style="--card:#F59E0B" markdown="1">

### Bloqueig de Seguretat

Permet bloquejar el terminal a l'acte i revocar els certificats d'accés a la xarxa des del moment en què es notifica la pèrdua.

</div>

</div>

## Funcionalitat MDM: Polítiques de Seguretat Requerides

<p class="md-kicker">CONTROL D'ACCÉS</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### Autenticació Forta (PIN / Biometria)

Obliga l'usuari a establir un PIN complex o desbloqueig biomètric per poder connectar-se a la xarxa corporativa.

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### Xifratge Obligatori de Disc

Verifica que el dispositiu tingui el xifratge integrat activat (BitLocker, FileVault, Android/iOS Encryption).

</div>

<div class="md-card" style="--card:#8B5CF6" markdown="1">

### Verificació d'Integritat (No Root / Jailbreak)

Denega l'accés si es detecta que el dispositiu ha estat alterat (root o jailbreak), ja que inhabilita les proteccions del SO.

</div>

</div>

## Diapositiva 10

**COMPARATIVA TECNOLÒGICA**

**Escenari BYOD: Sense MDM vs. Amb MDM**

| Característica / Afectació | Escenari BYOD Sense MDM | Escenari BYOD Amb MDM |
|---|---|---|
| Aïllament de Dades | Nul. Dades personals i de l'empresa barrejades | Alt. Contenidors corporatius xifrats i aïllats |
| Acció davant de Pèrdua | Fuga imminent de dades confidencials | Esborrat remot selectiu de les dades de l'empresa |
| Compliment de Requisits | Depèn de la bona voluntat de l'usuari | Automàtic. Bloqueig si no es compleix la política PIN/Xifratge |
| Risc de Malware | Alt. Infecta la xarxa des del dispositiu privat | Mitigat. El malware no pot accedir al contenidor de feina |

## Integració de BYOD en una Estratègia Zero Trust

<p class="md-kicker">ARQUITECTURA GLOBAL</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### 1. Validació de Salut (Posture Check)

Abans de connectar, el sistema comprova si el dispositiu compleix les regles de l'MDM (sistema actualitzat, sense root).

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### 2. Mínim Privilegi

El dispositiu BYOD només rep accés a les aplicacions estrictament necessàries per al seu treball, no a tota la xarxa.

</div>

<div class="md-card" style="--card:#8B5CF6" markdown="1">

### 3. Continuïtat de Vigilància

El monitoratge contínuament verifica si el patró del dispositiu canvia o si mostra comportaments anòmals.

</div>

</div>

## Resum d'Estudi - BYOD i MDM

Adoptar el model **BYOD** permet flexibilitat, però amplia el vector d'intrusió. La implementació de solucions **MDM** és indispensable per crear **contenidors segurs**, executar **esborrats remots selectius** i mantenir la seguretat corporativa sense vulnerar la privacitat dels usuaris.
