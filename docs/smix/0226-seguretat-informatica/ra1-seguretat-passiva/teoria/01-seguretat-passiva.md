---
description: Introducció al mòdul, protecció física i ambiental, mesures de seguretat física, SAI i primers conceptes de seguretat lògica.
# Enllaç de Google Drive per descarregar el PDF complet (si el deixes buit, el botó no es mostra):
pdf: ""
---

# Seguretat passiva

## Introducció al mòdul

La **seguretat informàtica** engloba tots els processos i mecanismes destinats a preservar la informació en ordinadors i xarxes. El seu objectiu principal és protegir aquesta informació contra robatoris, corrupció i catàstrofes, assegurant al mateix temps que els usuaris autoritzats puguin continuar accedint-hi.

## La primera línia de defensa: seguretat passiva

### Què és la seguretat passiva?

La **seguretat passiva** estudia els aspectes més importants de la seguretat física per minimitzar riscos en els equips informàtics.

Decidir correctament les característiques de la seguretat física representa tenir una base sòlida sobre la qual construir els altres elements de seguretat.

!!! warning "Idea clau"
    Una fallada en la seguretat física pot comprometre directament la seguretat lògica i la integritat de la informació, per molt sofisticades que siguin les mesures de ciberseguretat implementades.

## Protecció física i ambiental dels equips

Les mesures més importants són:

- **Emplaçament:** la ubicació és clau. És molt recomanable triar llocs amb poca visibilitat per no cridar l'atenció de possibles atacants. Cal tenir en compte també possibles catàstrofes naturals (incendis, inundacions…).
- **Prevenció d'incendis:** és vital tenir detectors de fum i sistemes d'extinció. És molt important que els sistemes siguin adequats als dispositius que tenim, per evitar agreujar els problemes i els danys als equips.
- **Condicions ambientals:** és crucial controlar la temperatura, la humitat i la ventilació.

*Exemple de centre de procés de dades (CPD): el del Banco Sabadell a Madrid.*

## Categories de mesures de seguretat física

Les mesures de seguretat es poden dividir en diverses categories segons la finalitat que tenen:

**Mesures dissuasives**
:   Desplegar una sèrie d'elements visibles per a possibles atacants que els facin canviar d'opinió i es pensin dues vegades fer l'atac.
    *Exemples:* tanques, guardes de seguretat, il·luminació nocturna.

**Dificultats en l'accés a personal no autoritzat**
:   Per exemple cadenats i controls d'accés (biomètrics, amb targetes o teclat numèric), seguretat perimetral o *mantraps*.

**Detecció d'intrusos**
:   Sensors de detecció interns i externs, detecció de canvis en l'ambient (lumínics, acústics, de moviment…). Aquests sistemes de detecció han de tenir un subministrament elèctric aïllat de la resta per evitar sabotatges.

**Avaluació d'incidències**
:   És recomanable redactar una sèrie de procediments que cal seguir quan apareix una alarma, i també tenir una estructura de comunicació.
    *Sistemes d'avaluació d'incidències:* monitoratge dels sistemes d'alarmes, procediments per a casos d'emergència i estructura de comunicació.

## Garantint el subministrament elèctric: els SAI

Les alteracions del subministrament elèctric, com les **sobretensions** o les **baixades de tensió**, representen un risc greu per als components electrònics i poden causar danys irreparables.

Un **SAI** és un equip que protegeix i, en cas de tall de corrent, subministra energia el temps suficient per poder apagar els equips de manera ordenada i segura.

| Exemple de SAI | Cost aproximat |
|---|---|
| SAI de la marca APC (model petit) | entre 45 € i 90 € |
| SAI de la marca Eaton (model professional) | entre 550 € i 3.500 € |

:material-arrow-right: Els SAI es tracten amb detall a la pàgina [SAI](02-sai.md).

## Seguretat lògica

- **Autenticació:** verificació de la identitat d'un usuari o d'una altra entitat del sistema. Es pot basar en:
    - alguna cosa que una persona **sap** (contrasenya),
    - alguna cosa que una persona **té** (una clau, una targeta d'accés),
    - alguna cosa que una persona **és o fa** (biometria).
- **Autorització:** concessió d'un dret o d'un permís a una entitat per accedir a un recurs.

:material-arrow-right: Aquest tema es desenvolupa a la pàgina [Seguretat lògica](03-seguretat-logica.md).

### Contrasenyes

Perquè una contrasenya sigui difícil d'esbrinar ha de:

- contenir tant majúscules com minúscules, text, valors numèrics i alfanumèrics,
- tenir com a mínim **10 caràcters** de longitud,
- no aparèixer a cap diccionari,
- no basar-se en informació personal.

Exemple de contrasenya forta: `K#zu4^40\l2`

Les contrasenyes sempre han de ser **úniques per a cada servei** que ens donem d'alta: fer servir la mateixa contrasenya per a tot no és correcte. Per facilitar-ne la gestió tenim els **gestors de contrasenyes**:

| Tipus | Com funciona | Exemples |
|---|---|---|
| Basats en el cloud | Les dades es guarden xifrades en servidors. | LastPass, Passit, 1Password… |
| Locals | Les dades es guarden xifrades a l'ordinador. | KeePass |
| Integrats al navegador | Molt còmodes, però poden ser menys segurs que les aplicacions dedicades. | Gestor de contrasenyes de Google |
