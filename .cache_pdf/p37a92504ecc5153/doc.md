# Alarmes i Gestió d'Incidències

<p class="md-kicker">MÒDUL DE SEGURETAT INFORMÀTICA (PART 3)</p>

Material d'estudi: Detecció i Prevenció d'Intrusions (IDS vs IPS), Canals de Detecció, Resolució de Crisi i Documentació Retroalimentada

## IDS i IPS: Monitoratge i Resposta Activa

<p class="md-kicker">MONITORATGE DE SEGURETAT</p>

Dins del marc de la seguretat activa, els sistemes de vigilància de xarxa i equips s'especialitzen en dues tasques complementàries: **detectar** i **prevenir** accions no autoritzades.

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### IDS (Intrusion Detection System)

Sistema de Detecció d'Intrusions. Vigila la xarxa o l'equip per identificar activitats sospitoses o violacions de polítiques. **Acció: Observa i avisa.**

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### IPS (Intrusion Prevention System)

Evolució natural de l'IDS. No només detecta sinó que intervé de manera immediata per tallar l'amenaça. **Acció: Observa i actua.**

</div>

</div>

## Analogia: Firewall, IDS i IPS a la Protecció Físic

<p class="md-kicker">EXPLICACIÓ DIDÀCTICA</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### Tallafoc (Firewall)

És la **porta blindada** de casa teva. Controla qui pot entrar o sortir segons les claus (regles de xarxa) establertes.

</div>

<div class="md-card" style="--card:#F97316" markdown="1">

### IDS (Alarma)

És l'**alarma amb sensors** de moviment. Sona i t'avisa si algú ha forçat una finestra o aconseguit entrar a la casa.

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### IPS (Vigilant Actiu)

És el **vigilant de seguretat presencial**. En veure l'intrús, el deté immediatament abans que pugui tocar o robar res.

</div>

</div>

## Com es Detecta una Incidència de Seguretat?

<p class="md-kicker">IDENTIFICACIÓ DE PROBLEMES</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### 1. Alarma Automàtica del Sistema

Notificació directa generada per alguna de les eines de seguretat instal·lades:

- Alertes de l'antivirus o programes EDR.
- Notificacions del detector d'intrusos (IDS/IPS).
- Bloquejos i avisos del tallafoc (Firewall).

</div>

<div class="md-card" style="--card:#F59E0B" markdown="1">

### 2. Comportament Anòmal del Sistema

L'usuari o administrador nota indicis estranys en l'ús diari de l'equip.

- Aparició o desaparició de fitxers de cop i volta.
- Lentitud extrema del disc o CPU sense estar fent tasques intenses.
- Fallades o tancaments inesperats de programes.

</div>

</div>

## Indicis de Comportament Anòmal a la Màquina

<p class="md-kicker">SIMPTOMATOLOGIA D'INFECCIÓ</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#EF4444" markdown="1">

### Alteració de Fitxers

Fitxers o carpetes que s'esborren soles, o aparició d'arxius desconeguts en ubicacions del sistema.

</div>

<div class="md-card" style="--card:#F59E0B" markdown="1">

### Degradació de Rendiment

El disc dur treballa de forma constant o la CPU se satura sense que l'usuari estigui executant tasques feixugues.

</div>

<div class="md-card" style="--card:#8B5CF6" markdown="1">

### Inestabilitat i Tancaments

Tancaments inesperats d'aplicacions, reinicis automàtics de l'equip o bloquejos permanents de la pantalla.

</div>

</div>

## Com Actuar en Detectar una Incidència?

<p class="md-kicker">PROTOCOL D'ACTUACIÓ</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#16A34A" markdown="1">

### Opció A: Existeix Pla de Contingència

Si l'empresa disposa d'un pla de contingència i la incidència està prevista:

<div class="md-callout" style="--card:#16A34A" markdown="1">

**Seguir estrictament el procediment pas a pas indicat en el document organitzatiu per pal·liar efectes.**

</div>

</div>

