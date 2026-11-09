# Malware Avançat, SIEM i Zero Trust

## Diapositiva 1

![Imatge 1](@@IMG@@/img-001.jpg){ loading=lazy }

![Imatge 2](@@IMG@@/img-002.png){ loading=lazy }

**Protecció Avançada contra Malware**

**MÒDUL DE SEGURETAT INFORMÀTICA (PART 4)**

Material d'estudi: Virus Polimòrfics, SIEM, Intel·ligència Artificial Defensiva, Model Zero Trust i Evolució del Ransomware

## Diapositiva 2

**AMENACES MODERNES**

**Panorama Actual del Programari Maliciós (Malware)**

El malware modern no cerca només la destrucció, sinó principalment el **benefici econòmic**, la dades personals o el control del sistema mitjançant tècniques molt sofisticades.

**Ransomware**

**Spyware i Adware**

**Phishing i Enginyeria Social**

**Troians i Cucs**

Segresta i xifra les dades del sistema exigint un rescat econòmic per desxifrar-les.

Espien l'activitat de l'usuari, roben credencials o inunden el sistema amb publicitat.

Els troians s'amaguen dins d'apps legítimes; els cucs es propaguen sols per la xarxa.

Tècnica d'engany per robar dades confidencials suplantant entitats de confiança.

## Diapositiva 3

**MUTACIÓ DE CODI**

**Què és un Virus Polimòrfic?**

Programari maliciós que **canvia el seu propi codi (la seva forma)** cada vegada que s'estén, però mantenint la seva funció maliciosa original.

**Concepte de Polimorfisme**

• **Motor de Mutació:** Genera noves claus de xifrat i canvia l'ordre de les instruccions.

**Mecanisme de Mutació**

**Com que la seva empremta digital (hash) canvia constantment, el diccionari de signatures de l'antivirus no el pot reconèixer.**

• **Capa Externa Variable:** Es xifra amb una clau diferent en cada nova infecció.

• **Execució a RAM:** Es desxifra en memòria RAM per actuar, però en disc sembla un fitxer nou.

## Diapositiva 4

**DETECCIÓ AVANÇADA**

**Com es Detecten els Virus Polimòrfics?**

En lloc de mirar com *"és"* el virus, l'antivirus analitza què *"fa"*.

**Anàlisi de Comportament (Heurística)**

Execució del fitxer en un entorn virtual aïllat i segur.

**Emulació (Sandboxing)**

Si un programa intenta capturar dades, monitorar ports o xifrar fitxers sense permís, es bloqueja immediatament.

S'observa si el programa es desxifra i mostra el seu comportament maliciós abans de permetre l'execució al sistema real.

## Diapositiva 5

**ARQUITECTURA DEFENSIVA**

**Estratègies Globals de Defensa Informàtica**

**Antivirus Moderns (EDR / XDR)**

**Tallafoc (Firewall)**

**Higiene Digital i Backups**

Combinació de signatures conegudes amb motor d'anàlisi heurística i resposta automatitzada.

Filtra i controla el trànsit de xarxa en funció de regles de comunicació establertes.

Actualitzacions constants del SO, aplicació del principi de mínims privilegis i backups periòdics.

## Diapositiva 6

**CORRELACIÓ D'ESDEVENIMENTS**

**SIEM: La Pantalla de Control Centralitzada**

**Concepte del SIEM**

**Valor Afegit: Correlació**

Plataforma centralitzada que **recull i analitza els registres (logs)** de totes les eines de seguretat de l'empresa (Antivirus, Firewall, IDS, servidors).

Permet detectar atacs complexos coordinats que passarien completament desapercebuts si les eines s'analitzessin de forma aïllada.

## Diapositiva 7

**NOVES TECNOLOGIES**

**Intel·ligència Artificial: Ofensiva vs. Defensiva**

**IA Ofensiva (Atacants)**

**IA Defensiva (Protecció)**

• **Malware Generat per IA:** Mutacions de codi ultra-ràpides en qüestió de segons.

• **Models Predictius:** Antivirus que prediuen la conducta de l'atac abans que s'hagi produït.

• **Deepfakes i Phishing 2.0:** Clonació de veu i vídeo per enganyar empleats en procediments financers.

• **Resposta Automàtica:** Aïllament instantani d'equips afectats sense intervenció humana.

## Diapositiva 8

**PARADIGMA ACTUAL**

**Model Zero Trust: "Mai Confiïs, Verifica Sempre"**

**Principis del Model**

**Importància en Credencials Robades**

Ja no n'hi ha prou amb estar "dins" de la xarxa corporativa o darrere d'un firewall.

Si un atacant aconsegueix una contrasenya, Zero Trust atura la danyosa expansió lateral perquè el comportament o el dispositiu no coincideixen amb el patró habitual.

• Cada usuari, dispositiu i petició s'ha d'**autenticar i autoritzar constantment**.

• **Privilegi Mínim:** Accés restringit només al que és estrictament necessari per a la tasca.

## Diapositiva 9

**AMENACES DE RANSOMWARE**

**Evolució del Ransomware: Extorsió Múltiple**

**Doble / Triple Extorsió**

**Ransomware-as-a-Service (RaaS)**

Els cibercriminals no només xifren les dades, sinó que:

Model de negoci on es lloguen "kits" de malware ja preparats. Permet cometre ciberdelictes complexos sense necessitat de tenir coneixements de programació.

• Amenacen amb publicar informació privada o confidencial.

• Contacten directament amb els clients de l'empresa per augmentar la pressió.

## Diapositiva 10

**COMPARATIVA TECNOLÒGICA**

**Evolució de les Eines de Seguretat Activa**

| Eina / Model | Mètode Principal | Focus de Protecció | Nivell d'Eficàcia Actual |
|---|---|---|---|
| Antivirus Clàssic | Signatures / Diccionari de virus | Fitxers locals en disc | Baix (Incapaç davant virus polimòrfics) |
| EDR / XDR | Anàlisi heurístic i comportamental | Endpoints i processos actius | Alt (Detecta accions sospitoses) |
| SIEM | Correlació centralitzada de logs | Tota la infraestructura de xarxa | Molt Alt (Detecta atacs complexos) |
| Zero Trust | Verificació continua i privilegis mínims | Identitats, accessos i dades | Màxim (Mitiga el robatori de credencials) |

## Diapositiva 11

**SÍNTESI TECNOLÒGICA**

**Cadena Integria de Protecció Activa**

**Endpoint**

**Xarxa i Logs**

**Accés i Dades**

EDR amb emulació en **Sandbox** i anàlisi heurístic contra virus polimòrfics.

Supervisió centralitzada amb **SIEM** i protecció per **Firewall**.

Arquitectura **Zero Trust** i backups immutables automatitzats contra Ransomware.

## Diapositiva 12

![Imatge 3](@@IMG@@/img-003.jpg){ loading=lazy }

![Imatge 4](@@IMG@@/img-004.png){ loading=lazy }

**Resum d'Estudi - Seguretat Activa 4**

Davant de malware mutant i atacs basats en IA, la seguretat activa moderna exigeix combinar la monitoratge d'heurística i **Sandboxing**, la visió global d'un **SIEM**, la verificació contínua de **Zero Trust** i la resiliència del **Backup**.
