# Còpies de Seguretat i Emmagatzematge

<p class="md-kicker">MÒDUL D'ADMINISTRACIÓ DE SISTEMES I SEGURETAT</p>

Material d'estudi: Jerarquia de Memòria, Rendiment de Busos (DDR5 vs. NVMe), Emmagatzematge Terciari i Protocols de Xarxa (NAS/SMB/NFS)

## Necessitat de l'Emmagatzematge Permanent i Segur

<p class="md-kicker">NECESSITAT DEL BACKUP</p>

Els sistemes informàtics reben dades d'entrada, les processen i generen resultats. La seguretat inicial de l'equip és insuficient: cal emmagatzematge permanent fiable per evitar pèrdues catastròfiques (com les d'un banc).

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### Principi de Disponibilitat

Garanteix que les dades guardades estiguin sempre accessibles i al nostre abast quan calgui reprendre o processar tasques en el futur.

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### Principi de Confidencialitat

Assegura que l'accés a les còpies i dades emmagatzemades estigui estrictament restringit a les persones degudament autoritzades.

</div>

<div class="md-card" style="--card:#8B5CF6" markdown="1">

### Redundància i Particions

La gestió avançada requereix la classificació dels medis, l'organització lògica per particions i l'ús de sistemes de redundància de dades.

</div>

</div>

## Emmagatzematge Primari (Intern) vs. Secundari (Extern)

<p class="md-kicker">CLASSIFICACIÓ DEL MAQUINARI</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#EF4444" markdown="1">

### Memòria Interna / Primària (RAM)

- **Volàtil:** Només reté la informació mentre l'equip rep alimentació elèctrica.
- Conectada directament a la CPU mitjançant el bus de memòria de la placa.
- Si es talla l'energia o l'equip s'apaga, les dades no desades **es perden completament**.

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### Emmagatzematge Secundari / Permanència

- **No volàtil:** Enregistra la informació de forma permanent en mitjans físics.
- Reté les dades independentment de si hi ha o no subministrament elèctric.
- **Tecnologies:** Unitats d'estat sòlid (SSD), discos durs magnètics (HDD) i cintes.

</div>

</div>

## Memòria RAM (DDR5) i Analogia de l'Escriptori

<p class="md-kicker">RENDIMENT EXTREM</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### Ample de Banda DDR5

La comunicació entre la RAM i la CPU utilitza un bus dedicat ultra-ràpid.

**DDR5 (Dual/Quad Channel): Ofereix fàcilment amplades de banda de 40 GB/s a més de 80 GB/s.**

</div>

<div class="md-card" style="--card:#F97316" markdown="1">

### Analogia de la Taula i l'Armari

<div class="md-callout" style="--card:#F97316" markdown="1">

- **RAM = Taula de Treball:** En obrir un programa (Word, joc) agafes l'eina de l'armari (Disc) i la penses a la taula. Treballar sobre la taula és ràpid i immediat.
- **Disc Dur = Armari:** Si s'apaga la llum sense guardar (tornar la feina a l'armari), tot el que hi ha a la taula de treball (RAM) es manté brut i es perd per sempre.

</div>

</div>

</div>

## Diapositiva 5

**AVALUACIÓ DE RENDIMENT**

**Velocitats de l'Emmagatzematge Secundari**

Tot i l'evolució de les unitats d'estat sòlid, cap dispositiu secundari no iguala la velocitat directa del bus de la memòria RAM:

