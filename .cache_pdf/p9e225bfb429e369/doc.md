# Seguretat en Xarxes de Cable i Monitoratge

<p class="md-kicker">MÒDUL DE SEGURETAT INFORMÀTICA I XARXES</p>

Material d'estudi: Xifratge Ethernet (MACsec, TLS 1.3), Protecció contra Sniffing i Monitoratge d'Nova Generació (UEBA, NDR, Full-Stack)

## Informació en la Xarxa: "El Xifratge és el Nou Cable"

<p class="md-kicker">NOU PARADIGMA DE XARXA</p>

En les xarxes corporatives modernes ja no es pot assumir que el cable físic és un medi segur o privat. S'assumeix des del primer moment que un tercer pot estar intentant escoltar el trànsit (*sniffing*).

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### TLS 1.3 (Extrem a Extrem)

Estàndard actual de xifratge d'aplicació i transport que codifica les comunicacions directament entre client i servidor.

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### MACsec (IEEE 802.1AE)

Xifratge a Nivell de Enllaç (Capa 2) directament entre switches per protegir el cable físic de punxades i atacs.

</div>

<div class="md-card" style="--card:#8B5CF6" markdown="1">

### Segmentació Dinàmica

Divisió basades en la identitat de l'usuari (Zero Trust), no només en ports físics o rosetes de paret.

</div>

</div>

## Xifratge a Capa 2: MACsec (IEEE 802.1AE)

<p class="md-kicker">SEGURETAT DE MAQUINARI</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#16A34A" markdown="1">

### Concepte de MACsec

Protocol d'alta seguretat corporativa que xifra **totes les trames Ethernet** directament en el cable físic entre commutadors (switches) o entre equip i switch.

- Protegeix contra punxades físiques del cableat.
- Impedeix la modificació o injecció de trames a la xarxa local.

</div>

<div class="md-card" style="--card:#0284C7" markdown="1">

### Avantatge en Infraestructures

Garanteix que el trànsit no xifrat en capes superiors (com protocols antics de gestió) quedi completament protegit mentre circula pels cables de l'edifici.

</div>

</div>

## Segmentació Dinàmica: Més enllà dels Ports Físics

<p class="md-kicker">CONTROL D'ACCÉS</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#EF4444" markdown="1">

### Model Tradicional (Vulnerable)

Qualsevol equip que es connectava a una roseta de paret obtenia accés automàtic a la VLAN d'aquella zona o departament.

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### Model Dinàmic (Zero Trust)

El cable o port de paret per si sol **no dona accés a cap recurs** fins que l'usuari i l'equip s'autentiquen correctament.

- La xarxa assigna polítiques i permisos en funció del rol de l'usuari.
- Si l'usuari es mou de despatx, les seves polítiques viatgen amb ell.

</div>

</div>

## Sniffing Il·legítim: L'Amenaça Invisible al Cable

<p class="md-kicker">VECTORS D'ATAC EN CABLE</p>

L'*sniffing* consisteix a capturar paquets de dades que circulen per la xarxa. Encara que el medi sigui cablejat, existeixen tècniques sofisticades per interceptar la informació.

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#EF4444" markdown="1">

### Atacs Man-in-the-Middle (MitM)

Tècniques com l'**ARP Spoofing** enganyen els equips perquè tot el tràfic del cable passi per l'ordinador de l'atacant abans d'arribar al router.

</div>

<div class="md-card" style="--card:#F59E0B" markdown="1">

### Dispositius "Drop-in"

Petits equips fets a mida (com Raspberry Pi camuflades) connectats físicament a cables o ports de paret per capturar dades de forma remota.

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### Port Security (Solució)

Configuració dels switches per bloquejar automàticament qualsevol port si detecten una adreça MAC no autoritzada.

</div>

</div>

## Mitigació de Hardware: Port Security i Control MAC

<p class="md-kicker">DEFENSA A CONMUTADORS</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### Com funciona el Port Security?

S'estableix un límit i un registre d'adreces MAC permeses per cada port físic del switch.

- **MACs Estàtiques o Sticky:** El switch aprèn la MAC de l'equip legítim.
- **Violació de Seguretat:** Si un usuari desconnecta l'ordinador i hi punxa un dispositiu *drop-in*, el port es deshabilita a l'instant (mode *shutdown*).

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### Prevenció d'ARP Spoofing

