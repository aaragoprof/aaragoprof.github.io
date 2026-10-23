---
description: Xifratge en xarxes de cable, analítica de xarxa UEBA/NDR i atacs de sniffing.
pdf: ""
---

# Seguretat en xarxes de cable i monitoratge avançat

## El xifratge com a nova protecció física
Ja no es considera que el cable sigui un medi segur; s'assumeix que el tràfic pot ser interceptat (*sniffing*).

- **TLS 1.3:** Xifratge extrem a extrem actual.
- **MACsec (IEEE 802.1AE):** Xifratge a capa 2 que protegeix el tràfic físic directament entre switches.
- **Segmentació Dinàmica (Zero Trust):** L'accés als recursos depèn de la identitat autenticada de l'usuari i no de la presa física de paret.

## Monitoratge modern
- **UEBA (User and Entity Behavior Analytics):** Analítica basada en comportament d'usuaris per detectar anomalies.
- **Observabilitat Full-Stack:** Integració del tràfic de xarxa, aplicacions i núvol en un sol panell.
- **NDR (Network Detection and Response):** Ús d'IA per detectar i respondre a atacs en temps real sobre el tràfic.

## Sniffing il·legítim
- **Atacs Man-in-the-Middle (MitM):** Tècniques com *ARP Spoofing* per interposar-se en el tràfic.
- **Dispositius Drop-in:** Petits equips físics (com Raspberry Pi) connectats en secret a la xarxa per capturar paquets.
- **Solució:** Configuració de **Port Security** als switches per bloquejar connexions de MACs no autoritzades.