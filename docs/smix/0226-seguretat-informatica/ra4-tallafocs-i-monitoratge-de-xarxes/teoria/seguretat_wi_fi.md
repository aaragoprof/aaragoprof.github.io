---
description: Evolució dels protocols de seguretat sense fil des de WEP fins a WPA3.
pdf: ""
---

# Seguretat en xarxes sense fil (Wi-Fi)

## Evolució dels protocols

### WEP (Wired Equivalent Privacy)
- **Estat:** Obsolescent / Insegur.
- **Problema:** Clau estàtica i xifratge feble (RC4). Es pot trencar en pocs minuts capturant paquets.

### WPA (Wi-Fi Protected Access)
- **Estat:** Solució d'emergència (2003).
- **Característiques:** Va introduir **TKIP** per canviar la clau per cada paquet, però mantenia codi base de WEP.

### WPA2
- **Estat:** Estàndard estès (2004).
- **Característiques:** Implementa xifratge fort **AES** (Advanced Encryption Standard).
- **Vulnerabilitat:** Atac **KRACK** (2017) durant el procés de negociació (*handshake*).

### WPA3
- **Estat:** Estàndard actual i recomanat.
- **Millores:**
  - **SAE (Simultaneous Authentication of Equals):** Intercanvi de claus robust contra l'escolta.
  - **Xifratge individualitzat:** Impedeix desxifrar tràfic antic d'altres usuaris tot i conèixer la contrasenya de la xarxa.
  - **Protecció contra atacs de diccionari:** Bloqueja intents de força bruta.