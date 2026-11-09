# Gestió del Procés de Còpies de Seguretat

<p class="md-kicker">MÒDUL D'ADMINISTRACIÓ I PLANIFICACIÓ DE BACKUPS</p>

Material d'estudi: Models de Backup (Incremental vs Diferencial), Imatges de Sistema, Finestra de Còpia, Limitacions i Checksums vs Hashes

## Objectius del Procés de Còpia de Seguretat

<p class="md-kicker">OBJECTIUS OPERATIUS</p>

La creació d'una còpia de seguretat és un procés continu i dinàmic que s'ha d'actualitzar a mesura que es modifiquen les dades originals. Tant usuaris domèstics com empreses comparteixen objectius fonamentals:

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### Recuperació en un Punt Temporal

Permet conservar l'estat exacte de les dades en un moment determinat del temps per poder tornar enrere si es produeix una fallada o corrupció.

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### Protecció contra Accés No Autoritzat

Les còpies s'han de protegir per evitar que usuaris no autoritzats puguin accedir-hi o robar-les en cas de pèrdua dels arxius originals.

</div>

<div class="md-card" style="--card:#8B5CF6" markdown="1">

### Garantia de Restauració

Un sistema de còpies només és tan bo com la seva **estratègia de restauració**. Cal validar contínuament que la recuperació sigui funcional.

</div>

</div>

## Cas Pràctic: Còpia Incremental (Dia a Dia)

<p class="md-kicker">AVALUACIÓ NUMÈRICA DE MODELS</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### Escenari de Dades (Base 100 GB)

Tenim una base inicial de **100 GB el Diumenge** i cada dia es modifiquen o s'afegeixen **10 GB** de dades noves.

- **Diumenge:** Còpia Completa → **100 GB**
- **Dilluns:** Incremental (canvis dilluns) → **10 GB**
- **Dimarts:** Incremental (canvis dimarts) → **10 GB**
- **Dimecres:** Incremental (canvis dimecres) → **10 GB**

</div>

<div class="md-card" style="--card:#EF4444" markdown="1">

### Procés de Restauració

Per restaurar l'estat del Dimecres es necessiten:

<div class="md-callout" style="--card:#EF4444" markdown="1">

**Completa Diumenge + Inc. Dilluns + Inc. Dimarts + Inc. Dimecres (4 fitxers en total).**

</div>

\* Risc: Si una sola còpia de la cadena falla, la restauració no es pot dur a terme.

</div>

</div>

## Cas Pràctic: Còpia Diferencial (Acumulativa)

<p class="md-kicker">AVALUACIÓ NUMÈRICA DE MODELS</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#16A34A" markdown="1">

### Escenari de Dades (Base 100 GB)

Cada dia guarda **tots els canvis acumulats** des de la darrera còpia completa del diumenge:

- **Diumenge:** Còpia Completa → **100 GB**
- **Dilluns:** Diferencial (canvis dilluns) → **10 GB**
- **Dimarts:** Diferencial (dilluns + dimarts) → **20 GB**
- **Dimecres:** Diferencial (dilluns + dimarts + dimecres) → **30 GB**

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### Procés de Restauració

Per restaurar l'estat del Dimecres només calen:

<div class="md-callout" style="--card:#22C55E" markdown="1">

**Completa Diumenge + Diferencial Dimecres (Només 2 fitxers en total).**

</div>

✓ Avantatge: Restauració molt més ràpida i amb menor risc de fallada.

</div>

</div>

## Imatges del Sistema vs. Punts de Restauració

<p class="md-kicker">RECUPERACIÓ DEL SISTEMA</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### Imatge del Sistema (System Image)

Còpia exacta bloc a bloc de tot el sistema informàtic:

- Inclou SO, particions, aplicacions instal·lades i configuracions de serveis.
- Permet reinstal·lacions completes molt més ràpides des de zero en cas de fallada total del disc duro.

</div>

<div class="md-card" style="--card:#8B5CF6" markdown="1">

### Punt de Restauració (Restore Point)

Instantània de l'estat del sistema operatiu:

- Còpia fitxers de sistema, registre del SO, configuracions i controladors (drivers).
- Permet tornar a un estat anterior estable sense haver de reinstal·lar el SO complet.

</div>

</div>

## Finestra de Còpia i Impacte en el Rendiment

<p class="md-kicker">RESTRICCIONS TÈCNIQUES</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#F59E0B" markdown="1">

