# Gestió de Còpies de Seguretat

## Diapositiva 1

![Imatge 1](@@IMG@@/img-001.jpg){ loading=lazy }

![Imatge 2](@@IMG@@/img-002.png){ loading=lazy }

**Gestió del Procés de Còpies de Seguretat**

**MÒDUL D'ADMINISTRACIÓ I PLANIFICACIÓ DE BACKUPS**

Material d'estudi: Models de Backup (Incremental vs Diferencial), Imatges de Sistema, Finestra de Còpia, Limitacions i Checksums vs Hashes

## Diapositiva 2

**OBJECTIUS OPERATIUS**

**Objectius del Procés de Còpia de Seguretat**

La creació d'una còpia de seguretat és un procés continu i dinàmic que s'ha d'actualitzar a mesura que es modifiquen les dades originals. Tant usuaris domèstics com empreses comparteixen objectius fonamentals:

**Recuperació en un Punt Temporal**

**Protecció contra Accés No Autoritzat**

**Garantia de Restauració**

Permet conservar l'estat exacte de les dades en un moment determinat del temps per poder tornar enrere si es produeix una fallada o corrupció.

Un sistema de còpies només és tan bo com la seva **estratègia de restauració**. Cal validar contínuament que la recuperació sigui funcional.

Les còpies s'han de protegir per evitar que usuaris no autoritzats puguin accedir-hi o robar-les en cas de pèrdua dels arxius originals.

## Diapositiva 3

**AVALUACIÓ NUMÈRICA DE MODELS**

**Cas Pràctic: Còpia Incremental (Dia a Dia)**

Tenim una base inicial de **100 GB el Diumenge** i cada dia es modifiquen o s'afegeixen **10 GB** de dades noves.

**Escenari de Dades (Base 100 GB)**

Per restaurar l'estat del Dimecres es necessiten:

**Procés de Restauració**

**Completa Diumenge + Inc. Dilluns + Inc. Dimarts + Inc. Dimecres (4 fitxers en total).**

• **Diumenge:** Còpia Completa → **100 GB**

• **Dilluns:** Incremental (canvis dilluns) → **10 GB**

• **Dimarts:** Incremental (canvis dimarts) → **10 GB**

\* Risc: Si una sola còpia de la cadena falla, la restauració no es pot dur a terme.

• **Dimecres:** Incremental (canvis dimecres) → **10 GB**

## Diapositiva 4

**AVALUACIÓ NUMÈRICA DE MODELS**

**Cas Pràctic: Còpia Diferencial (Acumulativa)**

Cada dia guarda **tots els canvis acumulats** des de la darrera còpia completa del diumenge:

**Escenari de Dades (Base 100 GB)**

Per restaurar l'estat del Dimecres només calen:

**Procés de Restauració**

**Completa Diumenge + Diferencial Dimecres (Només 2 fitxers en total).**

• **Diumenge:** Còpia Completa → **100 GB**

• **Dilluns:** Diferencial (canvis dilluns) → **10 GB**

✓ Avantatge: Restauració molt més ràpida i amb menor risc de fallada.

• **Dimarts:** Diferencial (dilluns + dimarts) → **20 GB**

• **Dimecres:** Diferencial (dilluns + dimarts + dimecres) → **30 GB**

## Diapositiva 5

**RECUPERACIÓ DEL SISTEMA**

**Imatges del Sistema vs. Punts de Restauració**

**Imatge del Sistema (System Image)**

**Punt de Restauració (Restore Point)**

Còpia exacta bloc a bloc de tot el sistema informàtic:

• Inclou SO, particions, aplicacions instal·lades i configuracions de serveis.

Instantània de l'estat del sistema operatiu:

• Còpia fitxers de sistema, registre del SO, configuracions i controladors (drivers).

• Permet reinstal·lacions completes molt més ràpides des de zero en cas de fallada total del disc duro.

• Permet tornar a un estat anterior estable sense haver de reinstal·lar el SO complet.

## Diapositiva 6

**RESTRICCIONS TÈCNIQUES**

