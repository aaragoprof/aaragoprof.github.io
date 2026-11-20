# Seguretat en Xarxes Sense Fil i Mobilitat

<p class="md-kicker">MÒDUL DE SEGURETAT INFORMÀTICA I XARXES</p>

Material d'estudi: Evolució de Protocols Wi-Fi (WEP, WPA, WPA2, WPA3), Algorismes de Xifratge i Protecció davant d'Atacs Moderns

## El Desafiament del Medi Sense Fil

<p class="md-kicker">CONCEPTE I CONTEXT</p>

A diferència de les xarxes cablejades on l'accés requereix connexió física a un connector, les ones de ràdio Wi-Fi es propaguen a l'espai públic. Això fa imprescindible establir protocols de xifratge per garantir la confidencialitat.

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#EF4444" markdown="1">

### Medi Obert

Qualsevol dispositiu a l'abast de les ones pot escoltar el trànsit si no està correctament xifrat.

</div>

<div class="md-card" style="--card:#0284C7" markdown="1">

### Xifrat de Canal

Mecanismes per codificar les dades transmitides entre el client i l'Punt d'Accés (AP).

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### Evolució Tecnològica

Sistemes de seguretat en constant actualització per corregir vulnerabilitats descobertes en protocols antics.

</div>

</div>

## WEP (Wired Equivalent Privacy): El Primer Protocol

<p class="md-kicker">ORIGEN HISTÒRIC</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#EF4444" markdown="1">

### Objectiu i Disseny

Creat per oferir a les xarxes sense fil un nivell de seguretat equivalent al d'una xarxa de cable tradicional.

- **Clau Estàtica:** Utilitzava una mateixa clau que mai no canviava.
- **Algorisme RC4:** Xifratge feble i propens a col·lisions de vector d'inicialització (IV).

</div>

<div class="md-card" style="--card:#EF4444" markdown="1">

### Vulnerabilitat Absoluta

Els atacants van descobrir que, capturant un nombre suficient de paquets de dades, es podia obtenir la clau en pocs minuts.

<div class="md-callout" style="--card:#EF4444" markdown="1">

**Estat actual: Totalment obsolet i insegur. Prohibit en entorns corporatius.**

</div>

</div>

</div>

## WPA (2003): El "Pegat" d'Emergència

<p class="md-kicker">TRANSICIÓ DE SEGURETAT</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#F59E0B" markdown="1">

### Solució d'Emergència

Desenvolupat per la Wi-Fi Alliance per substituir WEP ràpidament sense requerir el canvi del maquinari existent (routers antics).

<div class="md-callout" style="--card:#F59E0B" markdown="1">

**Introducció de TKIP (Temporal Key Integrity Protocol), algorisme que canviava la clau per a cada paquet de dades.**

</div>

</div>

<div class="md-card" style="--card:#0284C7" markdown="1">

### Limitació Tecnològica

Tot i que millorava la seguretat de WEP, encara heretava part de la seva estructura base per mantenir la compatibilitat amb dispositius antics, deixant escletxes de seguretat.

</div>

</div>

## WPA2 (2004): L'Estàndard d'Or

<p class="md-kicker">CONSOLIDACIÓ DE SEGURETAT</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#16A34A" markdown="1">

### Innovació Principal: AES

Va ser el protocol dominant durant més de 15 anys. Reemplaça el feble TKIP per l'algorisme de grau militar **AES (Advanced Encryption Standard)** i CCMP.

- Alta resistència al desxifratge directe.
- Dos modes principals: WPA2-Personal (PSK) i WPA2-Enterprise (802.1X/RADIUS).

</div>

<div class="md-card" style="--card:#EF4444" markdown="1">

### L'Atac KRACK (2017)

Descoberta de la vulnerabilitat **KRACK (Key Reinstallation Attacks)**. Els atacants podien intervenir el procés de negociació (handshake) de connexió i desxifrar el trànsit, accelerant la transició cap a WPA3.

</div>

</div>

## WPA3 (2018 - Present): La Seguretat Moderna

<p class="md-kicker">ESTÀNDARD ACTUAL</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### Xifratge Individualitzat

Encara que un tercer sàpiga la contrasenya de la xarxa, no pot desxifrar el tràfic enviat prèviament per altres usuaris.

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### Anti Força Bruta

Bloqueja automàticament els intents repetits de provar milers de contrasenyes per minut (atacs de diccionari).

