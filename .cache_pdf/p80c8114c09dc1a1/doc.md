# IDS, IPS i Gestió d'Incidències

## Diapositiva 1

![Imatge 1](@@IMG@@/img-001.jpg){ loading=lazy }

![Imatge 2](@@IMG@@/img-002.png){ loading=lazy }

**Alarmes i Gestió d'Incidències**

**MÒDUL DE SEGURETAT INFORMÀTICA (PART 3)**

Material d'estudi: Detecció i Prevenció d'Intrusions (IDS vs IPS), Canals de Detecció, Resolució de Crisi i Documentació Retroalimentada

## Diapositiva 2

**MONITORATGE DE SEGURETAT**

**IDS i IPS: Monitoratge i Resposta Activa**

Dins del marc de la seguretat activa, els sistemes de vigilància de xarxa i equips s'especialitzen en dues tasques complementàries: **detectar** i **prevenir** accions no autoritzades.

**IDS (Intrusion Detection System)**

**IPS (Intrusion Prevention System)**

Sistema de Detecció d'Intrusions. Vigila la xarxa o l'equip per identificar activitats sospitoses o violacions de polítiques. **Acció: Observa i avisa.**

Evolució natural de l'IDS. No només detecta sinó que intervé de manera immediata per tallar l'amenaça. **Acció: Observa i actua.**

## Diapositiva 3

**EXPLICACIÓ DIDÀCTICA**

**Analogia: Firewall, IDS i IPS a la Protecció Físic**

**Tallafoc (Firewall)**

**IDS (Alarma)**

**IPS (Vigilant Actiu)**

És la **porta blindada** de casa teva. Controla qui pot entrar o sortir segons les claus (regles de xarxa) establertes.

És l'**alarma amb sensors** de moviment. Sona i t'avisa si algú ha forçat una finestra o aconseguit entrar a la casa.

És el **vigilant de seguretat presencial**. En veure l'intrús, el deté immediatament abans que pugui tocar o robar res.

## Diapositiva 4

**IDENTIFICACIÓ DE PROBLEMES**

**Com es Detecta una Incidència de Seguretat?**

**1. Alarma Automàtica del Sistema**

**2. Comportament Anòmal del Sistema**

Notificació directa generada per alguna de les eines de seguretat instal·lades:

L'usuari o administrador nota indicis estranys en l'ús diari de l'equip.

• Alertes de l'antivirus o programes EDR.

• Notificacions del detector d'intrusos (IDS/IPS).

• Aparició o desaparició de fitxers de cop i volta.

• Lentitud extrema del disc o CPU sense estar fent tasques intenses.

• Bloquejos i avisos del tallafoc (Firewall).

• Fallades o tancaments inesperats de programes.

## Diapositiva 5

**SIMPTOMATOLOGIA D'INFECCIÓ**

**Indicis de Comportament Anòmal a la Màquina**

**Alteració de Fitxers**

**Degradació de Rendiment**

**Inestabilitat i Tancaments**

Fitxers o carpetes que s'esborren soles, o aparició d'arxius desconeguts en ubicacions del sistema.

El disc dur treballa de forma constant o la CPU se satura sense que l'usuari estigui executant tasques feixugues.

Tancaments inesperats d'aplicacions, reinicis automàtics de l'equip o bloquejos permanents de la pantalla.

## Diapositiva 6

**PROTOCOL D'ACTUACIÓ**

**Com Actuar en Detectar una Incidència?**

**Opció A: Existeix Pla de Contingència**

**Opció B: Sense Pla o Incidència Nova**

Si l'empresa disposa d'un pla de contingència i la incidència està prevista:

Si no hi ha pla o la incidència és imprevista:

**Seguir estrictament el procediment pas a pas indicat en el document organitzatiu per pal·liar efectes.**

Cenyir-se a les **instruccions i documentació tècnica** subministrada pels mateixos programes de seguretat que han donat l'alarma.

## Diapositiva 7

**MILLORA CONTÍNUA**

**Documentació de les Incidències Resoltes**

**Obligatorietat de Documentar**

**Actualització del Pla de Contingència**

Un cop detectada i resolta la incidència de seguretat, és imprescindible realitzar un **informe detallat de l'incident**.

Si la incidència no constava al pla perquè no estava prevista, **convindrà incloure-hi el nou protocol immediatament** per estar preparats davant d'esdeveniments futurs.

• Registrar la causa de la fallada o atac.

• Anotar les accions realitzades per a la seva resolució.

## Diapositiva 8

**PROCÉS ESTRUCTURAT**

**El Cicle de Vida de la Gestió d'Incidències**

**1. Detecció:** Recepció d'alerta d'eines (IDS/Antivirus) o identificació d'anomalies en el sistema.

**2. Diagnòstic i Aïllament:** Identificació de l'origen de l'atac i contenció per pal·liar els efectes immediats.

**3. Resolució:** Aplicació del pla de contingència o de les instruccions tècniques del software.

**4. Documentació i Retroalimentació:** Registre de l'incident i actualització del pla per a incidències meva futures.

## Diapositiva 9

**COMPARATIVA TECNOLÒGICA**

**Firewall vs. IDS vs. IPS**

| Eina / Sistema | Funció Principal | Acció Davant l'Amenaça | Analogia Física |
|---|---|---|---|
| Tallafoc (Firewall) | Filtratge de ports i trànsit de xarxa segons regles | Bloqueja o permet l'accés d'entrada/sortida | Porta blindada de l'edifici |
| IDS (Detecció) | Vigilància i anàlisi de patrons d'intrusió | Genera una alerta als administradors | Alarma de seguretat amb sensors |
| IPS (Prevenció) | Vigilància contínua i tall de comunicacions | Bloqueja i deté l'atac en temps real | Vigilant de seguretat actiu |

## Diapositiva 10

**GESTIÓ DEL CONEIXEMENT**

**Per què cal Documentar Sempre les Incidències?**

**Historial Tecnològic**

**Enfortiment del Pla**

**Compliment Normatiu**

Permet crear una base de coneixement per resoldre amb més velocitat futurs atacs similars.

Transforma el pla de contingència en un document viu que evoluciona amb les noves amenaces.

Demostra la diligència deguda en l'administració de sistemes davant d'auditories de seguretat.

## Diapositiva 11

**SÍNTESI D'ESTUDI**

**Cadena de Gestió d'Alarmes**

**Detecció Precoç**

**Resolució Guiada**

**Registre Post-Mortem**

Combinació de sensors automàtics (IDS/IPS) i observació de la conducta de l'equip.

Seguiment del pla de contingència o documentació del software d'alarma.

Documentar l'incident i actualitzar el pla organitzatiu.

## Diapositiva 12

![Imatge 3](@@IMG@@/img-003.jpg){ loading=lazy }

![Imatge 4](@@IMG@@/img-004.png){ loading=lazy }

**Resum d'Estudi - Seguretat Activa 3**

Una estratègia eficaç de gestió d'alarmes requereix diferir entre observació (**IDS**) i acció immediata (**IPS**), detectar anomalies ràpidament, actuar segons el **pla de contingència** i registrar cada esdeveniment per enfortir el sistema.
