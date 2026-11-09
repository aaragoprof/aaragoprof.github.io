# Seguretat en Xarxes de Cable i Control de Monitoratge

## Diapositiva 1

![Imatge 1](@@IMG@@/img-001.jpg){ loading=lazy }

![Imatge 2](@@IMG@@/img-002.png){ loading=lazy }

**Seguretat en Xarxes de Cable i Monitoratge**

**MÒDUL DE SEGURETAT INFORMÀTICA I XARXES**

Material d'estudi: Xifratge Ethernet (MACsec, TLS 1.3), Protecció contra Sniffing i Monitoratge d'Nova Generació (UEBA, NDR, Full-Stack)

## Diapositiva 2

**NOU PARADIGMA DE XARXA**

**Informació en la Xarxa: "El Xifratge és el Nou Cable"**

En les xarxes corporatives modernes ja no es pot assumir que el cable físic és un medi segur o privat. S'assumeix des del primer moment que un tercer pot estar intentant escoltar el trànsit (*sniffing*).

**TLS 1.3 (Extrem a Extrem)**

**MACsec (IEEE 802.1AE)**

**Segmentació Dinàmica**

Estàndard actual de xifratge d'aplicació i transport que codifica les comunicacions directament entre client i servidor.

Xifratge a Nivell de Enllaç (Capa 2) directament entre switches per protegir el cable físic de punxades i atacs.

Divisió basades en la identitat de l'usuari (Zero Trust), no només en ports físics o rosetes de paret.

## Diapositiva 3

**SEGURETAT DE MAQUINARI**

**Xifratge a Capa 2: MACsec (IEEE 802.1AE)**

**Concepte de MACsec**

**Avantatge en Infraestructures**

Protocol d'alta seguretat corporativa que xifra **totes les trames Ethernet** directament en el cable físic entre commutadors (switches) o entre equip i switch.

Garanteix que el trànsit no xifrat en capes superiors (com protocols antics de gestió) quedi completament protegit mentre circula pels cables de l'edifici.

• Protegeix contra punxades físiques del cableat.

• Impedeix la modificació o injecció de trames a la xarxa local.

## Diapositiva 4

**CONTROL D'ACCÉS**

**Segmentació Dinàmica: Més enllà dels Ports Físics**

**Model Tradicional (Vulnerable)**

**Model Dinàmic (Zero Trust)**

Qualsevol equip que es connectava a una roseta de paret obtenia accés automàtic a la VLAN d'aquella zona o departament.

El cable o port de paret per si sol **no dona accés a cap recurs** fins que l'usuari i l'equip s'autentiquen correctament.

• La xarxa assigna polítiques i permisos en funció del rol de l'usuari.

• Si l'usuari es mou de despatx, les seves polítiques viatgen amb ell.

## Diapositiva 5

**VECTORS D'ATAC EN CABLE**

**Sniffing Il·legítim: L'Amenaça Invisible al Cable**

L'*sniffing* consisteix a capturar paquets de dades que circulen per la xarxa. Encara que el medi sigui cablejat, existeixen tècniques sofisticades per interceptar la informació.

**Atacs Man-in-the-Middle (MitM)**

**Dispositius "Drop-in"**

**Port Security (Solució)**

Tècniques com l'**ARP Spoofing** enganyen els equips perquè tot el tràfic del cable passi per l'ordinador de l'atacant abans d'arribar al router.

Petits equips fets a mida (com Raspberry Pi camuflades) connectats físicament a cables o ports de paret per capturar dades de forma remota.

Configuració dels switches per bloquejar automàticament qualsevol port si detecten una adreça MAC no autoritzada.

## Diapositiva 6

**DEFENSA A CONMUTADORS**

**Mitigació de Hardware: Port Security i Control MAC**

**Com funciona el Port Security?**

**Prevenció d'ARP Spoofing**

S'estableix un límit i un registre d'adreces MAC permeses per cada port físic del switch.

