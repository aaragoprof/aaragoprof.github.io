---
description: Conceptes de seguretat activa, eines principals, plans de contingència i verificació d'aplicacions (Hash, Signatura, SBOM, SLSA).
pdf: ""
---

# Introducció a la seguretat activa i verificació de programari

## Què és la seguretat activa?

La **seguretat activa** és el conjunt de mesures i eines que tenen com a objectiu prevenir danys, disminuir els efectes dels atacs i, en cas que es produeixi un error, recuperar el sistema el més ràpidament possible. Comprèn les parts de la seguretat que es mantenen sempre alerta en el funcionament del dia a dia.

### Eines i recursos principals

- **Protecció directa:** Antivirus i programes que controlen el trànsit de dades a la xarxa.
- **Manteniment:** Actualitzacions constants del programari i configuració segura dels sistemes operatius.
- **Prevenció de pèrdues:** Realització de còpies de seguretat (tant de dades com de configuració).
- **Autenticació:** Ús de certificats digitals i sistemes d'identificació.

## Plans de contingència

Un **pla de contingència** és el conjunt de procediments alternatius a l'operativitat normal d'una organització. La seva finalitat és permetre el funcionament continu quan alguna de les funcions deixa d'operar a causa d'un incident.

Fases d'elaboració d'un pla de contingència:

1. **Avaluació**
2. **Planificació**
3. **Proves de viabilitat**
4. **Execució**
5. **Recuperació**

!!! warning "Instal·lació de programari"
    Una bona mesura de seguretat consisteix a instal·lar només les aplicacions strictly necessàries per al treball diari.

## Verificació de l'origen i l'autenticitat d'aplicacions

Per assegurar que una aplicació és legítima i no ha estat modificada, s'utilitzen tres nivells de verificació:

### Nivell 1: Matrícula i integritat (Mètodes Clàssics)
- **Funcions Hash (MD5, SHA-256):** Actuen com una empremta dactilar digital. Si es modifica un sol caràcter del codi, el hash canvia completament.
- **Signatura Digital:** Segell de lacre del desenvolupador que garanteix la procedència de l'aplicació.

### Nivell 2: Llista d'ingredients (SBOM)
- **SBOM (Software Bill of Materials):** Etiqueta nutricional del programari que detalla totes les llibreries i components de tercers utilitzats. Si una llibreria externa té una vulnerabilitat, l'SBOM permet identificar quines aplicacions estan afectades.

### Nivell 3: Cadena de custòdia (SLSA)
- **SLSA (*Supply-chain Levels for Software Artifacts*):** Estableix la traçabilitat de tot el procés des del codi font fins a la instal·lació. Genera proves signades (*attestations*) en cada pas (compilació, proves, empaquetat).

| Pas | Acció | Eina típica |
|---|---|---|
| **Codi** | El programador puja el codi. | GitHub / GitLab |
| **Build** | Una màquina aïllada compila el codi. | GitHub Actions / Tekton |
| **Signatura** | Es genera el segell de seguretat. | Sigstore (Cosign) |
| **Provinença** | Es crea el document JSON (atestació). | SLSA Generator |
| **Verificació** | Es comprova el segell abans d'executar l'app. | Policy Controller |