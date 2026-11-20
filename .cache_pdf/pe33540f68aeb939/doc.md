# Recuperació de Dades i Identitat Digital

<p class="md-kicker">MÒDUL DE SEGURETAT INFORMÀTICA (PART 2)</p>

Material d'estudi: Tècniques de Recuperació sense Backup, Xifrat Simètric/Asimètric, Certificats Digitals i Signatura Electrònica (eIDAS)

## Tècniques de Recuperació de Dades

<p class="md-kicker">RESILIÈNCIA D'INFORMACIÓ</p>

La pèrdua de dades pot aturar l'activitat d'una organització. Per evitar-ho, cal aplicar una combinació de polítiques preventives de còpies de seguretat i tècniques d'extracció directa.

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#16A34A" markdown="1">

### Política Preventiva (Backup)

L'opció més ràpida i efectiva. Les còpies s'han de guardar en **2 o 3 ubicacions diferents** per minimitzar la pèrdua d'informació recent.

</div>

<div class="md-card" style="--card:#0284C7" markdown="1">

### Restabliment Immediat

Permet restaurar el sistema en pocs minuts, perdent únicament les dades modificades posteriorment a la darrera còpia programada.

</div>

</div>

## Recuperació de Fitxers Eliminats sense Backup

<p class="md-kicker">FORENSICA DE BAIX NIVELL</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### El Marcador del Clúster

Quan s'esborra un arxiu, el sistema operatiu **no n'elimina les dades immediatament** del disc físic.

- Simplement marca el **clúster** com a disponible per ser sobreescrit.
- La informació continua intacta fins que un nou fitxer s'escriu a sobre.

</div>

<div class="md-card" style="--card:#EF4444" markdown="1">

### Regla d'Or de la Recuperació

**Molt Important:** Per poder utilitzar eines de recuperació de dades:

<div class="md-callout" style="--card:#EF4444" markdown="1">

**No s'ha de realitzar CAP operació d'escriptura al disc per evitar que els clústers originals es sobreescriguin.**

</div>

</div>

</div>

## Certificat Digital i Passaport Electrònic

<p class="md-kicker">AUTENTICACIÓ A LA XARXA</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### Concepte de Certificat Digital

Document electrònic que actua com a **passaport digital** per garantir la identitat d'una persona o entitat a Internet.

Permet establir connexions segures, transaccions comercials i gestions administratives de manera remota.

</div>

<div class="md-card" style="--card:#8B5CF6" markdown="1">

### Autoritat Certificadora (CA)

Tercer de confiança oficial (com CATCert o la FNMT) que verifica la identitat del sol·licitant i expedeix el certificat oficial.

</div>

</div>

## Model de Claus: Simètric vs. Asimètric

<p class="md-kicker">FONAMENT CRIPTOGRÀFIC</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#F59E0B" markdown="1">

### Clau Secreta (Simètrica)

Emissor i receptor utilitzen la **mateixa clau privada** per xifrar i desxifrar.

\* Poc pràctic per a comunicacions massives a Internet.

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### Clau Pública (Asimètrica)

Cada usuari disposa d'un par de claus matemàticament enllaçades:

- **Clau Pública:** La coneix tothom; serveix per xifrar el missatge.
- **Clau Privada:** Només la té el propietari; serveix per desxifrar el missatge rebut.

</div>

</div>

## Variants de Certificats Digitals segons Funció

<p class="md-kicker">CLASSIFICACIÓ DE CERTIFICATS</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### Certificats SSL / TLS

S'instal·len en servidors web per establir connexions xifrades (HTTPS) i verificar el domini.

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### Certificats de Correu

S'utilitzen per signar i xifrar missatges de correu electrònic personal o corporatiu.

</div>

<div class="md-card" style="--card:#8B5CF6" markdown="1">

### Segell de Data i Hora

Certifiquen de manera inalterable l'instant exacte en què s'ha realitzat una transacció o signatura.

</div>

</div>

## La Signatura Electrònica i les Seves 3 Garanties

<p class="md-kicker">GARANTIES DE SEGURETAT</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### Autenticitat

Confirma de manera inequívoca que l'autor del document és exactament qui diu ser.

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### Integritat

Garanteix que el missatge no ha estat alterat (si es toca una sola coma, la signatura es trenca).

</div>

<div class="md-card" style="--card:#8B5CF6" markdown="1">

### No Repudi (No Denegació)

L'autor no pot negar haver après o enviat el document, ja que només ell té la seva clau privada.

</div>

</div>

## El Concepte de "Sobre Electrònic"

<p class="md-kicker">SEGURETAT EN LA TRANSMISSIÓ</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### Passos del Procés

- **1. Signar:** L'emissor encripta el missatge amb la seva clau privada (demostra la seva identitat).
- **2. Protegir:** S'utilitza la **clau pública del receptor** per tancar el "sobre".
- **3. Obertura:** Només el receptor pot obrir el sobre amb la seva pròpia clau privada.

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### Resultat Inviolable

El missatge queda completament protegit contra la lectura per part de tercers i qualsevol modificació destrueix automàticament la validesa del certificat.

</div>

</div>

## Diapositiva 9

**MARCO LEGAL (LLEI 59/2003 I EIDAS)**

**Nivells de Signatura segons la Legislació**

| Nivell de Signatura | Requisits Tecnològics | Nivell de Seguretat | Validesa Jurídica |
|---|---|---|---|
| Signatura Simple | Dades en format electrònic associades (ex: codi PIN o checkbox) | Baix | Provativa bàsica en judici |
| Signatura Avançada | Identifica el signant i garanteix la integritat del document | Mitjà | Alt valor provatori |
| Signatura Qualificada | Feta amb dispositiu segur (DNIe) i verificació presencial de la identitat | Alt | Equivalent a la firma manuscrita |

## Obtenció de Certificats i Tràmit Presencial

<p class="md-kicker">PROCEDIMENT D'EXPEDICIÓ</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### Tràmit de Presencialitat

Perquè un certificat tingui la màxima validesa legal (Qualificada), cal acreditació presencial.

- Cal anar físicament a una oficina d'acreditació (Agència Tributària, ajuntament).
- **Entitats d'expedició:** AOC (CATCert a Catalunya) o FNMT.

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### Instal·lació i Compatibilitat

El software s'instal·la al navegador o gestor de correu. Actualment és 100% compatible amb sistemes Windows, Linux i dispositius mòbils.

</div>

</div>

## La Finestreta Virtual i Plataformes de Verificació

<p class="md-kicker">APLICACIÓ PRÀCTICA</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### Tràmits Telemàtics

Substitueix la presència física per a tràmits oficials:

- Declaració de la Renda (Hisenda).
- Canvis de padró i certificats de vida laboral.

</div>

<div class="md-card" style="--card:#8B5CF6" markdown="1">

### Verificació en Línia (VALId / VALIDE)

Plataformes públiques que permeten pujar un document signat per comprovar si la signatura és vàlida, la clau no està caducada i el text no ha estat alterat.

</div>

</div>

## Resum d'Estudi - Seguretat Activa 2

La recuperació de dades combina la prevenció per backups amb la forensica de clústers. Per a la seguretat en línia, la **criptografia asimètrica**, els **certificats digitals** i la **signatura qualificada** garanteixen autenticitat, integritat i no repudi en tots els tràmits telemàtics.
