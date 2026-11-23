# Seguretat Activa: Introducció

<p class="md-kicker">MÒDUL DE SEGURETAT INFORMÀTICA</p>

Principis estratègics, classificació d'atacs i cicle de vida d'una intrusió

## Principis de la Protecció de la Informació

<p class="md-kicker">FONAMENTS ESTRATÈGICS</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### Objectiu Global

La seguretat abasta tota la infraestructura tecnològica.

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### Disseny Integrat

Forma part estructural de tota l'organització.

</div>

<div class="md-card" style="--card:#EAB308" markdown="1">

### Marc Legal

Integrat des de l'inici a les polítiques internes.

</div>

</div>

## Seguretat Activa vs. Seguretat Passiva

<p class="md-kicker">ENFOCAMENT DEFENSIU</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### Seguretat Activa

Mecanismes físics i lògics per prevenir i detectar intents de comprometre el sistema.

</div>

<div class="md-card" style="--card:#8B5CF6" markdown="1">

### Seguretat Passiva

Mesures per minimitzar els efectes d'un incident i informar els administradors.

</div>

</div>

## Diapositiva 4

**ACTIU CRÍTIC**

**L'Actiu Més Valuós: Les Dades**

**Les Dades Són Irreemplaçables**

El maquinari i el programari es poden substituir gairebé sempre; la informació perduda, no.

## Classificació Segons l'Objectiu de l'Atac

<p class="md-kicker">TIPOLOGIA D'AMENACES</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#EF4444" markdown="1">

### Interrupció

Atac contra la disponibilitat d'un recurs.

</div>

<div class="md-card" style="--card:#EAB308" markdown="1">

### Intercepció

Atac contra la confidencialitat per accés il·legítim.

</div>

<div class="md-card" style="--card:#0284C7" markdown="1">

### Modificació

Accés no autoritzat amb alteració de dades.

</div>

<div class="md-card" style="--card:#8B5CF6" markdown="1">

### Fabricació

Inserció d'objectes falsificats al sistema.

</div>

</div>

## Atacs Passius vs. Atacs Actius

<p class="md-kicker">FORMA D'EXECUCIÓ</p>

<div class="md-card" markdown="1">



</div>

| Criteri | Atacs Passius | Atacs Actius |
|---|---|---|
| Acció sobre el sistema | Observa i escolta sense alterar dades | Altera, destrueix o falsifica recursos |
| Objectiu principal | Obtenir informació confidencial | Suplantació, degradació o modificació |
| Facilitat de detecció | Molt difícil (no deixa rastre d'alteració) | Més detectable per l'impacte visible |

## Atacants Externs vs. Atacants Interns

<p class="md-kicker">ORIGEN DE L'AMENAÇA</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### Atacs Externs

- Són molt més nombrosos en volum.
- Troben barreres perimetrals inicials.

</div>

<div class="md-card" style="--card:#EF4444" markdown="1">

### Atacs Interns

- Percentatge d'èxit molt més elevat.
- Provoquen un dany molt superior.

</div>

</div>

## Anatomia dels Atacs: Preparació i Accés

<p class="md-kicker">CICLE D'INTRUSIÓ (I)</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### 1. Reconeixement

Recopilació prèvia d'informació sobre l'objectiu.

</div>

<div class="md-card" style="--card:#EAB308" markdown="1">

### 2. Escaneig

Sondeig del sistema per detectar vulnerabilitats.

</div>

<div class="md-card" style="--card:#EF4444" markdown="1">

### 3. Accés al Sistema

Explotació efectiva de les fallades localitzades.

</div>

</div>

## Anatomia dels Atacs: Persistència i Ocultació

<p class="md-kicker">CICLE D'INTRUSIÓ (II)</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#8B5CF6" markdown="1">

### 4. Manteniment de l'Accés

Assegurar vies d'entrada persistents per a futurs accessos no autoritzats.

</div>

<div class="md-card" style="--card:#EF4444" markdown="1">

### 5. Esborrat d'Empremtes

Eliminació de registres en fitxers de log i alarmes IDS per evitar ser descobert.

</div>

</div>

## Resum d'Estudi - Seguretat Activa

Protegir les dades requereix combinar prevenció activa i mitigació passiva, comprenent tant les amenaces internes com les **5 fases d'un atac informàtic**.
