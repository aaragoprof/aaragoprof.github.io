# Seguretat Passiva i Física

<p class="md-kicker">MÒDUL DE SEGURETAT INFORMÀTICA</p>

Material d'estudi: Protecció Ambiental, Emplaçament del CPD, Càmeres i Sensors, Protecció Elèctrica i Gestió de Contrasenyes

## Concepte i Importància de la Seguretat Passiva

<p class="md-kicker">FONAMENTS DEL SISTEMES</p>

La **seguretat passiva i física** estudia els aspectes destinats a minimitzar els riscos físics i ambientals sobre els equips informàtics. Constitueix la base sòlida sobre la qual es construeix qualsevol mesura de seguretat lògica.

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### Base de la Cadena

Una fallada o descuit en la seguretat física pot comprometre directament la seguretat global, per molt sofisticat que sigui el software o xifratge.

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### Prevenir i Minimitzar

Optimitza les condicions entorn del maquinari per reduir la probabilitat d'accidents, desastres naturals o robatoris directes.

</div>

<div class="md-card" style="--card:#8B5CF6" markdown="1">

### Continuïtat Operativa

Assegura que els usuaris autoritzats mantinguin l'accés ininterromput a les dades evitant danys catastròfics al hardware.

</div>

</div>

## Emplaçament del CPD i Prevenció d'Incendis

<p class="md-kicker">PROTECCIÓ AMBIENTAL</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### Emplaçament Físic

- **Discreció i visibilitat baixa:** Triar ubicacions poc cridaneres per no atreure l'atenció de possibles atacants o intrusos.
- **Catàstrofes naturals:** Evitar zones de risc d'inundació (com soterranis vulnerables) o zones propenses a esllavissades.
- **Estructura resistent:** Murs i sostres preparats per suportar càrregues pesades de racks i servidors.

</div>

<div class="md-card" style="--card:#EF4444" markdown="1">

### Prevenció d'Incendis

- **Detecció precoç:** Instal·lació de detectors de fum i de temperatura d'alta sensibilitat.
- **Extinció adequada:** Ús de sistemes d'extinció neta (gasos inerts o contaminants no conductors) que apaguin el foc sense danyar l'equipament electrònic delicat (evitar l'aigua en sales de servidors).

</div>

</div>

## Categories de Mesures Físiques

<p class="md-kicker">CONTROL D'ACCÉS FÍSIC</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#F59E0B" markdown="1">

### 1. Mesures Dissuasives

Despleguen una barrera psicològica o visual per fer canviar d'opinió als intrusos.

- Tanques perimetrals
- Guàrdies de seguretat
- Cartells d'advertència i càmeres visibles

</div>

<div class="md-card" style="--card:#0284C7" markdown="1">

### 2. Restricció d'Accés

Dificulten o impedeixen l'entrada física a personal no autoritzat.

- Targetes d'accés / Teclat numèric
- Control biomètric (empremta/iris)
- Portes de doble pas (mantraps)

</div>

<div class="md-card" style="--card:#8B5CF6" markdown="1">

### 3. Detecció d'Intrusos

Identifiquen presències no permeses i alerten els equips de seguretat.

- Sensors de moviment i volumètrics
- Detectors acústics / de ruptura de vidre
- Control d'alimentació anti-sabotatge

</div>

</div>

## Garantia del Subministrament Elèctric

<p class="md-kicker">FIABILITAT ENERGÈTICA</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#EF4444" markdown="1">

### Risc de les Alteracions Elèctriques

Les alteracions en la xarxa elèctrica (com tallades de llum, sobretensions brusques o caigudes de voltatge) representen un **risc greu per als equips electrònics**.

Poden provocar des de la corrupció de dades immediata fins a danys irreparables en els components interns del maquinari.

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### El paper del SAI / UPS

Un **SAI (Sistema d'Alimentació Ininterrompuda)** és un dispositiu que:

- Subministra energia d'emergència des de bateries durant una caiguda de xarxa.
- Permet mantenir els equips en funcionament o tancar-los de manera segura.
- Filtra i estabilitza el senyal elèctric.

</div>

</div>

## Els 3 Factors d'Autenticació

<p class="md-kicker">AUTENTICACIÓ</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### 1. Alguna cosa que SAPS

Informació o coneixement secret que l'usuari ha de recordar.

<div class="md-callout" markdown="1">

**Ex: Contrasenyes, codis PIN, preguntes de seguretat.**

</div>

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### 2. Alguna cosa que TENS

Un objecte o dispositiu físic únic en possessió de l'usuari.

<div class="md-callout" markdown="1">

**Ex: Tarjeta d'accés, token USB, telèfon (MFA/OTP).**

</div>

</div>

<div class="md-card" style="--card:#8B5CF6" markdown="1">

### 3. Alguna cosa que ETS

Característiques biològiques o comportamentals úniques.

<div class="md-callout" markdown="1">

**Ex: Empremta dactilar, reconeixement facial, iris.**

</div>

</div>

</div>

## Polítiques de Contrasenyes Segures

<p class="md-kicker">BONES PRÀCTIQUES</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#16A34A" markdown="1">

### Requisits d'una Contrasenya Robust

- **Longitud mínima:** Pel cap baix 10 caràcters de longitud.
- **Complexitat:** Combinar majúscules, minúscules, números i caràcters especials (ex: K#zu4^40\\12).
- **Sense dades personals:** No incloure noms, dates de naixement o paraules de diccionari.
- **Contrasenyes úniques:** Mai reutilitzar la mateixa contrasenya en diferents serveis.

</div>

<div class="md-card" style="--card:#0284C7" markdown="1">

### Gestors de Contrasenyes

Per facilitar la gestió de múltiples claus complexes i úniques sense haver de recordar-les totes:

- **Basats en el núvol:** Les dades es guarden xifrades i se sincronitzen entre dispositius.
- Permeten generar claus aleatòries d'alta seguretat automàticament.

</div>

</div>

## Resum d'Estudi - Seguretat Passiva i Física

La seguretat passiva i física protegeix la infraestructura mitjançant un bon emplaçament, prevenció d'incendis, restriccions d'accés, protecció elèctrica amb **SAI** i una autenticació robusta basada en **3 factors** i contrasenyes segures.
