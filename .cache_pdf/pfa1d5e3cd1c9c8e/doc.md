# Còpies de Seguretat i Gestió d'Emmagatzematge

## Diapositiva 1

![Imatge 1](@@IMG@@/img-001.jpg){ loading=lazy }

![Imatge 2](@@IMG@@/img-002.png){ loading=lazy }

**Còpies de Seguretat i Emmagatzematge**

**MÒDUL D'ADMINISTRACIÓ DE SISTEMES I SEGURETAT**

Material d'estudi: Jerarquia de Memòria, Rendiment de Busos (DDR5 vs. NVMe), Emmagatzematge Terciari i Protocols de Xarxa (NAS/SMB/NFS)

## Diapositiva 2

**NECESSITAT DEL BACKUP**

**Necessitat de l'Emmagatzematge Permanent i Segur**

Els sistemes informàtics reben dades d'entrada, les processen i generen resultats. La seguretat inicial de l'equip és insuficient: cal emmagatzematge permanent fiable per evitar pèrdues catastròfiques (com les d'un banc).

**Principi de Disponibilitat**

**Principi de Confidencialitat**

**Redundància i Particions**

Garanteix que les dades guardades estiguin sempre accessibles i al nostre abast quan calgui reprendre o processar tasques en el futur.

Assegura que l'accés a les còpies i dades emmagatzemades estigui estrictament restringit a les persones degudament autoritzades.

La gestió avançada requereix la classificació dels medis, l'organització lògica per particions i l'ús de sistemes de redundància de dades.

## Diapositiva 3

**CLASSIFICACIÓ DEL MAQUINARI**

**Emmagatzematge Primari (Intern) vs. Secundari (Extern)**

**Memòria Interna / Primària (RAM)**

**Emmagatzematge Secundari / Permanència**

• **Volàtil:** Només reté la informació mentre l'equip rep alimentació elèctrica.

• **No volàtil:** Enregistra la informació de forma permanent en mitjans físics.

• Reté les dades independentment de si hi ha o no subministrament elèctric.

• Conectada directament a la CPU mitjançant el bus de memòria de la placa.

• **Tecnologies:** Unitats d'estat sòlid (SSD), discos durs magnètics (HDD) i cintes.

• Si es talla l'energia o l'equip s'apaga, les dades no desades **es perden completament**.

## Diapositiva 4

**RENDIMENT EXTREM**

**Memòria RAM (DDR5) i Analogia de l'Escriptori**

**Ample de Banda DDR5**

**Analogia de la Taula i l'Armari**

La comunicació entre la RAM i la CPU utilitza un bus dedicat ultra-ràpid.

**DDR5 (Dual/Quad Channel): Ofereix fàcilment amplades de banda de 40 GB/s a més de 80 GB/s.**

• **RAM = Taula de Treball:** En obrir un programa (Word, joc) agafes l'eina de l'armari (Disc) i la penses a la taula. Treballar sobre la taula és ràpid i immediat.

• **Disc Dur = Armari:** Si s'apaga la llum sense guardar (tornar la feina a l'armari), tot el que hi ha a la taula de treball (RAM) es manté brut i es perd per sempre.

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

## Diapositiva 6

**ARQUITECTURA HARDWARE**

**Integració a la Placa i Targetes d'Expansió**

**Controladors Integrats (Chipset/CPU)**

**Targetes d'Expansió PCIe**

En els ordinadors moderns, els controladors per a interfícies SATA i ports NVMe estan integrats directament al **Chipset** de la placa o connectats directament a les línies PCIe de la **CPU**.

En entorns professionals o servidors d'alt rendiment, s'utilitzen targetes d'expansió en ranures PCIe addicionals per afegir:

• Controladors **RAID per hardware** especialitzats.

• Targetes d'ampliació de múltiples ports NVMe ultra-ràpids.

## Diapositiva 7

**GESTIÓ DEL SISTEMA OPERATIU**

**Memòria Virtual (Swap / Paging File)**

**Objectiu de la Memòria Virtual**

