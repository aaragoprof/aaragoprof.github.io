# Seguretat Física 1.0 - Material d'Estudi Ampliat

## Diapositiva 1

![Imatge 1](@@IMG@@/img-001.jpg){ loading=lazy }

![Imatge 2](@@IMG@@/img-002.png){ loading=lazy }

**Seguretat Física i Lògica**

**MÒDUL DE SEGURETAT INFORMÀTICA**

Material d'estudi detallat: Principis de Fiabilitat (CID), Protecció de CPD/SAI, Autenticació i Criptografia Simètrica/Asimètrica

## Diapositiva 2

**CONCEPTES FONAMENTALS**

**Seguretat Informàtica i la Triada CID**

**Com que la seguretat absoluta és impossible, la gestió de seguretat és un compromís econòmic i operatiu entre el risc assumible i el cost. Parlem de fiabilitat quan es garanteixen aquests 3 pilars:**

Garanteix que la informació i els recursos del sistema només siguin accessibles per als usuaris o processos degudament autoritzats, evitant filtracions no desitjades.

**Confidencialitat**

Assegura que la informació, dades i programari no hagin estat modificats, manipulats o esborrats de forma fraudulenta o accidental per cap entitat no autoritzada.

**Integritat**

Garanteix que els serveis, dades i recursos informàtics (processadors, impressores, memòria) estiguin operatius i accessibles sempre que els usuaris ho requereixin.

**Disponibilitat**

## Diapositiva 3

**ACTIUS A PROTEGIR**

**Elements Vulnerables del Sistema**

**1. Maquinari (Hardware)**

**2. Programari (Software)**

**3. Dades (Informació)**

Equips físics, servidors, estacions de treball, dispositius de xarxa (encaminadors, switches), cablatge i sistemes d'emmagatzematge. Són vulnerables a avaries, robatoris o desastres ambientals.

Sistemes operatius, aplicacions de negoci, servidors web i bases de dades. Vulnerables a errors de programació (bugs), defectes de disseny, injeccions de codi i atac de malware.

L'actiu de més valor de l'organització. Inclou bases de dades de clients, la propietat intel·lectual, fitxers financers i credencials. Vulnerables a la fuga, alteració o destrucció.

## Diapositiva 4

**ANÀLISI DE RISCOS**

**Diferència entre Vulnerabilitat i Amenaça**

**Vulnerabilitat (Factor Intern)**

**Amenaça (Agent Extern)**

**Feblesa inherent al sistema**

**Esdeveniment que explota una vulnerabilitat**

• **Física/Natural:** CPDs sense control de temperatura o sense control d'accés a la porta.

• **Físiques:** Incendis, talls de fluid elèctric, inundacions, danys per pols o descàrregues.

• **Tècnica:** Software desactualitzat, ports oberts innecessaris o absència de xifratge.

• **Lògiques:** Infecció per Ransomware, atacs DoS/DDoS, Phishing o intromissions no autoritzades.

• **Humana:** Personal no format en ciberseguretat o contrasenyes febles/reutilitzades.

• **Objectiu:** Materialitzar un dany directament sobre el maquinari, software o dades.

## Diapositiva 5

**INFRAESTRUCTURES FÍSIQUES**

**Protecció del CPD i Estacions de Treball**

**CPD (Data Center)**

**Estacions de Treball**

**Control i Vigilància**

Instal·lació d'alta seguretat dissenyada per allotjar servidors sota condicions ambientalment estrictes.

Tot i no contingut dades crítiques directament, poden ser la porta d'entrada a la xarxa corporativa.

Mesures preventives administratives i de monitorització contínua.

• Control de temperatura i humitat constant.

• Videovigilància CCTV (complint normativa de privacitat).

• Protecció electromagnètica i aïllament.

• Accés físic restringit a personal autoritzat.

• Sistemes avançats d'extinció d'incendis per gas.

• Bloqueig automàtic de sessió i protecció per contrasenya.

• Realització d'inventaris periòdics d'equips.

• Separació de l'emmagatzematge de dades respecte al HW general.

• Protecció física de cablatge i connectors.

## Diapositiva 6

