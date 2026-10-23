---
description: Tècniques de recuperació de dades, xifratge simètric/asimètric, certificats digitals i signatura electrònica.
pdf: ""
---

# Recuperació de dades, certificats digitals i signatura electrònica

## Recuperació de dades

### Còpies de seguretat
La millor opció preventiva és disposar de còpies de seguretat programades i emmagatzemades en almenys dos o tres llocs diferents.

### Recuperació sense còpies
Quan s'elimina un arxiu, el sistema operatiu no esborra immediatament les dades; només marca el clúster com a disponible per a ser sobreescrit.

!!! danger "Atenció durant la recuperació"
    És fonamental **no realitzar cap operació d'escriptura** a la unitat afectada mentre s'intenta recuperar un fitxer, ja que si es sobreescriu el clúster la informació es perdrà definitivament.

## Xifratge i xarxes de confiança

El xifratge transforma un missatge intel·ligible en un codi secret per garantir tres pilars: **confidencialitat**, **integritat** i **autenticitat**.

- **Clau Secreta (Simètrica):** L'emissor i el receptor utilitzen la mateixa clau. Poc pràctica per a ús massiu a Internet.
- **Clau Pública (Asimètrica):** Cada usuari disposa d'un parell de claus:
    - **Clau Pública:** Accessible per a tothom; s'utilitza per xifrar missatges destinats a l'usuari.
    - **Clau Privada:** Secret personal; s'utilitza per desxifrar els missatges rebuts.

## Certificat digital

Document electrònic expedit per una **Autoritat Certificadora (CA)** que garanteix la identitat d'una persona o entitat a la xarxa.

### Tipus de certificats comuns
- **SSL / TLS:** Per a servidors web segurs.
- **De correu electrònic:** Per signar i xifrar missatges.
- **De segell, data i hora:** Per certificar el moment d'una transacció.

## Signatura electrònica

Component del certificat digital que garanteix:

1. **Autenticitat:** Confirma la identitat de l'autor.
2. **Integritat:** Garanteix que el document no ha estat modificat.
3. **No denegació (No repudi):** L'autor no pot negar l'autoria del document.

### Tipus de signatura segons la normativa

| Nivell | Nivell de seguretat | Característiques |
|---|---|---|
| **Simple** | Baix | Només identifica el firmant (ex. codi PIN). |
| **Avançada** | Mitjà | Identifica el firmant i garanteix la integritat del document. |
| **Reconeguda / Qualificada** | Alt | Utilitza un dispositiu segur (DNIe) i verificació presencial. Equivalent a la signatura manuscrita. |