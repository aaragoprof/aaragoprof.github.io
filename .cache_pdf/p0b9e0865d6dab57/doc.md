# Protecció Avançada contra Malware

<p class="md-kicker">MÒDUL DE SEGURETAT INFORMÀTICA (PART 4)</p>

Material d'estudi: Virus Polimòrfics, SIEM, Intel·ligència Artificial Defensiva, Model Zero Trust i Evolució del Ransomware

## Panorama Actual del Programari Maliciós (Malware)

<p class="md-kicker">AMENACES MODERNES</p>

El malware modern no cerca només la destrucció, sinó principalment el **benefici econòmic**, la dades personals o el control del sistema mitjançant tècniques molt sofisticades.

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#EF4444" markdown="1">

### Ransomware

Segresta i xifra les dades del sistema exigint un rescat econòmic per desxifrar-les.

</div>

<div class="md-card" style="--card:#F59E0B" markdown="1">

### Spyware i Adware

Espien l'activitat de l'usuari, roben credencials o inunden el sistema amb publicitat.

</div>

<div class="md-card" style="--card:#8B5CF6" markdown="1">

### Phishing i Enginyeria Social

Tècnica d'engany per robar dades confidencials suplantant entitats de confiança.

</div>

<div class="md-card" style="--card:#0284C7" markdown="1">

### Troians i Cucs

Els troians s'amaguen dins d'apps legítimes; els cucs es propaguen sols per la xarxa.

</div>

</div>

## Què és un Virus Polimòrfic?

<p class="md-kicker">MUTACIÓ DE CODI</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#EF4444" markdown="1">

### Concepte de Polimorfisme

Programari maliciós que **canvia el seu propi codi (la seva forma)** cada vegada que s'estén, però mantenint la seva funció maliciosa original.

<div class="md-callout" style="--card:#EF4444" markdown="1">

**Com que la seva empremta digital (hash) canvia constantment, el diccionari de signatures de l'antivirus no el pot reconèixer.**

</div>

</div>

<div class="md-card" style="--card:#0284C7" markdown="1">

### Mecanisme de Mutació

- **Motor de Mutació:** Genera noves claus de xifrat i canvia l'ordre de les instruccions.
- **Capa Externa Variable:** Es xifra amb una clau diferent en cada nova infecció.
- **Execució a RAM:** Es desxifra en memòria RAM per actuar, però en disc sembla un fitxer nou.

</div>

</div>

## Com es Detecten els Virus Polimòrfics?

<p class="md-kicker">DETECCIÓ AVANÇADA</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#16A34A" markdown="1">

### Anàlisi de Comportament (Heurística)

En lloc de mirar com *"és"* el virus, l'antivirus analitza què *"fa"*.

Si un programa intenta capturar dades, monitorar ports o xifrar fitxers sense permís, es bloqueja immediatament.

</div>

<div class="md-card" style="--card:#0284C7" markdown="1">

### Emulació (Sandboxing)

Execució del fitxer en un entorn virtual aïllat i segur.

S'observa si el programa es desxifra i mostra el seu comportament maliciós abans de permetre l'execució al sistema real.

</div>

</div>

## Estratègies Globals de Defensa Informàtica

<p class="md-kicker">ARQUITECTURA DEFENSIVA</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### Antivirus Moderns (EDR / XDR)

Combinació de signatures conegudes amb motor d'anàlisi heurística i resposta automatitzada.

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### Tallafoc (Firewall)

Filtra i controla el trànsit de xarxa en funció de regles de comunicació establertes.

</div>

<div class="md-card" style="--card:#8B5CF6" markdown="1">

### Higiene Digital i Backups

Actualitzacions constants del SO, aplicació del principi de mínims privilegis i backups periòdics.

</div>

</div>

## SIEM: La Pantalla de Control Centralitzada

<p class="md-kicker">CORRELACIÓ D'ESDEVENIMENTS</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### Concepte del SIEM

