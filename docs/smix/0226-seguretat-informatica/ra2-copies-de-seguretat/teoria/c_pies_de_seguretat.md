---
description: Principis, objectius, models de còpies de seguretat (incremental vs diferencial) i limitacions en la gestió del procés.
pdf: ""
---

# Gestió del procés de creació de còpies de seguretat

## Introducció i principis

La creació d'una còpia de seguretat és un procés continu que s'ha d'actualitzar a mesura que les dades originals es modifiquen. La pèrdua o l'error de dades podria tenir conseqüències catastròfiques.

Els dos principis fonamentals de seguretat són:
* **Principi de disponibilitat:** Les dades han d'estar disponibles i al nostre abast.
* **Principi de confidencialitat:** Les dades només han de ser accessibles per les persones autoritzades.

## Objectius de les còpies de seguretat

- **Recuperació d'un determinat punt temporal:** Permet recuperar les dades en el moment exacte en què es va crear la còpia.
- **Seguretat de les dades:** Mantenir els permisos d'accés assignats als fitxers originals per evitar accessos no autoritzats.

## Models de còpies de seguretat

**Còpia Completa**
:   Còpia total de tots els fitxers seleccionats.

**Còpia Incremental**
:   Primer es desa una còpia completa i, a les següents, només s'afegeixen els canvis realitzats des de l'última còpia incremental.

**Còpia Diferencial**
:   Primer es desa una còpia completa i, a les següents, s'afegeixen tots els canvis acumulats des de l'última còpia completa.

### Comparativa: Incremental vs Diferencial

Suposant un conjunt de dades base de $100\text{ GB}$ el diumenge i un augment de $10\text{ GB}$ diaris:

| Dia | Còpia Incremental | Còpia Diferencial |
|---|---|---|
| **Diumenge** | Completa ($100\text{ GB}$) | Completa ($100\text{ GB}$) |
| **Dilluns** | Incremental: canvis dilluns ($10\text{ GB}$) | Diferencial: canvis dilluns ($10\text{ GB}$) |
| **Dimarts** | Incremental: canvis dimarts ($10\text{ GB}$) | Diferencial: canvis dilluns + dimarts ($20\text{ GB}$) |
| **Dimecres** | Incremental: canvis dimecres ($10\text{ GB}$) | Diferencial: canvis dilluns + dimarts + dimecres ($30\text{ GB}$) |
| **Restauració Dimecres** | Requereix: Completa + Dilluns + Dimarts + Dimecres (4 fitxers) | Requereix: Completa + Dimecres (2 fitxers) |
| **Pros / Contres** | Ràpida i poc espai, però restauració lenta/fràgil. | Restauració ràpida/segura, però la còpia diària creix en espai i temps. |

## Imatges del sistema i punts de restauració

* **Imatge del sistema:** Còpia exacta de tot el sistema informàtic (aplicacions, serveis i configuracions) que permet reinstal·lacions més ràpides i còmodes.
* **Punt de restauració:** Permet tornar a un estat anterior del sistema sense reinstal·lar-ho tot. Desa arxius del sistema, registre, aplicacions i controladors.

## Limitacions i riscos

1. **Finestra de còpies de seguretat:** Períodes de temps planificats en què es fa la còpia per no afectar els usuaris.
2. **Impacte en el rendiment:** El disc dur estarà ocupat realitzant operacions de lectura intensives.
3. **Cost econòmic:** Consideració de la capacitat d'emmagatzematge requerida i el cost de llicències de programari.
4. **Amplada de banda de la xarxa:** En sistemes distribuïts, la transferència pot saturar la xarxa.

## Mesura, monitoratge i validació

!!! warning "Checksum vs Hash"
    * **Checksum (suma de verificació):** Dissenyat per protegir contra canvis o errors **accidentals**.
    * **Hash criptogràfic:** Dissenyat per protegir contra modificacions **malicioses**.

* **Validació:** Proves i proves de comprobació de la integritat de les dades.
* **Creació d'informes:** Historials generats automàticament i registres d'activitat.

## Bones pràctiques

* Un sistema de còpies només és útil si tenim una **estratègia de restauració** planificada prèviament.
* **No desar les còpies físicament a prop** del sistema original.
* **Automatitzar** la creació per evitar errors humans.
* Utilitzar **formats estàndard o oberts**.
* Establir un monitoratge constant, ja que les còpies de vegades fallen.