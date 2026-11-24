# Seguretat Física i Lògica

<p class="md-kicker">MÒDUL DE SEGURETAT INFORMÀTICA</p>

Material d'estudi detallat: Principis de Fiabilitat (CID), Protecció de CPD/SAI, Autenticació i Criptografia Simètrica/Asimètrica

## Seguretat Informàtica i la Triada CID

<p class="md-kicker">CONCEPTES FONAMENTALS</p>

<div class="md-callout" style="--card:#0284C7" markdown="1">

**Com que la seguretat absoluta és impossible, la gestió de seguretat és un compromís econòmic i operatiu entre el risc assumible i el cost. Parlem de fiabilitat quan es garanteixen aquests 3 pilars:**

</div>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### Confidencialitat

Garanteix que la informació i els recursos del sistema només siguin accessibles per als usuaris o processos degudament autoritzats, evitant filtracions no desitjades.

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### Integritat

Assegura que la informació, dades i programari no hagin estat modificats, manipulats o esborrats de forma fraudulenta o accidental per cap entitat no autoritzada.

</div>

<div class="md-card" style="--card:#F59E0B" markdown="1">

### Disponibilitat

Garanteix que els serveis, dades i recursos informàtics (processadors, impressores, memòria) estiguin operatius i accessibles sempre que els usuaris ho requereixin.

</div>

</div>

## Elements Vulnerables del Sistema

<p class="md-kicker">ACTIUS A PROTEGIR</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### 1. Maquinari (Hardware)

Equips físics, servidors, estacions de treball, dispositius de xarxa (encaminadors, switches), cablatge i sistemes d'emmagatzematge. Són vulnerables a avaries, robatoris o desastres ambientals.

</div>

<div class="md-card" style="--card:#8B5CF6" markdown="1">

### 2. Programari (Software)

Sistemes operatius, aplicacions de negoci, servidors web i bases de dades. Vulnerables a errors de programació (bugs), defectes de disseny, injeccions de codi i atac de malware.

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### 3. Dades (Informació)

L'actiu de més valor de l'organització. Inclou bases de dades de clients, la propietat intel·lectual, fitxers financers i credencials. Vulnerables a la fuga, alteració o destrucció.

</div>

</div>

## Diferència entre Vulnerabilitat i Amenaça

<p class="md-kicker">ANÀLISI DE RISCOS</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### Vulnerabilitat (Factor Intern)

**Feblesa inherent al sistema**

- **Física/Natural:** CPDs sense control de temperatura o sense control d'accés a la porta.
- **Tècnica:** Software desactualitzat, ports oberts innecessaris o absència de xifratge.
- **Humana:** Personal no format en ciberseguretat o contrasenyes febles/reutilitzades.

</div>

<div class="md-card" style="--card:#EF4444" markdown="1">

### Amenaça (Agent Extern)

**Esdeveniment que explota una vulnerabilitat**

- **Físiques:** Incendis, talls de fluid elèctric, inundacions, danys per pols o descàrregues.
- **Lògiques:** Infecció per Ransomware, atacs DoS/DDoS, Phishing o intromissions no autoritzades.
- **Objectiu:** Materialitzar un dany directament sobre el maquinari, software o dades.

</div>

</div>

## Protecció del CPD i Estacions de Treball

<p class="md-kicker">INFRAESTRUCTURES FÍSIQUES</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### CPD (Data Center)

Instal·lació d'alta seguretat dissenyada per allotjar servidors sota condicions ambientalment estrictes.

- Control de temperatura i humitat constant.
- Protecció electromagnètica i aïllament.
- Sistemes avançats d'extinció d'incendis per gas.

</div>

<div class="md-card" style="--card:#F59E0B" markdown="1">

### Estacions de Treball

Tot i no contingut dades crítiques directament, poden ser la porta d'entrada a la xarxa corporativa.

- Accés físic restringit a personal autoritzat.
- Bloqueig automàtic de sessió i protecció per contrasenya.
- Protecció física de cablatge i connectors.

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### Control i Vigilància

Mesures preventives administratives i de monitorització contínua.

- Videovigilància CCTV (complint normativa de privacitat).
- Realització d'inventaris periòdics d'equips.
- Separació de l'emmagatzematge de dades respecte al HW general.

</div>

</div>

