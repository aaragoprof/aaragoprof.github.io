# Anàlisi de Programari Maliciós

<p class="md-kicker">MÒDUL DE SEGURETAT ACTIVA</p>

Naturalesa del malware, detecció d'integritat i metodologia d'anàlisi en laboratori

## Què és i Com Actua el Programari Maliciós?

<p class="md-kicker">FONAMENTS DEL MALWARE</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### Definició i Tipologia

Programari amb efectes nocius per al sistema com virus, cucs i cavalls de Troia.

</div>

<div class="md-card" style="--card:#EF4444" markdown="1">

### Mecanisme d'Ocultació

S'amaga dins de programes legítims per esborrar o robar dades sense coneixement de l'usuari.

</div>

</div>

## Evolució Històrica del Malware

<p class="md-kicker">TRAJECTÒRIA DE L'AMENAÇA</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### 1972: Creeper

Naixement del primer virus conegut a la xarxa Arpanet.

</div>

<div class="md-card" style="--card:#8B5CF6" markdown="1">

### Anys 80 – 2005

Objectiu centrat a causar danys tècnics o guanyar reconeixement.

</div>

<div class="md-card" style="--card:#EAB308" markdown="1">

### A partir del 2005

Motivació econòmica amb spyware, adware, phishing i troians bancaris.

</div>

</div>

## Propagació i Objectius Actuals

<p class="md-kicker">ESCENARI CONTEMPORANI</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### Vies d'Entrada

Correu electrònic mitjançant enginyeria social i dispositius USB.

</div>

<div class="md-card" style="--card:#EAB308" markdown="1">

### Tipus d'Atac

Atacs massius indiscriminats o dirigits a organitzacions d'alt valor.

</div>

<div class="md-card" style="--card:#EF4444" markdown="1">

### Plataformes

De Windows com a blanc històric cap als telèfons mòbils actuals.

</div>

</div>

## Mètodes de Detecció del Codi Maliciós

<p class="md-kicker">SUPERVISIÓ D'INTEGRITAT</p>

<div class="md-card" markdown="1">



</div>

| Enfocament | Funcionament | Eines i Fiabilitat |
|---|---|---|
| 1. Anàlisi de Fitxers | Revisa dates i mida dels fitxers | Poc fiable per manipulació (timestomping) |
| 2. Control Hash (FIM) | Empremta SHA-256 en base immutable | Tripwire, Wazuh i OSSEC (detecció a posteriori) |
| 3. Temps Real | Monitorització contínua del comportament | Antivirus NGAV i sistemes EDR bloquejants |

## Preparació d'un Entorn Aïllat (Sandbox)

<p class="md-kicker">FASE 1 D'ANÀLISI</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### Aïllament Total

Màquines virtuals separades (VirtualBox, Proxmox) o Cuckoo i ANY.RUN.

</div>

<div class="md-card" style="--card:#8B5CF6" markdown="1">

### Línia Base i Snapshots

Instantànies prèvies i registre de ports, processos i recursos inicials.

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### Eines d'Inspecció

Captura de trànsit amb Wireshark i activitat amb Sysmon.

</div>

</div>

## Anàlisi Estàtica vs. Anàlisi Dinàmica

<p class="md-kicker">FASE 2 D'ANÀLISI</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### Anàlisi Estàtica (Sense Executar)

- Estudi del fitxer en repòs i metadades.
- Extracció de hashes, cadenes (strings), capçaleres i codi.

</div>

<div class="md-card" style="--card:#EAB308" markdown="1">

### Anàlisi Dinàmica (En Execució)

- Observació en viu de connexions externes (C2).
- Control de nous processos, registre i fitxers alterats.

</div>

</div>

## Extracció d'IoCs i Resposta a Incidents (DFIR)

<p class="md-kicker">FASE 3 D'ANÀLISI</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### Indicadors de Compromís (IoCs)

Documentació d'IPs malicioses, dominis i hashes per alimentar tallafocs i antivirus.

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### Aplicació Forense Real

Metodologia clau per investigar sistemes ja compromesos en entorns de producció (DFIR).

</div>

</div>

## Resum d'Estudi - Anàlisi de Programari Maliciós

Combatre el malware actual exigeix integritat immutable amb **FIM/EDR** i una metodologia rigorosa en **Sandbox** per extreure **IoCs** útils en resposta a incidents.