**PROTECCIÓ ELÈCTRICA**

**Sistemes SAI / UPS per a Servidors**

**Perills dels Talls d'Electricitat**

Una apagada repentina sense aturada controlada provoca danys greus en els servidors:

• **Potència (Watts / VA):** Determina el nombre màxim d'equips i servidors que es poden alimentar simultàniament.

**Factors Claus de Triar un SAI**

• Pèrdua irreversible de dades emmagatzemades a la memòria cau (Cache RAM).

• **Autonomia (Temps de bateria):** Minuts disponibles per mantenir l'activitat abans d'iniciar l'apagada.

• Corrupció de fitxers de sistema oberts i bases de dades transaccionals.

• **Comunicació i Apagada Automàtica (USB/Sèrie):** Envia alertes d'estat de bateria al SO, executa scripts d'aturada segura i ordenada i reinicia el servidor en tornar el corrent.

• Errors crítics i impossibilitat d'arrencada en el reinici.

• **Manteniment:** Canvi periòdic de bateries segons especificacions del fabricant.

## Diapositiva 7

**CONTROL D'ACCÉS DIGITAL**

**Els 3 Factors d'Autenticació**

**1. El que Saps**

**2. El que Tens**

**3. El que Ets**

**Contrasenyes i PINs**

**Targetes i Tokens**

**Sistemes Biomètrics**

Mètode econòmic però més vulnerable a la filtració o descavells. Requereix ≥12 caràcters, majúscules, minúscules, números, símbols i no reutilització.

Dispositius físics compactes com targetes intel·ligents (DNIe), claus de seguretat USB (YubiKey) o tokens de fitxatge tipus clauer.

Característiques físiques úniques: empremta dactilar, reconeixement facial o escàner de retina. Alta fiabilitat sense haver de recordar claus.

## Diapositiva 8

**CRIPTOGRAFIA DE CLAU PRIVADA**

**Criptosistemes Simètrics**

**Principi de Funcionament**

**Evolució dels Algorismes**

L'emissor i el receptor utilitzen la **mateixa clau secreta compartida** tant per xifrar el text en clar com per desxifrar el criptograma.

• **Obsolets:** DES (1977), Triple DES, Blowfish / IDEA (superats per tenir mides de bloc de dades petites o claus curtes).

• **Estàndard Actual (AES-256):** Advanced Encryption Standard. Mètode ultra-ràpid, utilitzat globalment i considerat 100% segur fins i tot contra la computació quàntica.

**Problema principal:** Com fer arribar la clau al receptor inicialment de forma segura sense que sigui interceptada.

• **Modern Mòbil (ChaCha20):** Desenvolupat el 2008, d'alta velocitat en mòbils, emprat a WireGuard i TLS 1.3.

## Diapositiva 9

**CRIPTOGRAFIA DE CLAU PÚBLICA**

**Criptosistemes Asimètrics**

Imagina que cada usuari té una bústia al carrer amb un candau especial:

**Analogia de la Bústia i el Candau**

Com que les claus estan vinculades matemàticament, allò que es tanca amb la clau privada (Su) es pot verificar amb la pública (Pu).

**Signatura Digital i No-Repudi**

• **Clau Pública (Pu):** És el candau obert disponible a un directori públic. Qualsevol persona pot agafar la clau Pu per tancar una carta a la bústia. Un cop tancada, ningú al carrer la pot obrir.

**Propietat de No-Repudi:** Permet signar digitalment documents confirmant l'autoria. L'emissor no pot negar haguer-ho enviat.

• **Clau Privada (Su):** És la clau física secreta que només té el propietari per obrir el candau i llegir el missatge.

## Diapositiva 10

![Imatge 3](@@IMG@@/img-003.jpg){ loading=lazy }

![Imatge 4](@@IMG@@/img-004.png){ loading=lazy }

**Resum d'Estudi - Seguretat Física 1.0**

La seguretat integral combina la protecció ambiental del maquinari (CPD i SAI), mètodes robusos d'autenticació multifactor i l'ús combinat de criptografia simètrica (AES-256 per a velocitat) i asimètrica (RSA/Pu-Su per a intercanvi i signatures).
