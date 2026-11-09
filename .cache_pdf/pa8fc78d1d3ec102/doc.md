# Seguretat Activa i Verificació de Software

<p class="md-kicker">MÒDUL DE SEGURETAT INFORMÀTICA</p>

Material d'estudi: Protecció Directa, Antivirus, Plans de Contingència i Cadena de Custòdia de Software (SBOM i SLSA)

## Concepte de Seguretat Activa

<p class="md-kicker">DEFINICIÓ I ROL</p>

La **seguretat activa** és la barrera "viva" que es manté sempre alerta en el funcionament diari del sistema per aturar atacs, minimitzar danys i recuperar l'activitat el més ràpidament possible.

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### Protecció Directa

Antivirus i sistemes que controlen el trànsit de dades a la xarxa en temps real.

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### Manteniment Proactiu

Actualitzacions constants del programari i configuració segura dels sistemes operatius.

</div>

<div class="md-card" style="--card:#8B5CF6" markdown="1">

### Identificació i Còpies

Certificats digitals, autenticació d'usuaris i còpies de seguretat de dades i configuració.

</div>

</div>

## Àmbits d'Actuació de la Seguretat Activa

<p class="md-kicker">PUNTS CRÍTICS</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### Sistemes i Aplicacions

Mantenir el maquinari i el programari vigilats, actualitzats i lliures de vulnerabilitats conegudes.

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### Identificació i Control

Controlar de manera estricta qui accedeix a la informació i amb quins permisos.

</div>

<div class="md-card" style="--card:#8B5CF6" markdown="1">

### Plans de Resposta

Tenir preparats protocols de contingència davant d'intrusions, virus o fallades greus.

</div>

</div>

## Amenaces de Seguretat i Sistemes Operatius

<p class="md-kicker">VULNERABILITATS I MAQUINARI</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#EF4444" markdown="1">

### Tipus d'Atacs i Malware

- **Atacs de Hackers:** Des de la filtració d'informació fins a la supressió de dades o el control total de la màquina.
- **Programari Maliciós:** Alenteix el sistema, col·lapsa el servei de correu o impedeix el funcionament de l'equip.
- **Minimitzar Aplicacions:** Una bona mesura és instal·lar *només les aplicacions estrictament necessàries*.

</div>

<div class="md-card" style="--card:#0284C7" markdown="1">

### Sistemes Operatius

Diferències entre **sistemes de pagament** i **programari lliure**:

Varien en el model de desenvolupament, arquitectura de permisos, incidència de malware i velocitat de publicació de parches de seguretat.

</div>

</div>

## Funcionament dels Antivirus

<p class="md-kicker">PROTECCIÓ ENDPOINT</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### 1. Diccionari de Signatures

Examina els fitxers per comparar-los amb una base de dades coneguda de virus i patrons maliciosos prèviament recopilats.

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### 2. Anàlisi Comportamental / Heurística

Identifica comportaments sospitosos en qualsevol programa: captura de dades no autoritzada, monitoratge de ports o modificacions del registre.

</div>

</div>

## Plans de Contingència Empresarials

<p class="md-kicker">CONTINUÏTAT DE NEGOCI</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#16A34A" markdown="1">

### Definició i Objectiu

Conjunt de **procediments alternatius** a l'operativitat normal de l'organització.

Permet el funcionament continu de l'empresa quan alguna de les seves funcions o serveis deixa d'operar a causa d'un incident intern o extern.

</div>

<div class="md-card" style="--card:#0284C7" markdown="1">

### Instruccions d'Actuació

Dóna regles clares sobre com resoldre la incidència, assignar responsabilitats i restaurar els sistemes afectats en el menor temps possible.

</div>

</div>

## Les 5 Fases del Pla de Contingència

<p class="md-kicker">METODOLOGIA D'IMPLANTACIÓ</p>

<div class="md-callout" style="--card:#0284C7" markdown="1">

**1. Avaluació:** Identificació de riscos, actius crítics i anàlisi d'impacte en el negoci (BIA).