**Finestra de Còpia i Impacte en el Rendiment**

**Finestra de Còpia (Backup Window)**

**Impacte en el Rendiment**

Interval de temps durant el qual es planifica l'execució de les còpies de seguretat.

Qualsevol procés de còpia utilitza recursos de CPU, lectura de disc i memòria RAM.

• S'ha de planificar en hores d'inactivitat per no interrompre els usuaris.

• Si la duració es prolonga massa, cal decidir si avortar o deixar que acabi afectant l'horari d'oficina.

L'execució de backups durant l'activitat normal pot ralentitzar greument les aplicacions de producció.

## Diapositiva 7

**RESTRICCIONS TÈCNIQUES**

**Costos HW/SW i Amplada de Banda de Xarxa**

**Cost de HW i SW**

**Amplada de Banda de Xarxa**

• **Capacitat d'Emmagatzematge:** Els suports tenen un cost financer. Cal preveure el creixement de dades a mitjà/llarg termini.

Els backups distribuïts cap a NAS, servidors remots o el Núvol utilitzen la xarxa intensivament.

• **Cost de Software:** Llicències de programari específic d'alta disponibilitat o de gestió empresarial.

Un volum massiu de dades pot saturar els enllaços de xarxa i reduir el rendiment per a la resta de serveis corporatius.

## Diapositiva 8

**BONES PRÀCTIQUES**

**Planificació i Seguretat en la Implementació**

**Planificació Automàtica**

**Autenticació i Accés**

Cal utilitzar un planificador de tasques integrat per automatitzar la creació periòdica.

Política estricta d'accés per protegir el repositori de backups:

• Evita intromissions no autoritzades a les còpies emmagatzemades.

**Les còpies manuals estan subjectes a errors humans i oblits catastròfics.**

• Protegeix la informació mitjançant credencials i xifratge.

## Diapositiva 9

**CONTROL DE QUALITAT**

**Mesura, Monitoratge i Informes de Còpia**

**Validació de les Còpies**

**Creació d'Informes i Logs**

**Verificació per Suma de Bits**

Procediments de verificació per assegurar que la còpia s'ha creat correctament i que les dades són 100% íntegres.

Revisió dels historials generats automàticament per l'ordinador per detectar errors, omissions o canvis no previstos.

Utilització d'algorismes de verificació per comparar les dades d'origen i destinació byte a byte.

## Diapositiva 10

**CONCEPTE TEÒRIC CLAU**

**Diferència entre Checksum i Hash Criptogràfic**

Dissenyat principalment per detectar **canvis accidentals** en les dades (errors d'escriptura al disc o soroll de xarxa).

**Checksum (Suma de Verificació)**

Dissenyat específicament per protegir contra **canvis maliciosos i alteracions intencionades**.

**Hash Criptogràfic**

Ex: CRC32, sumes de comprovació simples.

Ex: SHA-256, SHA-3. Impossibilita generar col·lisions falses.

## Diapositiva 11

**BONES PRÀCTIQUES FINALS**

**Consells Pràctics i Formats Oberts**

**Separació de Mitjans**

**Formats Oberts**

**Automatització**

**Mai no és aconsellable** desar les còpies de seguretat dins del mateix disc o sistema del qual s'ha fet la còpia.

Emmagatzemar les dades en formats oberts i no propietaris per facilitar la recuperació en el futur sense dependre d'un software concret.

Automatitzar la creació de backups per evitar la dependència d'execucions manuals subjectes a oblits i errors.

## Diapositiva 12

![Imatge 3](@@IMG@@/img-003.jpg){ loading=lazy }

![Imatge 4](@@IMG@@/img-004.png){ loading=lazy }

**Resum d'Estudi - Gestió de Backups**

Una gestió eficaç de backups combina una tria adequada del model (**Incremental vs Diferencial**), la gestió de la **finestra de còpia** i l'amplada de banda, l'automatització planificada, la verificació d'integritat amb **hashes** i l'emmagatzematge en mitjans externs i formats oberts.
