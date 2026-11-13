# Seguretat Física 2.0

<p class="md-kicker">MÒDUL DE SEGURETAT INFORMÀTICA</p>

Material d'estudi detallat: Funcions Hash, Llistes ACL, Polítiques d'Emmagatzematge, Còpies de Seguretat i la Regla 3-2-1

## Funcions Hash i Resum del Missatge

<p class="md-kicker">INTEGRITAT DE DADES</p>

Una **funció hash** és una funció matemàtica que transforma un missatge de qualsevol mida en una cadena de mida fixa (entre 128 i 512 bits). Aquesta empremta única identifica el fitxer.

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### Efecte Avalot

Quasi qualsevol canvi mínim en el fitxer d'origen (encara que sigui modificar un sol caràcter o bit) provoca un **canvi total i impredictible** en el valor resum resultant.

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### Algorismes Actuals

**SHA-2** (SHA-256, SHA-512) desenvolupat per la NSA i **SHA-3** (NIST). Ofereixen el millor balanç entre velocitat i seguretat per a verificació d'integritat i signatures digitals.

</div>

<div class="md-card" style="--card:#EF4444" markdown="1">

### Algorismes Obsolets

**MD5** (128 bits) i **SHA-1** (160 bits) estan completament desaconsellats a causa de vulnerabilitats greus i col·lisions demostrades en trobar fitxers diferents amb el mateix hash.

</div>

</div>

## Matriu d'Accés i Llistes ACL

<p class="md-kicker">AUTORITZACIÓ I PERMISOS</p>

<div class="md-callout" style="--card:#0284C7" markdown="1">

**Principi de Privilegi Mínim: L'usuari ha de tenir accés** ***únicament*** **a aquells recursos indispensables per dur a terme la seva tasca.**

</div>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### Autenticació

Verificació de la identitat de l'usuari o procés en entrar al sistema.

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### Autorització (ACL)

Procés que valida si l'usuari té permís (Lectura, Escriptura, Execució) sobre l'objecte o recurs sol·licitat.

</div>

<div class="md-card" style="--card:#8B5CF6" markdown="1">

### Auditoria (Registre)

Gravació en fitxers de log de totes les accions i l'ús que l'usuari fa dels recursos del sistema.

</div>

</div>

\* En els SO reals (com Windows o Linux), les **Llistes ACL** s'associen directament a cada fitxer/directori indicant quins usuaris i grups hi tenen accés.

## Polítiques d'Emmagatzematge (I)

<p class="md-kicker">GOVERNANÇA CORPORATIVA</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### Emmagatzematge Local

Regula l'ús dels discos durs de les estacions de treball dels empleats:

- Quin tipus d'informació es permet guardar localment.
- Temps màxim de permanència d'aquests fitxers.
- Ubicació exacta dins de l'arbre de directoris autoritzats.
- Prohibició/Normativa sobre la desa de documents personals.

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### Xarxa Corporativa

Servidors d'emmagatzematge centralitzat i compartit (NAS/SAN):

- Permisos d'accés definits per la direcció i els responsables de sistemes.
- Definició clara de les persones encarregades d'actualitzar cada carpeta.
- Regulació dels espais de treball personals assignats en xarxa a cada empleat.

</div>

</div>

## Polítiques d'Emmagatzematge (II)

<p class="md-kicker">GOVERNANÇA CORPORATIVA</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#F59E0B" markdown="1">

### Dispositius Externs (USBs / Discs)

Regula l'ús de suports d'emmagatzematge extraïbles emprats per a transport o còpia personal:

- Autorització explícita sobre si l'ús d'aquests suports està permès o bloquejat.
- Prohibició absoluta d'emmagatzemar-hi dades sensibles o de clients.
- Obligatorietat de xifratge de hardware/software en dispositius portàtils.

</div>

<div class="md-card" style="--card:#EF4444" markdown="1">

### Esborrat Segur i Destrucció

Quan la informació ja no es necessita o el suport arriba al final de la seva vida útil:

- Utilització de mètodes d'esborrat segur (sobrescriptura/wipe de dades).
- Destrucció física irrecuperable de discs durs obsolets per evitar furgat de dades.

</div>

</div>

## Planificació de Còpies de Seguretat

<p class="md-kicker">PLA DE CONTINGÈNCIA</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### 1. Definició i Freqüència

- Identificar quines dades cal preservar prioritàriament.
- Establir la freqüència de realització (diària, setmanal).
- Disposar del magatzem i suports físics adequats.

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### 2. Restauració i Proves

- Planificar al detall el procés de restauració.
- **Provar el sistema exhaustivament:** Una còpia no provada no és una còpia vàlida.
- Cercar la mínima probabilitat d'error en la recuperació.

</div>

<div class="md-card" style="--card:#8B5CF6" markdown="1">

### 3. Vigència i Obsolescència

- Definir el temps de retenció/vigència de cada còpia.
- Controlar l'obsolescència dels suports de memòria.
- Esborrar o destruir els suports en acabar la seva vida útil.

</div>

</div>

## Completa, Incremental i Diferencial

<p class="md-kicker">TIPOLOGIA DE BACKUP</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### Completa (Full)

Duplica **tota** la informació seleccionada del sistema. És la base de qualsevol pla de backup. Temps de realització alt i gran ús d'espai, però restauració molt senzilla.

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### Incremental

Desa **només les dades modificades des de la darrera còpia** (ja sigui completa o incremental). Molt ràpida de fer i d'ús d'espai mínim.

</div>

<div class="md-card" style="--card:#8B5CF6" markdown="1">

### Diferencial

Desa totes les dades modificades **des de la darrera còpia completa**. Ocupa més espai que la incremental, però simplifica i accelera la restauració.

</div>

</div>

## Diapositiva 8

**COMPARATIVA D'ESTUDI**

**Incremental vs Diferencial**

| Criteri d'Avaluació | Còpia Incremental | Còpia Diferencial |
|---|---|---|
| Punt de referència | Darrera còpia (sigui completa o incremental) | Darrera còpia completa realitzada |
| Temps de realització | Molt ràpid (només canvis del dia) | Augmenta gradualment cada dia des de la completa |
| Ús d'espai de memòria | Mínim indispensable | Major que la incremental (acumula canvis) |
| Fitxers per a la restauració | Còpia Completa + Totes les incrementals intermediament | Còpia Completa + Darrera còpia diferencial |
| Risc de fallada en restaurar | Major: si falla una sola còpia intermedia de la cadena, no es pot restaurar bé | Menor: només depèn de dos fitxers (completa i darrera diferencial) |

## La Regla de Còpies de Seguretat 3-2-1

<p class="md-kicker">ESTÀNDARD D'OR DE LA SEGURETAT</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### 3

**Còpies de Dades**

Mantenir les dades originals més almenys **2 còpies de seguretat addicionals** de suport.

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### 2

**Suports Diferents**

Desar aquestes còpies en almenys **dues tecnologies diferents** (ex: Disc local SSD/NAS i Núvol).

</div>

<div class="md-card" style="--card:#EF4444" markdown="1">

### 1

**Còpia Fora de la Seu**

Guardar almenys **una còpia en una ubicació externa (Offsite)** per protegir-se de desastres locals (incendis, robatoris).

</div>

</div>

## Resum d'Estudi - Seguretat Física 2.0

Garanteix la integritat amb funcions Hash modernes (SHA-2/SHA-3), controla l'accés amb ACLs i el principi de privilegi mínim, i assegura la continuïtat del negoci aplicant la **regla 3-2-1** de còpies de seguretat.
