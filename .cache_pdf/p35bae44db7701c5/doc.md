# Seguretat Física 2.0 - Material d'Estudi Ampliat

## Diapositiva 1

![Imatge 1](@@IMG@@/img-001.jpg){ loading=lazy }

![Imatge 2](@@IMG@@/img-002.png){ loading=lazy }

**Seguretat Física 2.0**

**MÒDUL DE SEGURETAT INFORMÀTICA**

Material d'estudi detallat: Funcions Hash, Llistes ACL, Polítiques d'Emmagatzematge, Còpies de Seguretat i la Regla 3-2-1

## Diapositiva 2

**INTEGRITAT DE DADES**

**Funcions Hash i Resum del Missatge**

Una **funció hash** és una funció matemàtica que transforma un missatge de qualsevol mida en una cadena de mida fixa (entre 128 i 512 bits). Aquesta empremta única identifica el fitxer.

**Efecte Avalot**

**Algorismes Actuals**

**Algorismes Obsolets**

Quasi qualsevol canvi mínim en el fitxer d'origen (encara que sigui modificar un sol caràcter o bit) provoca un **canvi total i impredictible** en el valor resum resultant.

**SHA-2** (SHA-256, SHA-512) desenvolupat per la NSA i **SHA-3** (NIST). Ofereixen el millor balanç entre velocitat i seguretat per a verificació d'integritat i signatures digitals.

**MD5** (128 bits) i **SHA-1** (160 bits) estan completament desaconsellats a causa de vulnerabilitats greus i col·lisions demostrades en trobar fitxers diferents amb el mateix hash.

## Diapositiva 3

**AUTORITZACIÓ I PERMISOS**

**Matriu d'Accés i Llistes ACL**

**Principi de Privilegi Mínim: L'usuari ha de tenir accés** ***únicament*** **a aquells recursos indispensables per dur a terme la seva tasca.**

**Autenticació**

**Autorització (ACL)**

**Auditoria (Registre)**

Verificació de la identitat de l'usuari o procés en entrar al sistema.

Procés que valida si l'usuari té permís (Lectura, Escriptura, Execució) sobre l'objecte o recurs sol·licitat.

Gravació en fitxers de log de totes les accions i l'ús que l'usuari fa dels recursos del sistema.

\* En els SO reals (com Windows o Linux), les **Llistes ACL** s'associen directament a cada fitxer/directori indicant quins usuaris i grups hi tenen accés.

## Diapositiva 4

**GOVERNANÇA CORPORATIVA**

**Polítiques d'Emmagatzematge (I)**

**Emmagatzematge Local**

**Xarxa Corporativa**

Regula l'ús dels discos durs de les estacions de treball dels empleats:

Servidors d'emmagatzematge centralitzat i compartit (NAS/SAN):

• Quin tipus d'informació es permet guardar localment.

• Permisos d'accés definits per la direcció i els responsables de sistemes.

• Temps màxim de permanència d'aquests fitxers.

• Ubicació exacta dins de l'arbre de directoris autoritzats.

• Definició clara de les persones encarregades d'actualitzar cada carpeta.

• Prohibició/Normativa sobre la desa de documents personals.

• Regulació dels espais de treball personals assignats en xarxa a cada empleat.

## Diapositiva 5

**GOVERNANÇA CORPORATIVA**

**Polítiques d'Emmagatzematge (II)**

Regula l'ús de suports d'emmagatzematge extraïbles emprats per a transport o còpia personal:

**Dispositius Externs (USBs / Discs)**

Quan la informació ja no es necessita o el suport arriba al final de la seva vida útil:

**Esborrat Segur i Destrucció**

• Utilització de mètodes d'esborrat segur (sobrescriptura/wipe de dades).

• Autorització explícita sobre si l'ús d'aquests suports està permès o bloquejat.

• Destrucció física irrecuperable de discs durs obsolets per evitar furgat de dades.

• Prohibició absoluta d'emmagatzemar-hi dades sensibles o de clients.

• Obligatorietat de xifratge de hardware/software en dispositius portàtils.

## Diapositiva 6

**PLA DE CONTINGÈNCIA**

**Planificació de Còpies de Seguretat**

• Identificar quines dades cal preservar prioritàriament.

**1. Definició i Freqüència**

• Planificar al detall el procés de restauració.

**2. Restauració i Proves**

• Definir el temps de retenció/vigència de cada còpia.

**3. Vigència i Obsolescència**

• **Provar el sistema exhaustivament:** Una còpia no provada no és una còpia vàlida.

• Establir la freqüència de realització (diària, setmanal).

• Cercar la mínima probabilitat d'error en la recuperació.

• Controlar l'obsolescència dels suports de memòria.

• Disposar del magatzem i suports físics adequats.

• Esborrar o destruir els suports en acabar la seva vida útil.

## Diapositiva 7

**TIPOLOGIA DE BACKUP**

**Completa, Incremental i Diferencial**

**Completa (Full)**

**Incremental**

**Diferencial**

Duplica **tota** la informació seleccionada del sistema. És la base de qualsevol pla de backup. Temps de realització alt i gran ús d'espai, però restauració molt senzilla.

Desa **només les dades modificades des de la darrera còpia** (ja sigui completa o incremental). Molt ràpida de fer i d'ús d'espai mínim.

Desa totes les dades modificades **des de la darrera còpia completa**. Ocupa més espai que la incremental, però simplifica i accelera la restauració.

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

## Diapositiva 9

**ESTÀNDARD D'OR DE LA SEGURETAT**

**La Regla de Còpies de Seguretat 3-2-1**

**3**

**2**

**1**

**Còpies de Dades**

Mantenir les dades originals més almenys **2 còpies de seguretat addicionals** de suport.

**Suports Diferents**

Desar aquestes còpies en almenys **dues tecnologies diferents** (ex: Disc local SSD/NAS i Núvol).

**Còpia Fora de la Seu**

Guardar almenys **una còpia en una ubicació externa (Offsite)** per protegir-se de desastres locals (incendis, robatoris).

## Diapositiva 10

![Imatge 3](@@IMG@@/img-003.jpg){ loading=lazy }

![Imatge 4](@@IMG@@/img-004.png){ loading=lazy }

**Resum d'Estudi - Seguretat Física 2.0**

Garanteix la integritat amb funcions Hash modernes (SHA-2/SHA-3), controla l'accés amb ACLs i el principi de privilegi mínim, i assegura la continuïtat del negoci aplicant la **regla 3-2-1** de còpies de seguretat.