<div class="md-card" style="--card:#0284C7" markdown="1">

### Opció B: Sense Pla o Incidència Nova

Si no hi ha pla o la incidència és imprevista:

Cenyir-se a les **instruccions i documentació tècnica** subministrada pels mateixos programes de seguretat que han donat l'alarma.

</div>

</div>

## Documentació de les Incidències Resoltes

<p class="md-kicker">MILLORA CONTÍNUA</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### Obligatorietat de Documentar

Un cop detectada i resolta la incidència de seguretat, és imprescindible realitzar un **informe detallat de l'incident**.

- Registrar la causa de la fallada o atac.
- Anotar les accions realitzades per a la seva resolució.

</div>

<div class="md-card" style="--card:#8B5CF6" markdown="1">

### Actualització del Pla de Contingència

Si la incidència no constava al pla perquè no estava prevista, **convindrà incloure-hi el nou protocol immediatament** per estar preparats davant d'esdeveniments futurs.

</div>

</div>

## El Cicle de Vida de la Gestió d'Incidències

<p class="md-kicker">PROCÉS ESTRUCTURAT</p>

<div class="md-callout" style="--card:#0284C7" markdown="1">

**1. Detecció:** Recepció d'alerta d'eines (IDS/Antivirus) o identificació d'anomalies en el sistema.

</div>

<div class="md-callout" style="--card:#EAB308" markdown="1">

**2. Diagnòstic i Aïllament:** Identificació de l'origen de l'atac i contenció per pal·liar els efectes immediats.

</div>

<div class="md-callout" style="--card:#16A34A" markdown="1">

**3. Resolució:** Aplicació del pla de contingència o de les instruccions tècniques del software.

</div>

<div class="md-callout" style="--card:#A855F7" markdown="1">

**4. Documentació i Retroalimentació:** Registre de l'incident i actualització del pla per a incidències meva futures.

</div>

## Diapositiva 9

**COMPARATIVA TECNOLÒGICA**

**Firewall vs. IDS vs. IPS**

| Eina / Sistema | Funció Principal | Acció Davant l'Amenaça | Analogia Física |
|---|---|---|---|
| Tallafoc (Firewall) | Filtratge de ports i trànsit de xarxa segons regles | Bloqueja o permet l'accés d'entrada/sortida | Porta blindada de l'edifici |
| IDS (Detecció) | Vigilància i anàlisi de patrons d'intrusió | Genera una alerta als administradors | Alarma de seguretat amb sensors |
| IPS (Prevenció) | Vigilància contínua i tall de comunicacions | Bloqueja i deté l'atac en temps real | Vigilant de seguretat actiu |

## Per què cal Documentar Sempre les Incidències?

<p class="md-kicker">GESTIÓ DEL CONEIXEMENT</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### Historial Tecnològic

Permet crear una base de coneixement per resoldre amb més velocitat futurs atacs similars.

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### Enfortiment del Pla

Transforma el pla de contingència en un document viu que evoluciona amb les noves amenaces.

</div>

<div class="md-card" style="--card:#8B5CF6" markdown="1">

### Compliment Normatiu

Demostra la diligència deguda en l'administració de sistemes davant d'auditories de seguretat.

</div>

</div>

## Cadena de Gestió d'Alarmes

<p class="md-kicker">SÍNTESI D'ESTUDI</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### Detecció Precoç

Combinació de sensors automàtics (IDS/IPS) i observació de la conducta de l'equip.

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### Resolució Guiada

Seguiment del pla de contingència o documentació del software d'alarma.

</div>

<div class="md-card" style="--card:#8B5CF6" markdown="1">

### Registre Post-Mortem

Documentar l'incident i actualitzar el pla organitzatiu.

</div>

</div>

## Resum d'Estudi - Seguretat Activa 3

Una estratègia eficaç de gestió d'alarmes requereix diferir entre observació (**IDS**) i acció immediata (**IPS**), detectar anomalies ràpidament, actuar segons el **pla de contingència** i registrar cada esdeveniment per enfortir el sistema.
