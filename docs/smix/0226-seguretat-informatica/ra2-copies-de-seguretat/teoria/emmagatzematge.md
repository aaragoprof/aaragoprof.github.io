---
description: Classificació dels dispositius d'emmagatzematge, velocitats, memòria virtual i emmagatzematge distribuït en xarxa.
pdf: ""
---

# Gestió de dispositius d'emmagatzematge

## Introducció

Els sistemes informàtics processen dades rebudes per perifèrics d'entrada i les mostren per perifèrics de sortida. És necessari emmagatzemar la informació de manera permanent per guardar resultats o preparar processaments futurs.

La seguretat inicial no és suficient; calen tècniques per assegurar la integritat de les dades emmagatzemades. La gestió dels dispositius inclou la seva classificació i l'organització lògica de la informació mitjançant sistemes de redundància i l'ús de particions.

## Memòria interna i externa

**Memòria interna**
:   Capaç de retenir informació només mentre l'equip rep alimentació elèctrica (és a dir, és volàtil). Es considera el dispositiu d'emmagatzematge primari (típicament la memòria RAM).

**Memòria externa**
:   Dispositius que enregistren la informació de manera permanent (són no volàtils). Retenen les dades independentment de l'alimentació elèctrica (discs durs SSD, HDD o cintes magnètiques). Es considera el dispositiu d'emmagatzematge secundari.

!!! info "Analogia de la memòria RAM"
    Penseu en la RAM com l'escriptori o la taula de treball del vostre ordinador:
    
    1. Quan obriu un programa, porteu els arxius des de l'armari (disc dur) cap a la taula (RAM).
    2. Mentre treballeu, tot es fa directament sobre aquesta taula (ràpid i fàcil).
    3. Si s'apaga el llum sense desar (sense tornar la informació al disc dur), tot el que hi ha a la taula es perd per sempre.

## Comparativa de velocitats

La memòria RAM és més ràpida i proporciona un accés més ràpid a la CPU que qualsevol dispositiu d'emmagatzematge secundari, inclosos els SSD NVMe més moderns.

| Tecnologia | Velocitat Típica (Lectura/Escriptura) |
|---|---|
| RAM (DDR5) | $40 - 80\text{ GB/s}$ |
| SSD NVMe (PCIe 5.0) | fins a $14\text{ GB/s}$ |
| SSD NVMe (PCIe 4.0) | $5 - 7.5\text{ GB/s}$ |
| SSD NVMe (PCIe 3.0) | fins a $3.5\text{ GB/s}$ |
| SSD SATA | $\sim 0.55\text{ GB/s}$ ($550-600\text{ MB/s}$) |

### Integració a la placa base
Els controladors bàsics per a interfícies SATA i la majoria de ports NVMe estan integrats al Chipset de la placa base o directament a la CPU. En entorns professionals s'utilitzen targetes d'expansió en ranures PCI Express (PCIe) per afegir controladors RAID o ports NVMe addicionals.

## Memòria virtual en l'era de l'SSD

La **memòria virtual** (o *swap space* / *paging file*) és una tècnica que utilitza el Sistema Operatiu per gestionar l'escassetat de RAM:

* **Objectiu:** Permet moure blocs de dades o processos menys utilitzats de la RAM a l'emmagatzematge secundari quan la RAM s'omple, alliberant espai per als processos més actius.
* **Evolució:** La transició dels HDD als SSD ha transformat la seva implementació d'una "degradació severa del rendiment" a una "solució d'emergència molt més ràpida".

## Altres nivells d'emmagatzematge

### Emmagatzematge terciari
Definit per la gestió de dades a gran escala i la seva automatització mitjançant un sistema robotitzat o mecànic que gestiona els mitjans físics.
* **Velocitat lenta:** Inclou el temps mecànic de localitzar, carregar i muntar el mitjà.
* **Dades fredes:** S'utilitza principalment per a magatzems d'informació massius (TBs o PBs) on l'accés és molt infreqüent.
* *Exemple:* Biblioteques de cintes en centres de dades.

### Emmagatzematge fora de línia (*Offline*)
Mitjà d'emmagatzematge que no està sota el control directe d'una unitat de processament. Requereix la intervenció humana per accedir-hi i s'utilitza habitualment per transferir informació entre sistemes diferents.

## Emmagatzematge distribuït i en xarxa

Consisteix a desar la informació en un o més ordinadors anomenats **servidors**, els quals fan accessible aquesta informació a altres ordinadors anomenats **clients** com si fos emmagatzemada localment.

* **Sistemes Windows:** Utilitzen principalment carpetes compartides mitjançant el protocol **SMB** (Server Message Block), sovint dins d'un domini d'Active Directory.
* **Sistemes UNIX / GNU/Linux:**
    * **NFS (Network File System):** Protocol clàssic per a la compartició nativa entre sistemes UNIX/Linux.
    * **SAMBA:** Implementació lliure del protocol SMB que permet la interoperabilitat entre clients Windows i servidors Linux.

### Tipus de servidors de fitxers

**Ordinadors completament configurats**
:   Servidors versàtils que, a més de compartir fitxers, poden executar altres tasques (bases de dades, correu, web).

**Servidors dedicats (NAS - Network Attached Storage)**
:   Dispositius dissenyats específicament per a compartir fitxers a través d'una xarxa. Utilitzen un sistema operatiu lleuger i tenen com a funció gairebé exclusiva l'emmagatzematge i la gestió de RAID.