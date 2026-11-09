# Seguretat en Xarxes Sense Fil i Mobilitat - Material d'Estudi

## Diapositiva 1

![Imatge 1](@@IMG@@/img-001.jpg){ loading=lazy }

![Imatge 2](@@IMG@@/img-002.png){ loading=lazy }

**Seguretat en Xarxes Sense Fil i Mobilitat**

**MÒDUL DE SEGURETAT INFORMÀTICA I XARXES**

Material d'estudi: Evolució de Protocols Wi-Fi (WEP, WPA, WPA2, WPA3), Algorismes de Xifratge i Protecció davant d'Atacs Moderns

## Diapositiva 2

**CONCEPTE I CONTEXT**

**El Desafiament del Medi Sense Fil**

A diferència de les xarxes cablejades on l'accés requereix connexió física a un connector, les ones de ràdio Wi-Fi es propaguen a l'espai públic. Això fa imprescindible establir protocols de xifratge per garantir la confidencialitat.

**Medi Obert**

**Xifrat de Canal**

**Evolució Tecnològica**

Qualsevol dispositiu a l'abast de les ones pot escoltar el trànsit si no està correctament xifrat.

Mecanismes per codificar les dades transmitides entre el client i l'Punt d'Accés (AP).

Sistemes de seguretat en constant actualització per corregir vulnerabilitats descobertes en protocols antics.

## Diapositiva 3

**ORIGEN HISTÒRIC**

**WEP (Wired Equivalent Privacy): El Primer Protocol**

**Objectiu i Disseny**

**Vulnerabilitat Absoluta**

Creat per oferir a les xarxes sense fil un nivell de seguretat equivalent al d'una xarxa de cable tradicional.

Els atacants van descobrir que, capturant un nombre suficient de paquets de dades, es podia obtenir la clau en pocs minuts.

• **Clau Estàtica:** Utilitzava una mateixa clau que mai no canviava.

**Estat actual: Totalment obsolet i insegur. Prohibit en entorns corporatius.**

• **Algorisme RC4:** Xifratge feble i propens a col·lisions de vector d'inicialització (IV).

## Diapositiva 4

**TRANSICIÓ DE SEGURETAT**

**WPA (2003): El "Pegat" d'Emergència**

**Solució d'Emergència**

**Limitació Tecnològica**

Desenvolupat per la Wi-Fi Alliance per substituir WEP ràpidament sense requerir el canvi del maquinari existent (routers antics).

Tot i que millorava la seguretat de WEP, encara heretava part de la seva estructura base per mantenir la compatibilitat amb dispositius antics, deixant escletxes de seguretat.

**Introducció de TKIP (Temporal Key Integrity Protocol), algorisme que canviava la clau per a cada paquet de dades.**

## Diapositiva 5

**CONSOLIDACIÓ DE SEGURETAT**

**WPA2 (2004): L'Estàndard d'Or**

**Innovació Principal: AES**

**L'Atac KRACK (2017)**

Va ser el protocol dominant durant més de 15 anys. Reemplaça el feble TKIP per l'algorisme de grau militar **AES (Advanced Encryption Standard)** i CCMP.

Descoberta de la vulnerabilitat **KRACK (Key Reinstallation Attacks)**. Els atacants podien intervenir el procés de negociació (handshake) de connexió i desxifrar el trànsit, accelerant la transició cap a WPA3.

• Alta resistència al desxifratge directe.

• Dos modes principals: WPA2-Personal (PSK) i WPA2-Enterprise (802.1X/RADIUS).

## Diapositiva 6

**ESTÀNDARD ACTUAL**

**WPA3 (2018 - Present): La Seguretat Moderna**

**Xifratge Individualitzat**

**Anti Força Bruta**

**Protocol SAE**

Encara que un tercer sàpiga la contrasenya de la xarxa, no pot desxifrar el tràfic enviat prèviament per altres usuaris.

Bloqueja automàticament els intents repetits de provar milers de contrasenyes per minut (atacs de diccionari).