</div>

<div class="md-callout" style="--card:#06B6D4" markdown="1">

**2. Planificació:** Disseny de procediments alternatius i protocols de resposta davant de crisis.

</div>

<div class="md-callout" style="--card:#F59E0B" markdown="1">

**3. Proves de Viabilitat:** Simulacres i assajos per comprovar l'eficàcia del pla abans que passi una emergència real.

</div>

<div class="md-callout" style="--card:#EF4444" markdown="1">

**4. Execució:** Activació dels protocols de contingència durant un incident de seguretat.

</div>

<div class="md-callout" style="--card:#16A34A" markdown="1">

**5. Recuperació:** Retorn a la normalitat operació i restauració completa dels serveis afectats.

</div>

## Nivell 1: Matrícula i Integritat (Mètodes Clàssics)

<p class="md-kicker">SEGURETAT DE SOFTWARE</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### Funcions Hash (SHA-256 / MD5)

Actua com una **amprenta dactilar única** del fitxer. Qualsevol modificació (encara que sigui d'un sol bit) canvia el hash completament.

<div class="md-callout" markdown="1">

*Exemple:* Com comprovar el pes exacte d'una caixa tancada per veure si s'ha tret alguna cosa.

</div>

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### Signatura Digital

Segell de lacre del desenvolupador. Garanteix que l'aplicació prové d'una entitat coneguda i de confiança (ex: Apple, Microsoft, Google).

</div>

</div>

## Nivell 2: Llista d'Ingredients (SBOM)

<p class="md-kicker">CADENA DE SUBMINISTRAMENT</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#F59E0B" markdown="1">

### Què és l'SBOM?

**Software Bill of Materials:** Funciona com l'etiqueta nutricional d'un aliment, detallant totes les llibreries externes utilitzades.

Avui dia cap desenvolupador escriu una app des de zero; s'utilitzen múltiples peces i llibreries de tercers.

</div>

<div class="md-card" style="--card:#EF4444" markdown="1">

### Utilitat de Seguretat

Si es descobreix una vulnerabilitat en una llibreria externa, l'SBOM permet saber immediatament quines aplicacions de l'organització estan afectades.

</div>

</div>

## Nivell 3: Cadena de Custòdia (SLSA)

<p class="md-kicker">SEGURETAT AVANÇADA</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#8B5CF6" markdown="1">

### Passaport Digital de Software

**SLSA (Supply-chain Levels for Software Artifacts):** Verifica tot el camí des del codi font de l'ordinador del programador fins a l'execució.

- **Atestació (Attestation):** Document JSON amb metadades de cada pas.
- **Segellat Criptogràfic:** Cada fase se signa amb claus d'alta seguretat.

</div>

<div class="md-card" style="--card:#EF4444" markdown="1">

### Mur de Verificació

Abans d'instal·lar l'app, el sistema comprova les signatures de la cadena. Si falta cap segell o el codi ha estat alterat, **la instal·lació es bloqueja automàticament**.

</div>

</div>

## Diapositiva 11

**EXEMPLE D'INTEGRACIÓ**

**La Cadena SLSA a la Pràctica**

| Pas | Acció Reallitzada | Eina Típica |
|---|---|---|
| Codi | El programador puja el codi font al repositori. | GitHub / GitLab |
| Build | Una màquina aïllada compila el codi en executable. | GitHub Actions / Tekton |
| Signatura | Es genera el segell de seguretat criptogràfic. | Sigstore (Cosign) |
| Provinència | Es crea el document JSON d'atestació de la cadena. | SLSA Generator |
| Verificació | L'empresa client comprova el segell abans d'executar-lo. | Policy Controller |

## Resum d'Estudi - Seguretat Activa

La seguretat activa combina eines de prevenció en temps real (antivirus, actualitzacions), planificació de contingència organitzativa i mecanismes moderns de verificació de programari com **Hashes, SBOM i SLSA**.
