# Seguretat Activa i Verificació de Software

## Diapositiva 1

![Imatge 1](@@IMG@@/img-001.jpg){ loading=lazy }

![Imatge 2](@@IMG@@/img-002.png){ loading=lazy }

**Seguretat Activa i Verificació de Software**

**MÒDUL DE SEGURETAT INFORMÀTICA**

Material d'estudi: Protecció Directa, Antivirus, Plans de Contingència i Cadena de Custòdia de Software (SBOM i SLSA)

## Diapositiva 2

**DEFINICIÓ I ROL**

**Concepte de Seguretat Activa**

La **seguretat activa** és la barrera "viva" que es manté sempre alerta en el funcionament diari del sistema per aturar atacs, minimitzar danys i recuperar l'activitat el més ràpidament possible.

**Protecció Directa**

**Manteniment Proactiu**

**Identificació i Còpies**

Antivirus i sistemes que controlen el trànsit de dades a la xarxa en temps real.

Actualitzacions constants del programari i configuració segura dels sistemes operatius.

Certificats digitals, autenticació d'usuaris i còpies de seguretat de dades i configuració.

## Diapositiva 3

**PUNTS CRÍTICS**

**Àmbits d'Actuació de la Seguretat Activa**

**Sistemes i Aplicacions**

**Identificació i Control**

**Plans de Resposta**

Mantenir el maquinari i el programari vigilats, actualitzats i lliures de vulnerabilitats conegudes.

Controlar de manera estricta qui accedeix a la informació i amb quins permisos.

Tenir preparats protocols de contingència davant d'intrusions, virus o fallades greus.

## Diapositiva 4

**VULNERABILITATS I MAQUINARI**

**Amenaces de Seguretat i Sistemes Operatius**

• **Atacs de Hackers:** Des de la filtració d'informació fins a la supressió de dades o el control total de la màquina.

**Tipus d'Atacs i Malware**

Diferències entre **sistemes de pagament** i **programari lliure**:

**Sistemes Operatius**

Varien en el model de desenvolupament, arquitectura de permisos, incidència de malware i velocitat de publicació de parches de seguretat.

• **Programari Maliciós:** Alenteix el sistema, col·lapsa el servei de correu o impedeix el funcionament de l'equip.

• **Minimitzar Aplicacions:** Una bona mesura és instal·lar *només les aplicacions estrictament necessàries*.

## Diapositiva 5

**PROTECCIÓ ENDPOINT**

**Funcionament dels Antivirus**

**1. Diccionari de Signatures**

**2. Anàlisi Comportamental / Heurística**

Examina els fitxers per comparar-los amb una base de dades coneguda de virus i patrons maliciosos prèviament recopilats.

Identifica comportaments sospitosos en qualsevol programa: captura de dades no autoritzada, monitoratge de ports o modificacions del registre.

## Diapositiva 6

**CONTINUÏTAT DE NEGOCI**

**Plans de Contingència Empresarials**

Conjunt de **procediments alternatius** a l'operativitat normal de l'organització.

**Definició i Objectiu**

Dóna regles clares sobre com resoldre la incidència, assignar responsabilitats i restaurar els sistemes afectats en el menor temps possible.

**Instruccions d'Actuació**

Permet el funcionament continu de l'empresa quan alguna de les seves funcions o serveis deixa d'operar a causa d'un incident intern o extern.

## Diapositiva 7

**METODOLOGIA D'IMPLANTACIÓ**

**Les 5 Fases del Pla de Contingència**

**1. Avaluació:** Identificació de riscos, actius crítics i anàlisi d'impacte en el negoci (BIA).

**2. Planificació:** Disseny de procediments alternatius i protocols de resposta davant de crisis.

**3. Proves de Viabilitat:** Simulacres i assajos per comprovar l'eficàcia del pla abans que passi una emergència real.

**4. Execució:** Activació dels protocols de contingència durant un incident de seguretat.

**5. Recuperació:** Retorn a la normalitat operació i restauració completa dels serveis afectats.

## Diapositiva 8

**SEGURETAT DE SOFTWARE**

**Nivell 1: Matrícula i Integritat (Mètodes Clàssics)**

**Funcions Hash (SHA-256 / MD5)**

**Signatura Digital**

Actua com una **amprenta dactilar única** del fitxer. Qualsevol modificació (encara que sigui d'un sol bit) canvia el hash completament.

Segell de lacre del desenvolupador. Garanteix que l'aplicació prové d'una entitat coneguda i de confiança (ex: Apple, Microsoft, Google).

*Exemple:* Com comprovar el pes exacte d'una caixa tancada per veure si s'ha tret alguna cosa.

## Diapositiva 9

**CADENA DE SUBMINISTRAMENT**

**Nivell 2: Llista d'Ingredients (SBOM)**

**Què és l'SBOM?**

**Utilitat de Seguretat**

**Software Bill of Materials:** Funciona com l'etiqueta nutricional d'un aliment, detallant totes les llibreries externes utilitzades.

Si es descobreix una vulnerabilitat en una llibreria externa, l'SBOM permet saber immediatament quines aplicacions de l'organització estan afectades.

Avui dia cap desenvolupador escriu una app des de zero; s'utilitzen múltiples peces i llibreries de tercers.

## Diapositiva 10

**SEGURETAT AVANÇADA**

**Nivell 3: Cadena de Custòdia (SLSA)**

**Passaport Digital de Software**

**Mur de Verificació**

**SLSA (Supply-chain Levels for Software Artifacts):** Verifica tot el camí des del codi font de l'ordinador del programador fins a l'execució.

Abans d'instal·lar l'app, el sistema comprova les signatures de la cadena. Si falta cap segell o el codi ha estat alterat, **la instal·lació es bloqueja automàticament**.

• **Atestació (Attestation):** Document JSON amb metadades de cada pas.

• **Segellat Criptogràfic:** Cada fase se signa amb claus d'alta seguretat.

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

## Diapositiva 12

![Imatge 3](@@IMG@@/img-003.jpg){ loading=lazy }

![Imatge 4](@@IMG@@/img-004.png){ loading=lazy }

**Resum d'Estudi - Seguretat Activa**

La seguretat activa combina eines de prevenció en temps real (antivirus, actualitzacions), planificació de contingència organitzativa i mecanismes moderns de verificació de programari com **Hashes, SBOM i SLSA**.