</div>

<div class="md-card" style="--card:#8B5CF6" markdown="1">

### Protocol SAE

Substitueix la negociació antiga PSK pel mètode **SAE (Simultaneous Authentication of Equals)** molt més resistent.

</div>

</div>

## Negociació de Clau: PSK (WPA2) vs. SAE (WPA3)

<p class="md-kicker">CRIPTOGRAFIA DE CONNEXIÓ</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#F59E0B" markdown="1">

### PSK (Pre-Shared Key en WPA2)

Negociació en 4 passos (Handshake). Un atacant pot capturar el handshake i intentar desxifrar la contrasenya *offline* mitjançant atacs de força bruta sense estar connectat a la xarxa.

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### SAE (Simultaneous Auth of Equals en WPA3)

Basat en el protocol Dragonfly (Diffie-Hellman sobre corbes el·líptiques).

- Obliga a interactuar amb l'AP per cada intent de clave.
- Elimina completament els atacs de diccionari fora de línia (offline).

</div>

</div>

## Xifratge Individualitzat i Privacitat cap Enrere

<p class="md-kicker">PRIVACITAT D'USUARI</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### Aïllament de Trànsit entre Clients

En xarxes WPA2 obertes o compartides, tots els usuaris usaven claus que permetien espiar el tràfic del veí de taula.

**En WPA3:** Es genera una clau de xifratge única per a cada sessió de dispositiu individual.

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### Forward Secrecy (Privacitat Segura)

Si un atacant esbrina la contrasenya de la xarxa en el futur, **no podrà desxifrar les dades que s'hagin enmagatzemat o capturat prèviament** a l'aire.

</div>

</div>

## Modes d'Desplegament: Personal (PSK/SAE) vs. Enterprise

<p class="md-kicker">ARQUITECTURA DE XARXA</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### Mode Personal (WPA3-Personal)

- Ús domèstic o petites oficines.
- Utilitza una contrasenya única compartida per a tots els usuaris.
- Utilitza **SAE (128 bits)** per a la connexió inicial segura.

</div>

<div class="md-card" style="--card:#8B5CF6" markdown="1">

### Mode Enterprise (WPA3-Enterprise)

- Entorns corporatius i universitaris.
- Autenticació individual d'usuaris mitjançant **servidor RADIUS (802.1X)**.
- Opció de xifratge d'alta seguretat de **192 bits** per a entorns governamentals.

</div>

</div>

## Diapositiva 10

**SÍNTESI D'ESTUDI**

**Taula Comparativa de Protocols de Seguretat Wi-Fi**

| Protocol | Any | Algorisme de Xifratge | Mètode d'Autenticació | Estat de Seguretat Actual |
|---|---|---|---|---|
| WEP | 1997 | RC4 (Clau estàtica) | Clau compartida feble | Totalment Insegur (Desxifrable en minuts) |
| WPA | 2003 | TKIP (Clau dinàmica) | PSK / 802.1X | Obsolet (Vulnerabilitats d'herència) |
| WPA2 | 2004 | AES / CCMP | PSK (4-Way Handshake) | Envellit (Vulnerable a atacs KRACK) |
| WPA3 | 2018 | AES / GCMP (128/192 bits) | SAE (Dragonfly) / RADIUS | Estàndard Actual Recomanat |

## Recomanacions per a Xarxes Wi-Fi Empresarials

<p class="md-kicker">BONES PRÀCTIQUES</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#EF4444" markdown="1">

### Desactivar WEP / WPA1

Desactivar de forma permanent l'ús de protocols antics en els punts d'accés (APs).

</div>

<div class="md-card" style="--card:#0284C7" markdown="1">

### Migració a WPA3 / Transition Mode

Configurar WPA3-Personal o utilitzar el mode de transició (WPA2/WPA3) mentre es renoven dispositius clients antics.

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### Xarxes de Convidats (Guest)

Aïllar el trànsit de convidats en una VLAN diferent sense accés als recursos interns corporatius.

</div>

</div>

## Resum d'Estudi - Seguretat Wi-Fi

L'evolució des del feble **WEP** i el conjunt transitori **WPA/WPA2** culmina en el protocol **WPA3**, que garanteix la protecció del trànsit mitjançant negociació **SAE**, xifratge individualitzat i resistència davant d'atacs de força bruta.
