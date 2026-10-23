---
description: Implementació de nivells RAID (0, 1, 5, 6, 10), càlculs de paritat XOR i tolerància a fallades del maquinari.
pdf: ""
---

# Sistemes d'emmagatzematge redundant (RAID)

## Introducció

Els sistemes d'emmagatzematge redundant s'implementen mitjançant **RAID** (*Redundant Array of Independent Disks*). Permeten assolir alts graus de fiabilitat i velocitat a partir d'un conjunt de discos durs de baix cost.

!!! note "Què protegeix i què NO protegeix un RAID"
    * **SI protegeix contra:** La fallada física d'un o més discs. El sistema pot continuar funcionant i permet la substitució del disc en calent (*hot-swap*).
    * **NO protegeix contra:** Esborrament accidental de fitxers, corrupció lògica de dades, atacs de *ransomware* o virus, ni desastres naturals/robatori.

## La paritat i la funció XOR

La redundància s'aconsegueix escrivint la mateixa informació en diversos discos (*mirror*) o mitjançant informació de **paritat**.

La paritat es calcula utilitzant l'operació lògica **XOR ($\oplus$)**:
* Si les dades binàries són iguals el resultat és **0**, si són diferents és **1**.
* **Propietat de recuperació:** Si es perd qualsevol dels valors, es pot reconstruir amb els altres:
    $$\text{Si es perd A: } A = B \oplus P$$
    $$\text{Si es perd B: } B = A \oplus P$$
    $$\text{Si es perd P: } P = A \oplus B$$

| A | B | A $\oplus$ B (Paritat P) |
|---|---|---|
| 0 | 0 | 0 (Iguals) |
| 0 | 1 | 1 (Diferents) |
| 1 | 0 | 1 (Diferents) |
| 1 | 1 | 0 (Iguals) |

## Nivells de RAID

### RAID 0 (Striping)
Distribueix les dades equitativament entre dos o més discos sense paritat ni redundància.
* **Mínim de discos:** 2
* **Avantatges:** Alt rendiment d'escriptura i lectura paral·lela.
* **Inconvenients:** No té tolerància a fallades; si falla un disc, es perden totes les dades.

### RAID 1 (Mirroring)
Crea una còpia exacta (mirall) de les dades en dos o més discos.
* **Mínim de discos:** 2
* **Capacitat utilitzable:** 50% (la mida del disc més petit).
* **Tolerància a fallades:** 1 disc (en matriu de 2 discs).

### RAID 5 (Distributed Parity)
Distribueix les dades i una informació de paritat de forma rotativa entre tots els discos.
* **Mínim de discos:** 3
* **Capacitat utilitzable:** $N - 1$ discos (on $N$ és el nombre total de discos).
* **Tolerància a fallades:** 1 disc.

### RAID 6 (Double Parity)
Extensió del RAID 5 que calcula dues paritats independents ($P$ i $Q$) distribuïdes entre els discos.
* **Mínim de discos:** 4
* **Capacitat utilitzable:** $N - 2$ discos.
* **Tolerància a fallades:** 2 discos simultanis.

### RAID 10 / RAID 1+0
Nivell híbrid que combina la velocitat del RAID 0 amb la redundància del RAID 1.
* **Mínim de discos:** 4
* **Capacitat utilitzable:** 50% de la capacitat total.
* **Avantatges:** El màxim rendiment de lectura/escriptura juntament amb alta tolerància a fallades.

## Taula resum dels nivells RAID

| Nivell RAID | Mínim de Discos | Tolerància a fallades | Capacitat Aprofitada | Principal ús |
|---|---|---|---|---|
| **RAID 0** | 2 | 0 discos | 100% | Alt rendiment on les dades no són crítiques. |
| **RAID 1** | 2 | 1 disc | 50% | Seguretat en sistemes petits o discs de SO. |
| **RAID 5** | 3 | 1 disc | $N - 1$ | Servidors de fitxers i emmagatzematge general. |
| **RAID 6** | 4 | 2 discos | $N - 2$ | Entorns on l'alta disponibilitat és crítica. |
| **RAID 10** | 4 | 1 disc per cada parell en mirall | 50% | Aplicacions d'alt rendiment i màxima seguretat. |