**Evolució de HDD a SSD**

Tècnica del SO per gestionar l'escassetat de memòria RAM física:

• Mou blocs de dades o processos poc utilitzats des de la RAM al disc dur quan la RAM s'omple.

Amb els antics HDD, l'ús de Swap suposava una *degradació severa del rendiment*. Amb els SSDs NVMe actuals, s'ha transformat en una **solució d'emergència molt més ràpida** i eficaç.

• Allibera RAM per als processos actius, permetent executar més aplicacions simultàniament.

## Diapositiva 8

**DADES FREDES I MASSIVES**

**Emmagatzematge Terciari i Dades Fredes**

• **Sistemes Robotitzats:** Utilitza braços mecànics que carreguen i munten automàticament els mitjans físics.

**Característiques del Terciari**

**Biblioteques de Cintes en Centres de Dades:**

**Exemples i Avantatge Econòmic**

Prioritza l'economia per terabyte i la gran capacitat de retenció a llarg termini per sobre de la velocitat immediata.

• **Velocitat Lenta:** El temps d'accés és alt pel temps mecànic de trobar i carregar la cinta o disc.

• **Dades Fredes (Cold Data):** Dissenyat per a informació massiva (TBs/PBs) a la qual s'accedeix molt raramen.

## Diapositiva 9

**AÏLLAMENT DE SEGURETAT**

**Emmagatzematge Fora de Línia (Offline)**

**Concepte Fora de Línia**

**Utilitats i Exemples**

Mitjà d'emmagatzematge que **no està sota el control de cap unitat de processament (CPU)** ni connectat a la xarxa.

• Transferència fàcil de dades entre sistemes aïllats.

• Realització de còpies de seguretat personals o aïllades de Ransomware (Air-gap).

Per tal d'accedir a la informació cal necessàriament la **intervenció humana** per connectar el dispositiu.

• Discs durs externs, unitats USB o cintes extraïbles guardades en caixes fortes.

## Diapositiva 10

**COMPARTICIÓ EN XARXA**

**Emmagatzematge Distribuït i Protocols de Xarxa**

Desar la informació en servidors de xarxa perquè els equips clients hi accedeixin com si fos un disc local:

**Entorn Windows (SMB)**

**Entorn UNIX/Linux (NFS)**

**Interoperabilitat (SAMBA)**

Utilitza el protocol **SMB (Server Message Block)**, integrat normalment en un entorn de domini amb **Active Directory** per a l'autenticació centralitzada.

Utilitza **NFS (Network File System)**, el protocol clàssic per a la compartició nativa de fitxers d'alta velocitat entre sistemes Linux/UNIX.

Implementació lliure del protocol SMB que permet a clients Windows accedir a servidors Linux i viceversa sense problemes de compatibilitat.

## Diapositiva 11

**ARQUITECTURA DE SERVIDORS**

**Servidors Multitasca vs. Dispositius NAS Dedicats**

**Servidors Completament Configurats**

**Dispositius NAS (Network Attached Storage)**

Equips versàtils d'alt rendiment. A més de compartir fitxers, realitzen tasques complexes:

Dispositius dedicats especialment dissenyats per compartir fitxers en xarxa:

• Allotjar bases de dades corporatives.

• Utilitzen un **sistema operatiu lleuger optimitzat**.

• Funció quasi exclusiva d'emmagatzematge i gestió de volums RAID.

• Gestionar correu electrònic i servidors Web/Aplicació.

• Solució escalable i senzilla per a entorns domèstics, PIMEs i empreses.

## Diapositiva 12

![Imatge 3](@@IMG@@/img-003.jpg){ loading=lazy }

![Imatge 4](@@IMG@@/img-004.png){ loading=lazy }

**Resum d'Estudi - Emmagatzematge i Backups**

La gestió eficaç combina la velocitat de la RAM i SSDs NVMe per a dades meva actives, amb emmagatzematge terciari/offline per a dades fredes, i protocols distribuïts (**SMB, NFS, NAS**) per a la continuïtat de negoci.