L'ús de **Dynamic ARP Inspection (DAI)** i **DHCP Snooping** valida les taules de coordinació IP-MAC per evitar l'envenenament de taules ARP i els atacs Man-in-the-Middle.

• **MACs Estàtiques o Sticky:** El switch aprèn la MAC de l'equip legítim.

• **Violació de Seguretat:** Si un usuari desconnecta l'ordinador i hi punxa un dispositiu *drop-in*, el port es deshabilita a l'instant (mode *shutdown*).

## Diapositiva 7

**EVOLUCIÓ DEL MONITORATGE**

**Monitoratge de Xarxes: Del "Què Passa" al "Què Passarà"**

**Monitoratge Tradicional (Reactivitat)**

**Monitoratge Modern (Predicció i Comportament)**

Comprovar únicament si un servidor respon (Ping), si un port està obert o si l'amplada de banda s'ha saturat. Reacciona *després* de la caiguda.

Utilitza algoritmes intel·ligents per analitzar patrons de trànsit i anomalia d'usuaris, identificant amenaces complexes abans que causin un dany greu.

## Diapositiva 8

**TECNOLOGIES AVANÇADES**

**Tres Pilars del Monitoratge Avançat**

**UEBA**

**Observabilitat Full-Stack**

**NDR**

**User and Entity Behavior Analytics:** Aprèn el patró normal d'un usuari per alertar davant d'anomalies.

Integra el rendiment del xarxa, aplicacions i infraestructura en el núvol en un únic panell centralitzat.

**Network Detection and Response:** Utilitza IA per detectar i aturar patrons d'atac en temps real al cable.

## Diapositiva 9

**ANÀLISI DE COMPORTAMENT**

**UEBA: Detecció d'Anomalies d'Usuari**

**Com Funciona l'Aprenentatge d'Hàbits?**

**Exemple d'Alerta Automàtica**

El sistema monitoritza contínuament la rutina habitual de cada treballador (horaris de treball, volums de transferència habituals, servidors als quals s'accedeix).

**"Un perfil d'administratiu que normalment genera 20 MB diaris comença a extreure 50 GB de dades a les 3:00 AM cap a una IP externa."**

El sistema bloqueja l'usuari i notifica l'equip de seguretat immediatament.

## Diapositiva 10

**DETECCIÓ INTEL·LIGENT**

**NDR: Resposta Automàtica a la Xarxa amb IA**

**Inspecció de Trànsit Profund**

**Resposta Immediata**

L'NDR analitza el trànsit que circula pels cables corporatius (incloent meta-dades de metratges xifrats) a la cerca de moviments laterals de malware.

En detectar una amenaça en temps real:

• Comunica l'ordre al switch per desconnectar el port afectat.

• Aïlla l'amenaça sense esperar l'actuació manual d'un tècnic.

## Diapositiva 11

**SÍNTESI TECNOLÒGICA**

**Eines de Seguretat i Monitoratge en Xarxes de Cable**

| Tecnologia | Nivell d'Actuació | Funció Clau | Protecció Principal |
|---|---|---|---|
| MACsec (802.1AE) | Capa 2 (Enllaç) | Xifratge del cable entre switches | Punxades físiques del cableat |
| Port Security | Hardware / Switch | Filtrat d'adreces MAC per port | Dispositius drop-in i equips no autoritzats |
| UEBA | Anàlisi de Dades | Aprenentatge d'hàbits d'usuari | Fugides de dades i comptabilitats robades |
| NDR | Xarxa / IA | Detecció de moviments laterals | Atacs complexos en temps real |

## Diapositiva 12

![Imatge 3](@@IMG@@/img-003.jpg){ loading=lazy }

![Imatge 4](@@IMG@@/img-004.png){ loading=lazy }

**Resum d'Estudi - Xarxes de Cable i Monitoratge**

La seguretat en xarxes cablejades combina el xifratge de medi (**MACsec**, **TLS 1.3**), el control d'accés a hardware (**Port Security**) i la intel·ligència predictiva (**UEBA**, **NDR**) per convertir un cable abans vulnerable en un entorn completament protegit.
