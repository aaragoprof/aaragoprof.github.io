# Sistemes d'Emmagatzematge Redundant (RAID)

## Diapositiva 1

![Imatge 1](@@IMG@@/img-001.jpg){ loading=lazy }

![Imatge 2](@@IMG@@/img-002.png){ loading=lazy }

**Sistemes d'Emmagatzematge Redundant**

**MÒDUL D'EMMAGATZEMATGE I SEGURETAT DE DADES**

Material d'estudi: Concepte RAID, Tolerància a Fallades, Operació XOR, Paritats (RAID 0, 1, 5, 6, 10) i Alta Disponibilitat

## Diapositiva 2

**ARQUITECTURA DE MAQUINARI**

**Introducció als Sistemes RAID**

Un sistema **RAID (Redundant Array of Independent Disks)** agrupa múltiples discos durs físics per formar un únic volum lògic amb major capacitat, rendiment o fiabilitat.

**Divisió i Replicació**

**Rendiment i Velocitat**

**Intercanvi en Calent**

Permet distribuir les dades entre diferents unitats físiques per optimitzar la transferència simultània.

L'accés paral·lel a diversos discos incrementa notablement les velocitats de lectura i escriptura.

Sistemes d'alta disponibilitat que permeten extreure i reemplaçar unitats avariades sense aturar el servidor (Hot-Swap).

## Diapositiva 3

**ACLARIMENT FONAMENTAL**

**Protecció del RAID: Abast i Limitacions**

**RAID PROTEGEIX Contra:**

**RAID NO PROTEGEIX Contra:**

• **Fallada física de discos:** Permet mantenir les dades accessibles i el sistema operatiu actiu si un o més discos s'avarien físicament.

• **Esborrament accidental** o intencionat d'arxius.

• **Continuïtat de servei:** Facilita la reconstrucció automàtica o assistida en substituir el disc avariat.

• **Corrupció lògica** de fitxers o errors de programari.

• **Atacs de Ransomware** o malware que xifren el volum.

• **Desastres ambientals** (incendis, inundacions) o robatori.

## Diapositiva 4

**TÈCNIQUES DE PROTECCIÓ**

**Redundància: Mirall (Mirror) vs. Paritat**

**Mirall (Mirroring)**

**Paritat (Parity)**

Consisteix a duplicar la informació de manera idèntica en dos o més discos.

S'escriuen dades addicionals calculades matemàticament per permetre la reconstrucció de blocs perduts.

• Proporciona alta velocitat de lectura.

• **Inconvenient:** La capacitat útil es redueix al 50%.

• Optimitza l'aprofitament de l'espai útil del conjunt.

• Idealment requereix discos de la mateixa capacitat.

## Diapositiva 5

**FONAMENT MATEMÀTIC**

**Càlcul de Paritat mitjançant la Funció XOR (⊕)**

**Taula XOR Binària**

**Reconstrucció Matemàtica**

| Entrada A | Entrada B | Paritat P (A ⊕ B) |
|---|---|---|
| 0 | 0 | 0 (Iguals) |
| 0 | 1 | 1 (Diferents) |
| 1 | 0 | 1 (Diferents) |
| 1 | 1 | 0 (Iguals) |

La propietat de la funció XOR permet aïllar qualsevol element quan un d'ells falta:

**• Si es perd A → A = B ⊕ P**   
 **• Si es perd B → B = A ⊕ P**   
 **• Càlcul de Paritat → P = A ⊕ B**

## Diapositiva 6

**NIVELLS ESTÀNDARD**

**RAID 0: Striping (Sense Redundància)**

**Rendiment Elevat**

**Risc Total**

Distribueix les dades equitativament en blocs alternats entre dos o més discos.

**No conté paritat:** Si falla un sol disc, es perden totes les dades del conjunt.

• **Mínim de discos:** 2 unitats.

• **Capacitat útil:** 100% de la suma dels discos.

• Escriu i llegeix dades en paral·lel.

## Diapositiva 7

**NIVELLS ESTÀNDARD**

**RAID 1: Mirroring (Còpia en Mirall)**

**Replicació Total**

**Capacitat Reutilitzable**

Guarda la mateixa informació exacta en dos o més discos simultàniament.

La capacitat total equival a la mida de la unitat més petita (50% d'eficiència espacial).

• **Mínim de discos:** 2 unitats.

• **Lectura:** Accelerada en consultar ambdós discos a la vegada.

• **Tolerància:** Suporta la fallada d'1 disc de la parella.

## Diapositiva 8

**NIVELLS ESTÀNDARD**

**RAID 5: Paritat Distribuïda (N - 1)**

**Paritat Rotativa**

**Equilibri General**

Distribueix les dades i el bloc de paritat corresponent entre totes les unitats de la matriu.

És la solució més estesa en servidors de fitxers per la seva relació cost-seguretat.

• **Mínim de discos:** 3 unitats.

• **Capacitat útil:** N - 1 discos.

• **Tolerància:** Admet la pèrdua d'1 disc.

## Diapositiva 9

**NIVELLS ESTÀNDARD**

**RAID 6: Doble Paritat Distribuïda (N - 2)**

**Doble Paritat (P i Q)**

**Maximització de Disponibilitat**

Calcula dos blocs de paritat independents distribuïts rotativament.

Dissenyat per a entorns on la pèrdua de dades és completament inacceptable.

• **Mínim de discos:** 4 unitats.

• **Tolerància:** Suporta la fallada simultània de **2 discos**.

• **Capacitat útil:** N - 2 discos.

## Diapositiva 10

**NIVELLS HÍBRIDS**

**RAID 10 (1+0): Mirall i Distribució**

**Mètode Híbrid**

**Entorns Crítics**

Combina blocs en mirall (RAID 1) agrupats en un volum distribuït (RAID 0).

Recomanat per a servidors de bases de dades d'alta freqüència de transaccions.

• **Mínim de discos:** 4 unitats.

• **Capacitat útil:** 50% de la capacitat total.

• Excel·lent velocitat d'E/S sense penalització de càlcul de paritats.

## Diapositiva 11

**TAULA DE SINTESI**

**Comparativa de Característiques RAID**

| Nivell | Mínim Discos | Tolerància a Fallades | Capacitat Útil | Benefici Principal |
|---|---|---|---|---|
| RAID 0 | 2 | 0 discos | 100% | Velocitat màxima de lectura/escriptura. |
| RAID 1 | 2 | 1 disc per parella | 50% | Simplicitat i redundància directa. |
| RAID 5 | 3 | 1 disc | N - 1 discos | Equilibri eficient de capacitat i cost. |
| RAID 6 | 4 | 2 discos | N - 2 discos | Protecció contra doble fallada física. |
| RAID 10 | 4 | 1 per subconjunt mirall | 50% | Màxim rendiment d'E/S amb alta seguretat. |

## Diapositiva 12

![Imatge 3](@@IMG@@/img-003.jpg){ loading=lazy }

![Imatge 4](@@IMG@@/img-004.png){ loading=lazy }

**Resum d'Estudi - Sistemes RAID**

Els sistemes RAID són indispensables per a la continuïtat de negoci i la tolerància a fallades físiques de maquinari, però **sempre han de ser complementats amb una estratègia de còpies de seguretat (backups)**.