### Finestra de Còpia (Backup Window)

Interval de temps durant el qual es planifica l'execució de les còpies de seguretat.

- S'ha de planificar en hores d'inactivitat per no interrompre els usuaris.
- Si la duració es prolonga massa, cal decidir si avortar o deixar que acabi afectant l'horari d'oficina.

</div>

<div class="md-card" style="--card:#EF4444" markdown="1">

### Impacte en el Rendiment

Qualsevol procés de còpia utilitza recursos de CPU, lectura de disc i memòria RAM.

L'execució de backups durant l'activitat normal pot ralentitzar greument les aplicacions de producció.

</div>

</div>

## Costos HW/SW i Amplada de Banda de Xarxa

<p class="md-kicker">RESTRICCIONS TÈCNIQUES</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### Cost de HW i SW

- **Capacitat d'Emmagatzematge:** Els suports tenen un cost financer. Cal preveure el creixement de dades a mitjà/llarg termini.
- **Cost de Software:** Llicències de programari específic d'alta disponibilitat o de gestió empresarial.

</div>

<div class="md-card" style="--card:#8B5CF6" markdown="1">

### Amplada de Banda de Xarxa

Els backups distribuïts cap a NAS, servidors remots o el Núvol utilitzen la xarxa intensivament.

Un volum massiu de dades pot saturar els enllaços de xarxa i reduir el rendiment per a la resta de serveis corporatius.

</div>

</div>

## Planificació i Seguretat en la Implementació

<p class="md-kicker">BONES PRÀCTIQUES</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#16A34A" markdown="1">

### Planificació Automàtica

Cal utilitzar un planificador de tasques integrat per automatitzar la creació periòdica.

<div class="md-callout" style="--card:#22C55E" markdown="1">

**Les còpies manuals estan subjectes a errors humans i oblits catastròfics.**

</div>

</div>

<div class="md-card" style="--card:#0284C7" markdown="1">

### Autenticació i Accés

Política estricta d'accés per protegir el repositori de backups:

- Evita intromissions no autoritzades a les còpies emmagatzemades.
- Protegeix la informació mitjançant credencials i xifratge.

</div>

</div>

## Mesura, Monitoratge i Informes de Còpia

<p class="md-kicker">CONTROL DE QUALITAT</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### Validació de les Còpies

Procediments de verificació per assegurar que la còpia s'ha creat correctament i que les dades són 100% íntegres.

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### Creació d'Informes i Logs

Revisió dels historials generats automàticament per l'ordinador per detectar errors, omissions o canvis no previstos.

</div>

<div class="md-card" style="--card:#8B5CF6" markdown="1">

### Verificació per Suma de Bits

Utilització d'algorismes de verificació per comparar les dades d'origen i destinació byte a byte.

</div>

</div>

## Diferència entre Checksum i Hash Criptogràfic

<p class="md-kicker">CONCEPTE TEÒRIC CLAU</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### Checksum (Suma de Verificació)

Dissenyat principalment per detectar **canvis accidentals** en les dades (errors d'escriptura al disc o soroll de xarxa).

Ex: CRC32, sumes de comprovació simples.

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### Hash Criptogràfic

Dissenyat específicament per protegir contra **canvis maliciosos i alteracions intencionades**.

Ex: SHA-256, SHA-3. Impossibilita generar col·lisions falses.

</div>

</div>

## Consells Pràctics i Formats Oberts

<p class="md-kicker">BONES PRÀCTIQUES FINALS</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#EF4444" markdown="1">

### Separació de Mitjans

**Mai no és aconsellable** desar les còpies de seguretat dins del mateix disc o sistema del qual s'ha fet la còpia.

</div>

<div class="md-card" style="--card:#0284C7" markdown="1">

### Formats Oberts

Emmagatzemar les dades en formats oberts i no propietaris per facilitar la recuperació en el futur sense dependre d'un software concret.

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### Automatització

Automatitzar la creació de backups per evitar la dependència d'execucions manuals subjectes a oblits i errors.

</div>

</div>

## Resum d'Estudi - Gestió de Backups

Una gestió eficaç de backups combina una tria adequada del model (**Incremental vs Diferencial**), la gestió de la **finestra de còpia** i l'amplada de banda, l'automatització planificada, la verificació d'integritat amb **hashes** i l'emmagatzematge en mitjans externs i formats oberts.