Substitueix la negociació antiga PSK pel mètode **SAE (Simultaneous Authentication of Equals)** molt més resistent.

## Diapositiva 7

**CRIPTOGRAFIA DE CONNEXIÓ**

**Negociació de Clau: PSK (WPA2) vs. SAE (WPA3)**

**PSK (Pre-Shared Key en WPA2)**

**SAE (Simultaneous Auth of Equals en WPA3)**

Negociació en 4 passos (Handshake). Un atacant pot capturar el handshake i intentar desxifrar la contrasenya *offline* mitjançant atacs de força bruta sense estar connectat a la xarxa.

Basat en el protocol Dragonfly (Diffie-Hellman sobre corbes el·líptiques).

• Obliga a interactuar amb l'AP per cada intent de clave.

• Elimina completament els atacs de diccionari fora de línia (offline).

## Diapositiva 8

**PRIVACITAT D'USUARI**

**Xifratge Individualitzat i Privacitat cap Enrere**

En xarxes WPA2 obertes o compartides, tots els usuaris usaven claus que permetien espiar el tràfic del veí de taula.

**Aïllament de Trànsit entre Clients**

Si un atacant esbrina la contrasenya de la xarxa en el futur, **no podrà desxifrar les dades que s'hagin enmagatzemat o capturat prèviament** a l'aire.

**Forward Secrecy (Privacitat Segura)**

**En WPA3:** Es genera una clau de xifratge única per a cada sessió de dispositiu individual.

## Diapositiva 9

**ARQUITECTURA DE XARXA**

**Modes d'Desplegament: Personal (PSK/SAE) vs. Enterprise**

**Mode Personal (WPA3-Personal)**

**Mode Enterprise (WPA3-Enterprise)**

• Ús domèstic o petites oficines.

• Entorns corporatius i universitaris.

• Utilitza una contrasenya única compartida per a tots els usuaris.

• Autenticació individual d'usuaris mitjançant **servidor RADIUS (802.1X)**.

• Utilitza **SAE (128 bits)** per a la connexió inicial segura.

• Opció de xifratge d'alta seguretat de **192 bits** per a entorns governamentals.

## Diapositiva 10

**SÍNTESI D'ESTUDI**

**Taula Comparativa de Protocols de Seguretat Wi-Fi**

| Protocol | Any | Algorisme de Xifratge | Mètode d'Autenticació | Estat de Seguretat Actual |
|---|---|---|---|---|
| WEP | 1997 | RC4 (Clau estàtica) | Clau compartida feble | Totalment Insegur (Desxifrable en minuts) |
| WPA | 2003 | TKIP (Clau dinàmica) | PSK / 802.1X | Obsolet (Vulnerabilitats d'herència) |
| WPA2 | 2004 | AES / CCMP | PSK (4-Way Handshake) | Envellit (Vulnerable a atacs KRACK) |
| WPA3 | 2018 | AES / GCMP (128/192 bits) | SAE (Dragonfly) / RADIUS | Estàndard Actual Recomanat |

## Diapositiva 11

**BONES PRÀCTIQUES**

**Recomanacions per a Xarxes Wi-Fi Empresarials**

**Desactivar WEP / WPA1**

**Migració a WPA3 / Transition Mode**

**Xarxes de Convidats (Guest)**

Desactivar de forma permanent l'ús de protocols antics en els punts d'accés (APs).

Configurar WPA3-Personal o utilitzar el mode de transició (WPA2/WPA3) mentre es renoven dispositius clients antics.

Aïllar el trànsit de convidats en una VLAN diferent sense accés als recursos interns corporatius.

## Diapositiva 12

![Imatge 3](@@IMG@@/img-003.jpg){ loading=lazy }

![Imatge 4](@@IMG@@/img-004.png){ loading=lazy }

**Resum d'Estudi - Seguretat Wi-Fi**

L'evolució des del feble **WEP** i el conjunt transitori **WPA/WPA2** culmina en el protocol **WPA3**, que garanteix la protecció del trànsit mitjançant negociació **SAE**, xifratge individualitzat i resistència davant d'atacs de força bruta.