| Tecnologia de Dispositiu | Interfície / Bus | Ample de Banda / Velocitat Màxima |
|---|---|---|
| SSD SATA III | Bus SATA integrat | Aproximadament 550 – 600 MB/s (Límit de l'especificació) |
| SSD NVMe Gen 3.0 | PCIe 3.0 x4 | Fins a 3,5 GB/s (3.500 MB/s) |
| SSD NVMe Gen 4.0 | PCIe 4.0 x4 | Fins a 7,5 GB/s (7.500 MB/s) |
| SSD NVMe Gen 5.0 | PCIe 5.0 x4 | Fins a 14 GB/s (14.000 MB/s) |

## Integració a la Placa i Targetes d'Expansió

<p class="md-kicker">ARQUITECTURA HARDWARE</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### Controladors Integrats (Chipset/CPU)

En els ordinadors moderns, els controladors per a interfícies SATA i ports NVMe estan integrats directament al **Chipset** de la placa o connectats directament a les línies PCIe de la **CPU**.

</div>

<div class="md-card" style="--card:#8B5CF6" markdown="1">

### Targetes d'Expansió PCIe

En entorns professionals o servidors d'alt rendiment, s'utilitzen targetes d'expansió en ranures PCIe addicionals per afegir:

- Controladors **RAID per hardware** especialitzats.
- Targetes d'ampliació de múltiples ports NVMe ultra-ràpids.

</div>

</div>

## Memòria Virtual (Swap / Paging File)

<p class="md-kicker">GESTIÓ DEL SISTEMA OPERATIU</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### Objectiu de la Memòria Virtual

Tècnica del SO per gestionar l'escassetat de memòria RAM física:

- Mou blocs de dades o processos poc utilitzats des de la RAM al disc dur quan la RAM s'omple.
- Allibera RAM per als processos actius, permetent executar més aplicacions simultàniament.

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### Evolució de HDD a SSD

Amb els antics HDD, l'ús de Swap suposava una *degradació severa del rendiment*. Amb els SSDs NVMe actuals, s'ha transformat en una **solució d'emergència molt més ràpida** i eficaç.

</div>

</div>

## Emmagatzematge Terciari i Dades Fredes

<p class="md-kicker">DADES FREDES I MASSIVES</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#F59E0B" markdown="1">

### Característiques del Terciari

- **Sistemes Robotitzats:** Utilitza braços mecànics que carreguen i munten automàticament els mitjans físics.
- **Velocitat Lenta:** El temps d'accés és alt pel temps mecànic de trobar i carregar la cinta o disc.
- **Dades Fredes (Cold Data):** Dissenyat per a informació massiva (TBs/PBs) a la qual s'accedeix molt raramen.

</div>

<div class="md-card" style="--card:#0284C7" markdown="1">

### Exemples i Avantatge Econòmic

**Biblioteques de Cintes en Centres de Dades:**

Prioritza l'economia per terabyte i la gran capacitat de retenció a llarg termini per sobre de la velocitat immediata.

</div>

</div>

## Emmagatzematge Fora de Línia (Offline)

<p class="md-kicker">AÏLLAMENT DE SEGURETAT</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#EF4444" markdown="1">

### Concepte Fora de Línia

Mitjà d'emmagatzematge que **no està sota el control de cap unitat de processament (CPU)** ni connectat a la xarxa.

Per tal d'accedir a la informació cal necessàriament la **intervenció humana** per connectar el dispositiu.

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### Utilitats i Exemples

- Transferència fàcil de dades entre sistemes aïllats.
- Realització de còpies de seguretat personals o aïllades de Ransomware (Air-gap).
- Discs durs externs, unitats USB o cintes extraïbles guardades en caixes fortes.

</div>

</div>

## Emmagatzematge Distribuït i Protocols de Xarxa

<p class="md-kicker">COMPARTICIÓ EN XARXA</p>

Desar la informació en servidors de xarxa perquè els equips clients hi accedeixin com si fos un disc local:

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### Entorn Windows (SMB)

Utilitza el protocol **SMB (Server Message Block)**, integrat normalment en un entorn de domini amb **Active Directory** per a l'autenticació centralitzada.

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### Entorn UNIX/Linux (NFS)

Utilitza **NFS (Network File System)**, el protocol clàssic per a la compartició nativa de fitxers d'alta velocitat entre sistemes Linux/UNIX.

</div>

<div class="md-card" style="--card:#8B5CF6" markdown="1">

### Interoperabilitat (SAMBA)

Implementació lliure del protocol SMB que permet a clients Windows accedir a servidors Linux i viceversa sense problemes de compatibilitat.

</div>

</div>

## Servidors Multitasca vs. Dispositius NAS Dedicats

<p class="md-kicker">ARQUITECTURA DE SERVIDORS</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### Servidors Completament Configurats

Equips versàtils d'alt rendiment. A més de compartir fitxers, realitzen tasques complexes:

- Allotjar bases de dades corporatives.
- Gestionar correu electrònic i servidors Web/Aplicació.

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### Dispositius NAS (Network Attached Storage)

Dispositius dedicats especialment dissenyats per compartir fitxers en xarxa:

- Utilitzen un **sistema operatiu lleuger optimitzat**.
- Funció quasi exclusiva d'emmagatzematge i gestió de volums RAID.
- Solució escalable i senzilla per a entorns domèstics, PIMEs i empreses.

</div>

</div>

## Resum d'Estudi - Emmagatzematge i Backups

La gestió eficaç combina la velocitat de la RAM i SSDs NVMe per a dades meva actives, amb emmagatzematge terciari/offline per a dades fredes, i protocols distribuïts (**SMB, NFS, NAS**) per a la continuïtat de negoci.