L'ús de **Dynamic ARP Inspection (DAI)** i **DHCP Snooping** valida les taules de coordinació IP-MAC per evitar l'envenenament de taules ARP i els atacs Man-in-the-Middle.

</div>

</div>

## Monitoratge de Xarxes: Del "Què Passa" al "Què Passarà"

<p class="md-kicker">EVOLUCIÓ DEL MONITORATGE</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#64748B" markdown="1">

### Monitoratge Tradicional (Reactivitat)

Comprovar únicament si un servidor respon (Ping), si un port està obert o si l'amplada de banda s'ha saturat. Reacciona *després* de la caiguda.

</div>

<div class="md-card" style="--card:#0284C7" markdown="1">

### Monitoratge Modern (Predicció i Comportament)

Utilitza algoritmes intel·ligents per analitzar patrons de trànsit i anomalia d'usuaris, identificant amenaces complexes abans que causin un dany greu.

</div>

</div>

## Tres Pilars del Monitoratge Avançat

<p class="md-kicker">TECNOLOGIES AVANÇADES</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### UEBA

**User and Entity Behavior Analytics:** Aprèn el patró normal d'un usuari per alertar davant d'anomalies.

</div>

<div class="md-card" style="--card:#8B5CF6" markdown="1">

### Observabilitat Full-Stack

Integra el rendiment del xarxa, aplicacions i infraestructura en el núvol en un únic panell centralitzat.

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### NDR

**Network Detection and Response:** Utilitza IA per detectar i aturar patrons d'atac en temps real al cable.

</div>

</div>

## UEBA: Detecció d'Anomalies d'Usuari

<p class="md-kicker">ANÀLISI DE COMPORTAMENT</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### Com Funciona l'Aprenentatge d'Hàbits?

El sistema monitoritza contínuament la rutina habitual de cada treballador (horaris de treball, volums de transferència habituals, servidors als quals s'accedeix).

</div>

<div class="md-card" style="--card:#EF4444" markdown="1">

### Exemple d'Alerta Automàtica

<div class="md-callout" style="--card:#EF4444" markdown="1">

**"Un perfil d'administratiu que normalment genera 20 MB diaris comença a extreure 50 GB de dades a les 3:00 AM cap a una IP externa."**

</div>

El sistema bloqueja l'usuari i notifica l'equip de seguretat immediatament.

</div>

</div>

## NDR: Resposta Automàtica a la Xarxa amb IA

<p class="md-kicker">DETECCIÓ INTEL·LIGENT</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#16A34A" markdown="1">

### Inspecció de Trànsit Profund

L'NDR analitza el trànsit que circula pels cables corporatius (incloent meta-dades de metratges xifrats) a la cerca de moviments laterals de malware.

</div>

<div class="md-card" style="--card:#0284C7" markdown="1">

### Resposta Immediata

En detectar una amenaça en temps real:

- Comunica l'ordre al switch per desconnectar el port afectat.
- Aïlla l'amenaça sense esperar l'actuació manual d'un tècnic.

</div>

</div>

## Diapositiva 11

**SÍNTESI TECNOLÒGICA**

**Eines de Seguretat i Monitoratge en Xarxes de Cable**

| Tecnologia | Nivell d'Actuació | Funció Clau | Protecció Principal |
|---|---|---|---|
| MACsec (802.1AE) | Capa 2 (Enllaç) | Xifratge del cable entre switches | Punxades físiques del cableat |
| Port Security | Hardware / Switch | Filtrat d'adreces MAC per port | Dispositius drop-in i equips no autoritzats |
| UEBA | Anàlisi de Dades | Aprenentatge d'hàbits d'usuari | Fugides de dades i comptabilitats robades |
| NDR | Xarxa / IA | Detecció de moviments laterals | Atacs complexos en temps real |

## Resum d'Estudi - Xarxes de Cable i Monitoratge

La seguretat en xarxes cablejades combina el xifratge de medi (**MACsec**, **TLS 1.3**), el control d'accés a hardware (**Port Security**) i la intel·ligència predictiva (**UEBA**, **NDR**) per convertir un cable abans vulnerable en un entorn completament protegit.
