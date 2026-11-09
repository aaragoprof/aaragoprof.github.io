# Recuperació de Dades i Identitat Digital

## Diapositiva 1

![Imatge 1](@@IMG@@/img-001.jpg){ loading=lazy }

![Imatge 2](@@IMG@@/img-002.png){ loading=lazy }

**Recuperació de Dades i Identitat Digital**

**MÒDUL DE SEGURETAT INFORMÀTICA (PART 2)**

Material d'estudi: Tècniques de Recuperació sense Backup, Xifrat Simètric/Asimètric, Certificats Digitals i Signatura Electrònica (eIDAS)

## Diapositiva 2

**RESILIÈNCIA D'INFORMACIÓ**

**Tècniques de Recuperació de Dades**

La pèrdua de dades pot aturar l'activitat d'una organització. Per evitar-ho, cal aplicar una combinació de polítiques preventives de còpies de seguretat i tècniques d'extracció directa.

**Política Preventiva (Backup)**

**Restabliment Immediat**

L'opció més ràpida i efectiva. Les còpies s'han de guardar en **2 o 3 ubicacions diferents** per minimitzar la pèrdua d'informació recent.

Permet restaurar el sistema en pocs minuts, perdent únicament les dades modificades posteriorment a la darrera còpia programada.

## Diapositiva 3

**FORENSICA DE BAIX NIVELL**

**Recuperació de Fitxers Eliminats sense Backup**

**El Marcador del Clúster**

**Regla d'Or de la Recuperació**

Quan s'esborra un arxiu, el sistema operatiu **no n'elimina les dades immediatament** del disc físic.

**Molt Important:** Per poder utilitzar eines de recuperació de dades:

• Simplement marca el **clúster** com a disponible per ser sobreescrit.

**No s'ha de realitzar CAP operació d'escriptura al disc per evitar que els clústers originals es sobreescriguin.**

• La informació continua intacta fins que un nou fitxer s'escriu a sobre.

## Diapositiva 4

**AUTENTICACIÓ A LA XARXA**

**Certificat Digital i Passaport Electrònic**

**Concepte de Certificat Digital**

**Autoritat Certificadora (CA)**

Document electrònic que actua com a **passaport digital** per garantir la identitat d'una persona o entitat a Internet.

Tercer de confiança oficial (com CATCert o la FNMT) que verifica la identitat del sol·licitant i expedeix el certificat oficial.

Permet establir connexions segures, transaccions comercials i gestions administratives de manera remota.

## Diapositiva 5

**FONAMENT CRIPTOGRÀFIC**

**Model de Claus: Simètric vs. Asimètric**

**Clau Secreta (Simètrica)**

**Clau Pública (Asimètrica)**

Emissor i receptor utilitzen la **mateixa clau privada** per xifrar i desxifrar.

Cada usuari disposa d'un par de claus matemàticament enllaçades:

\* Poc pràctic per a comunicacions massives a Internet.

• **Clau Pública:** La coneix tothom; serveix per xifrar el missatge.

• **Clau Privada:** Només la té el propietari; serveix per desxifrar el missatge rebut.

## Diapositiva 6

**CLASSIFICACIÓ DE CERTIFICATS**

**Variants de Certificats Digitals segons Funció**

**Certificats SSL / TLS**

**Certificats de Correu**

**Segell de Data i Hora**

S'instal·len en servidors web per establir connexions xifrades (HTTPS) i verificar el domini.

S'utilitzen per signar i xifrar missatges de correu electrònic personal o corporatiu.

Certifiquen de manera inalterable l'instant exacte en què s'ha realitzat una transacció o signatura.

## Diapositiva 7

**GARANTIES DE SEGURETAT**

**La Signatura Electrònica i les Seves 3 Garanties**

**Autenticitat**

**Integritat**

**No Repudi (No Denegació)**

Confirma de manera inequívoca que l'autor del document és exactament qui diu ser.

Garanteix que el missatge no ha estat alterat (si es toca una sola coma, la signatura es trenca).

L'autor no pot negar haver après o enviat el document, ja que només ell té la seva clau privada.

## Diapositiva 8

**SEGURETAT EN LA TRANSMISSIÓ**

**El Concepte de "Sobre Electrònic"**

**Passos del Procés**

**Resultat Inviolable**

• **1. Signar:** L'emissor encripta el missatge amb la seva clau privada (demostra la seva identitat).

El missatge queda completament protegit contra la lectura per part de tercers i qualsevol modificació destrueix automàticament la validesa del certificat.

• **2. Protegir:** S'utilitza la **clau pública del receptor** per tancar el "sobre".

• **3. Obertura:** Només el receptor pot obrir el sobre amb la seva pròpia clau privada.

## Diapositiva 9

**MARCO LEGAL (LLEI 59/2003 I EIDAS)**

**Nivells de Signatura segons la Legislació**

| Nivell de Signatura | Requisits Tecnològics | Nivell de Seguretat | Validesa Jurídica |
|---|---|---|---|
| Signatura Simple | Dades en format electrònic associades (ex: codi PIN o checkbox) | Baix | Provativa bàsica en judici |
| Signatura Avançada | Identifica el signant i garanteix la integritat del document | Mitjà | Alt valor provatori |
| Signatura Qualificada | Feta amb dispositiu segur (DNIe) i verificació presencial de la identitat | Alt | Equivalent a la firma manuscrita |

## Diapositiva 10

**PROCEDIMENT D'EXPEDICIÓ**

**Obtenció de Certificats i Tràmit Presencial**

**Tràmit de Presencialitat**

**Instal·lació i Compatibilitat**

Perquè un certificat tingui la màxima validesa legal (Qualificada), cal acreditació presencial.

El software s'instal·la al navegador o gestor de correu. Actualment és 100% compatible amb sistemes Windows, Linux i dispositius mòbils.

• Cal anar físicament a una oficina d'acreditació (Agència Tributària, ajuntament).

• **Entitats d'expedició:** AOC (CATCert a Catalunya) o FNMT.

## Diapositiva 11

**APLICACIÓ PRÀCTICA**

**La Finestreta Virtual i Plataformes de Verificació**

**Tràmits Telemàtics**

**Verificació en Línia (VALId / VALIDE)**

Substitueix la presència física per a tràmits oficials:

Plataformes públiques que permeten pujar un document signat per comprovar si la signatura és vàlida, la clau no està caducada i el text no ha estat alterat.

• Declaració de la Renda (Hisenda).

• Canvis de padró i certificats de vida laboral.

## Diapositiva 12

![Imatge 3](@@IMG@@/img-003.jpg){ loading=lazy }

![Imatge 4](@@IMG@@/img-004.png){ loading=lazy }

**Resum d'Estudi - Seguretat Activa 2**

La recuperació de dades combina la prevenció per backups amb la forensica de clústers. Per a la seguretat en línia, la **criptografia asimètrica**, els **certificats digitals** i la **signatura qualificada** garanteixen autenticitat, integritat i no repudi en tots els tràmits telemàtics.