Plataforma centralitzada que **recull i analitza els registres (logs)** de totes les eines de seguretat de l'empresa (Antivirus, Firewall, IDS, servidors).

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### Valor Afegit: Correlació

Permet detectar atacs complexos coordinats que passarien completament desapercebuts si les eines s'analitzessin de forma aïllada.

</div>

</div>

## Intel·ligència Artificial: Ofensiva vs. Defensiva

<p class="md-kicker">NOVES TECNOLOGIES</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#EF4444" markdown="1">

### IA Ofensiva (Atacants)

- **Malware Generat per IA:** Mutacions de codi ultra-ràpides en qüestió de segons.
- **Deepfakes i Phishing 2.0:** Clonació de veu i vídeo per enganyar empleats en procediments financers.

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### IA Defensiva (Protecció)

- **Models Predictius:** Antivirus que prediuen la conducta de l'atac abans que s'hagi produït.
- **Resposta Automàtica:** Aïllament instantani d'equips afectats sense intervenció humana.

</div>

</div>

## Model Zero Trust: "Mai Confiïs, Verifica Sempre"

<p class="md-kicker">PARADIGMA ACTUAL</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### Principis del Model

Ja no n'hi ha prou amb estar "dins" de la xarxa corporativa o darrere d'un firewall.

- Cada usuari, dispositiu i petició s'ha d'**autenticar i autoritzar constantment**.
- **Privilegi Mínim:** Accés restringit només al que és estrictament necessari per a la tasca.

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### Importància en Credencials Robades

Si un atacant aconsegueix una contrasenya, Zero Trust atura la danyosa expansió lateral perquè el comportament o el dispositiu no coincideixen amb el patró habitual.

</div>

</div>

## Evolució del Ransomware: Extorsió Múltiple

<p class="md-kicker">AMENACES DE RANSOMWARE</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#EF4444" markdown="1">

### Doble / Triple Extorsió

Els cibercriminals no només xifren les dades, sinó que:

- Amenacen amb publicar informació privada o confidencial.
- Contacten directament amb els clients de l'empresa per augmentar la pressió.

</div>

<div class="md-card" style="--card:#F59E0B" markdown="1">

### Ransomware-as-a-Service (RaaS)

Model de negoci on es lloguen "kits" de malware ja preparats. Permet cometre ciberdelictes complexos sense necessitat de tenir coneixements de programació.

</div>

</div>

## Diapositiva 10

**COMPARATIVA TECNOLÒGICA**

**Evolució de les Eines de Seguretat Activa**

| Eina / Model | Mètode Principal | Focus de Protecció | Nivell d'Eficàcia Actual |
|---|---|---|---|
| Antivirus Clàssic | Signatures / Diccionari de virus | Fitxers locals en disc | Baix (Incapaç davant virus polimòrfics) |
| EDR / XDR | Anàlisi heurístic i comportamental | Endpoints i processos actius | Alt (Detecta accions sospitoses) |
| SIEM | Correlació centralitzada de logs | Tota la infraestructura de xarxa | Molt Alt (Detecta atacs complexos) |
| Zero Trust | Verificació continua i privilegis mínims | Identitats, accessos i dades | Màxim (Mitiga el robatori de credencials) |

## Cadena Integria de Protecció Activa

<p class="md-kicker">SÍNTESI TECNOLÒGICA</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### Endpoint

EDR amb emulació en **Sandbox** i anàlisi heurístic contra virus polimòrfics.

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### Xarxa i Logs

Supervisió centralitzada amb **SIEM** i protecció per **Firewall**.

</div>

<div class="md-card" style="--card:#8B5CF6" markdown="1">

### Accés i Dades

Arquitectura **Zero Trust** i backups immutables automatitzats contra Ransomware.

</div>

</div>

## Resum d'Estudi - Seguretat Activa 4

Davant de malware mutant i atacs basats en IA, la seguretat activa moderna exigeix combinar la monitoratge d'heurística i **Sandboxing**, la visió global d'un **SIEM**, la verificació contínua de **Zero Trust** i la resiliència del **Backup**.