## Sistemes SAI / UPS per a Servidors

<p class="md-kicker">PROTECCIÓ ELÈCTRICA</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#EF4444" markdown="1">

### Perills dels Talls d'Electricitat

Una apagada repentina sense aturada controlada provoca danys greus en els servidors:

- Pèrdua irreversible de dades emmagatzemades a la memòria cau (Cache RAM).
- Corrupció de fitxers de sistema oberts i bases de dades transaccionals.
- Errors crítics i impossibilitat d'arrencada en el reinici.

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### Factors Claus de Triar un SAI

- **Potència (Watts / VA):** Determina el nombre màxim d'equips i servidors que es poden alimentar simultàniament.
- **Autonomia (Temps de bateria):** Minuts disponibles per mantenir l'activitat abans d'iniciar l'apagada.
- **Comunicació i Apagada Automàtica (USB/Sèrie):** Envia alertes d'estat de bateria al SO, executa scripts d'aturada segura i ordenada i reinicia el servidor en tornar el corrent.
- **Manteniment:** Canvi periòdic de bateries segons especificacions del fabricant.

</div>

</div>

## Els 3 Factors d'Autenticació

<p class="md-kicker">CONTROL D'ACCÉS DIGITAL</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### 1. El que Saps

**Contrasenyes i PINs**

Mètode econòmic però més vulnerable a la filtració o descavells. Requereix ≥12 caràcters, majúscules, minúscules, números, símbols i no reutilització.

</div>

<div class="md-card" style="--card:#8B5CF6" markdown="1">

### 2. El que Tens

**Targetes i Tokens**

Dispositius físics compactes com targetes intel·ligents (DNIe), claus de seguretat USB (YubiKey) o tokens de fitxatge tipus clauer.

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### 3. El que Ets

**Sistemes Biomètrics**

Característiques físiques úniques: empremta dactilar, reconeixement facial o escàner de retina. Alta fiabilitat sense haver de recordar claus.

</div>

</div>

## Criptosistemes Simètrics

<p class="md-kicker">CRIPTOGRAFIA DE CLAU PRIVADA</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### Principi de Funcionament

L'emissor i el receptor utilitzen la **mateixa clau secreta compartida** tant per xifrar el text en clar com per desxifrar el criptograma.

<div class="md-callout" style="--card:#F97316" markdown="1">

**Problema principal:** Com fer arribar la clau al receptor inicialment de forma segura sense que sigui interceptada.

</div>

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### Evolució dels Algorismes

- **Obsolets:** DES (1977), Triple DES, Blowfish / IDEA (superats per tenir mides de bloc de dades petites o claus curtes).
- **Estàndard Actual (AES-256):** Advanced Encryption Standard. Mètode ultra-ràpid, utilitzat globalment i considerat 100% segur fins i tot contra la computació quàntica.
- **Modern Mòbil (ChaCha20):** Desenvolupat el 2008, d'alta velocitat en mòbils, emprat a WireGuard i TLS 1.3.

</div>

</div>

## Criptosistemes Asimètrics

<p class="md-kicker">CRIPTOGRAFIA DE CLAU PÚBLICA</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### Analogia de la Bústia i el Candau

Imagina que cada usuari té una bústia al carrer amb un candau especial:

- **Clau Pública (Pu):** És el candau obert disponible a un directori públic. Qualsevol persona pot agafar la clau Pu per tancar una carta a la bústia. Un cop tancada, ningú al carrer la pot obrir.
- **Clau Privada (Su):** És la clau física secreta que només té el propietari per obrir el candau i llegir el missatge.

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### Signatura Digital i No-Repudi

Com que les claus estan vinculades matemàticament, allò que es tanca amb la clau privada (Su) es pot verificar amb la pública (Pu).

<div class="md-callout" style="--card:#22C55E" markdown="1">

**Propietat de No-Repudi:** Permet signar digitalment documents confirmant l'autoria. L'emissor no pot negar haguer-ho enviat.

</div>

</div>

</div>

## Resum d'Estudi - Seguretat Física 1.0

La seguretat integral combina la protecció ambiental del maquinari (CPD i SAI), mètodes robusos d'autenticació multifactor i l'ús combinat de criptografia simètrica (AES-256 per a velocitat) i asimètrica (RSA/Pu-Su per a intercanvi i signatures).
