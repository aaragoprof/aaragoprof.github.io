# Estructura de les Xarxes de Dades

<p class="md-kicker">RESULTAT D'APRENENTATGE 1</p>

Arquitectures, Medis de Transmissió, Dispositius, Topologies i Sistemes de Numeració Binària

## Components Principals d'una Xarxa

<p class="md-kicker">FONAMENTS DE XARXA</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### Terminals (Hosts)

Ordinadors, servidors i dispositius mòbils que actuen com a emissors o receptors de dades.

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### Medis de Transmissió

Suport físic (cablezat o d'aire) que transporta els senyals elèctrics, òptics o d'ones.

</div>

<div class="md-card" style="--card:#EAB308" markdown="1">

### Dispositius d'Enllaç

Equips com switches o routers que interconnecten, amplifiquen i encaminen les dades.

</div>

<div class="md-card" style="--card:#8B5CF6" markdown="1">

### Programari i Protocols

Sistemes operatius, adaptadors de xarxa i regles que regulen la comunicació.

</div>

</div>

## Medis de Transmissió

<p class="md-kicker">CAPA FÍSICA</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### Medis Guiats (Confinats)

**Cable de Coure:** Utilitzat en distàncies curtes i mitjanes en xarxes locals (UTP/STP).

**Fibra Òptica:** Fil de material transparent que transmet informació mitjançant polsos de llum a grans distàncies.

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### Medis No Guiats (Sense Fil)

**Ones de Ràdio:** Omnidireccionals, no requereixen visió directa (Wi-Fi, cel·lular).

**Infrarojos:** Enllaços directes a molt curta distància sense obstacles.

**Microones:** Comunicació direccional d'alta freqüència (Bluetooth, enllaços per satèl·lit).

</div>

</div>

## Classificació de la Transmissió

<p class="md-kicker">FLUX DE COMUNICACIÓ</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### Punt a Punt

Enllaç directe compartit exclusivament per dos dispositius destinats.

</div>

<div class="md-card" style="--card:#0284C7" markdown="1">

### Multipunt

Un sol medi de transmissió compartit simultàniament per diversos dispositius.

</div>

<div class="md-card" style="--card:#EAB308" markdown="1">

### Símplex

La informació flueix estrictament en un sol sentit (ex. radiodifusió).

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### Dúplex

La informació pot transmetre's en ambdós sentits entre els terminals.

</div>

</div>

## Dispositius d'Interconnexió

<p class="md-kicker">HARDWARE DE XARXA</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#64748B" markdown="1">

**Repetidor**

Amplifica i regenera el senyal primitiu abans que es degradi.

</div>

<div class="md-card" style="--card:#64748B" markdown="1">

**Hub (Concentrador)**

Reenvia tot el senyal rebut a totes les seves interfícies sense filtrar.

</div>

<div class="md-card" style="--card:#0284C7" markdown="1">

**Switch (Commutador)**

Interconnecta equips en una LAN dirigint la informació només al destí.

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

**Router (Encaminador)**

Connecta xarxes diferents i tria la millor ruta per enviar els paquets.

</div>

</div>

## Diapositiva 6

**ESCALA DE XARXA**

**Classificació per Àmbit Geogràfic**

| Tipus | Nom Complet | Abast i Característiques |
|---|---|---|
| PAN | Personal Area Network | Pocs metres. Connecta dispositius personals (ex. auriculars Bluetooth). |
| LAN / WLAN | Local Area Network (Wireless) | Oficines o llars. Alta velocitat, permet compartir fitxers i impressores. |
| MAN / WMAN | Metropolitan Area Network | Abasta una ciutat o campus universitari interconnectant diverses LANs. |
| WAN | Wide Area Network | Grans distàncies geogràfiques (països, continents o global com Internet). |

## Topologies de Xarxa

<p class="md-kicker">ESTRUCTURA FÍSICA I LÒGICA</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### Bus & Anell

**Bus:** Medi compartit únic. 
 **Anell:** Connexions punt a punt tancades en un cercle.

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### Estrella & Malla

**Estrella:** Tots els nodes van al Switch central. 
 **Malla:** Múltiples camins redundants.

</div>

<div class="md-card" style="--card:#EAB308" markdown="1">

### Jeràrquica (Arbre)

Organitzada en 3 capes: 
 • **Core:** Encaminament d'alta velocitat. 
 • **Distribució:** Polítiques i routing. 
 • **Accés:** Connexió directa de terminals.

</div>

</div>

## Tecnologies i Relacions de Xarxa

<p class="md-kicker">MODEL DE COMUNICACIÓ</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### Difusió vs Punt a Punt

**Broadcast:** El paquet s'envia a tots els nodes de la xarxa.

**Multicast:** Envia la informació només a un grup definit.

**Punt a Punt:** El paquet passa per equips intermedis fins al destí.

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### Client-Servidor vs P2P

**Client-Servidor:** Un servidor centralitzat ofereix recursos que els clients sol·liciten.

**Peer-to-Peer (P2P):** Tots els equips actuen simultàniament com a clients i servidors.

</div>

</div>

## Arquitectura i Elements d'un Protocol

<p class="md-kicker">ESTANDARDITZACIÓ</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### Arquitectura per Capes

La comunicació es divideix en nivells on cada capa ofereix serveis a la superior. Ambdós equips han de compartir el mateix protocol en el mateix nivell.

</div>

<div class="md-card" style="--card:#8B5CF6" markdown="1">

### Trets Fundamentals del Protocol

**Sintaxi:** Estrutura i format dels blocs de dades.

**Semàntica:** Informació de control i coordinació d'errors.

**Temporització:** Seqüència dels missatges i adaptació de velocitats.

</div>

</div>

## Sistemes de Numeració Posicional

<p class="md-kicker">REPRESENTACIÓ DIGITAL</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#EAB308" markdown="1">

### Principi Posicional

En exhaurir els símbols d'una columna, s'afegeix una unitat a la d'esquerra (unitat d'ordre superior) i la columna actual torna a 0.

</div>

<div class="md-card" style="--card:#0284C7" markdown="1">

### Base 2 (Sistema Binari)

En binari només existeixen dos símbols (0 i 1). Els canvis de columna es produeixen ràpidament:

<div class="md-callout" markdown="1">

0 (0d) → 1 (1d) → 10 (2d) → 11 (3d) → 100 (4d)

</div>

</div>

</div>

## Conversió de Decimal a Binari (Mètode de l'Octet)

<p class="md-kicker">MÈTODE PRÀCTIC DE XARXES</p>

Taula de valors de les 8 potències de 2 d'un octet (8 bits):

| 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
|---|---|---|---|---|---|---|---|
| 1 | 0 | 1 | 0 | 1 | 0 | 0 | 0 |

<div class="md-callout" style="--card:#0284C7" markdown="1">

**Exemple amb el número 168:** 
 168 ≥ 128 → **1** (resten 40) | 40 &lt; 64 → **0** | 40 ≥ 32 → **1** (resten 8) | 8 &lt; 16 → **0** | 8 ≥ 8 → **1** (resten 0) → Resta de caselles en **0**. 
 **Resultat Binari: 10101000**

</div>

## Diapositiva 12

**Conversió de Binari a Decimal**

S'assignen els bits a la taula de l'octet i es sumen exclusivament els valors de les caselles que tinguin un **1**:

<div class="md-card" markdown="1">

Binari: **10010100** → 128 + 16 + 4 = **148 Decimal**

</div>
