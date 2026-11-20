# Sistemes d'Emmagatzematge Redundant

<p class="md-kicker">MÒDUL D'EMMAGATZEMATGE I SEGURETAT DE DADES</p>

Material d'estudi: Concepte RAID, Tolerància a Fallades, Operació XOR, Paritats (RAID 0, 1, 5, 6, 10) i Alta Disponibilitat

## Introducció als Sistemes RAID

<p class="md-kicker">ARQUITECTURA DE MAQUINARI</p>

Un sistema **RAID (Redundant Array of Independent Disks)** agrupa múltiples discos durs físics per formar un únic volum lògic amb major capacitat, rendiment o fiabilitat.

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### Divisió i Replicació

Permet distribuir les dades entre diferents unitats físiques per optimitzar la transferència simultània.

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### Rendiment i Velocitat

L'accés paral·lel a diversos discos incrementa notablement les velocitats de lectura i escriptura.

</div>

<div class="md-card" style="--card:#8B5CF6" markdown="1">

### Intercanvi en Calent

Sistemes d'alta disponibilitat que permeten extreure i reemplaçar unitats avariades sense aturar el servidor (Hot-Swap).

</div>

</div>

## Protecció del RAID: Abast i Limitacions

<p class="md-kicker">ACLARIMENT FONAMENTAL</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#16A34A" markdown="1">

### RAID PROTEGEIX Contra:

- **Fallada física de discos:** Permet mantenir les dades accessibles i el sistema operatiu actiu si un o més discos s'avarien físicament.
- **Continuïtat de servei:** Facilita la reconstrucció automàtica o assistida en substituir el disc avariat.

</div>

<div class="md-card" style="--card:#EF4444" markdown="1">

### RAID NO PROTEGEIX Contra:

- **Esborrament accidental** o intencionat d'arxius.
- **Corrupció lògica** de fitxers o errors de programari.
- **Atacs de Ransomware** o malware que xifren el volum.
- **Desastres ambientals** (incendis, inundacions) o robatori.

</div>

</div>

## Redundància: Mirall (Mirror) vs. Paritat

<p class="md-kicker">TÈCNIQUES DE PROTECCIÓ</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### Mirall (Mirroring)

Consisteix a duplicar la informació de manera idèntica en dos o més discos.

- Proporciona alta velocitat de lectura.
- **Inconvenient:** La capacitat útil es redueix al 50%.

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### Paritat (Parity)

S'escriuen dades addicionals calculades matemàticament per permetre la reconstrucció de blocs perduts.

- Optimitza l'aprofitament de l'espai útil del conjunt.
- Idealment requereix discos de la mateixa capacitat.

</div>

</div>

## Càlcul de Paritat mitjançant la Funció XOR (⊕)

<p class="md-kicker">FONAMENT MATEMÀTIC</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### Taula XOR Binària

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### Reconstrucció Matemàtica

La propietat de la funció XOR permet aïllar qualsevol element quan un d'ells falta:

<div class="md-callout" style="--card:#BAE6FD" markdown="1">

- **Si es perd A → A = B ⊕ P**   
 **• Si es perd B → B = A ⊕ P**   
 **• Càlcul de Paritat → P = A ⊕ B**

</div>

</div>

</div>

| Entrada A | Entrada B | Paritat P (A ⊕ B) |
|---|---|---|
| 0 | 0 | 0 (Iguals) |
| 0 | 1 | 1 (Diferents) |
| 1 | 0 | 1 (Diferents) |
| 1 | 1 | 0 (Iguals) |

## RAID 0: Striping (Sense Redundància)

<p class="md-kicker">NIVELLS ESTÀNDARD</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### Rendiment Elevat

Distribueix les dades equitativament en blocs alternats entre dos o més discos.

- **Mínim de discos:** 2 unitats.
- **Capacitat útil:** 100% de la suma dels discos.
- Escriu i llegeix dades en paral·lel.

</div>

<div class="md-card" style="--card:#EF4444" markdown="1">

### Risc Total

**No conté paritat:** Si falla un sol disc, es perden totes les dades del conjunt.

</div>

</div>

## RAID 1: Mirroring (Còpia en Mirall)

<p class="md-kicker">NIVELLS ESTÀNDARD</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#16A34A" markdown="1">

### Replicació Total

Guarda la mateixa informació exacta en dos o més discos simultàniament.

- **Mínim de discos:** 2 unitats.
- **Lectura:** Accelerada en consultar ambdós discos a la vegada.
- **Tolerància:** Suporta la fallada d'1 disc de la parella.

</div>

<div class="md-card" style="--card:#F59E0B" markdown="1">

### Capacitat Reutilitzable

La capacitat total equival a la mida de la unitat més petita (50% d'eficiència espacial).

</div>

</div>

## RAID 5: Paritat Distribuïda (N - 1)

<p class="md-kicker">NIVELLS ESTÀNDARD</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### Paritat Rotativa

Distribueix les dades i el bloc de paritat corresponent entre totes les unitats de la matriu.

- **Mínim de discos:** 3 unitats.
- **Capacitat útil:** N - 1 discos.
- **Tolerància:** Admet la pèrdua d'1 disc.

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### Equilibri General

És la solució més estesa en servidors de fitxers per la seva relació cost-seguretat.

</div>

</div>

## RAID 6: Doble Paritat Distribuïda (N - 2)

<p class="md-kicker">NIVELLS ESTÀNDARD</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#8B5CF6" markdown="1">

### Doble Paritat (P i Q)

Calcula dos blocs de paritat independents distribuïts rotativament.

- **Mínim de discos:** 4 unitats.
- **Tolerància:** Suporta la fallada simultània de **2 discos**.
- **Capacitat útil:** N - 2 discos.

</div>

<div class="md-card" style="--card:#0284C7" markdown="1">

### Maximització de Disponibilitat

Dissenyat per a entorns on la pèrdua de dades és completament inacceptable.

</div>

</div>

## RAID 10 (1+0): Mirall i Distribució

<p class="md-kicker">NIVELLS HÍBRIDS</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#16A34A" markdown="1">

### Mètode Híbrid

Combina blocs en mirall (RAID 1) agrupats en un volum distribuït (RAID 0).

- **Mínim de discos:** 4 unitats.
- **Capacitat útil:** 50% de la capacitat total.
- Excel·lent velocitat d'E/S sense penalització de càlcul de paritats.

</div>

<div class="md-card" style="--card:#0284C7" markdown="1">

### Entorns Crítics

Recomanat per a servidors de bases de dades d'alta freqüència de transaccions.

</div>

</div>

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

## Resum d'Estudi - Sistemes RAID

Els sistemes RAID són indispensables per a la continuïtat de negoci i la tolerància a fallades físiques de maquinari, però **sempre han de ser complementats amb una estratègia de còpies de seguretat (backups)**.
