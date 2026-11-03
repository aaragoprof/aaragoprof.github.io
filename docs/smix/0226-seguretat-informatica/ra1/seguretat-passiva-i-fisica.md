# La primera línia de defensa: seguretat passiva

**Seguretat informàtica** · Protecció física, ambiental, control de riscos, SAI i gestió de contrasenyes

## Introducció al mòdul

*Objectius generals*

La **seguretat informàtica** engloba tots els processos i mecanismes destinats a preservar la informació en ordinadors i xarxes.

### Protecció integral

Protegir la informació contra robatoris, corrupció i catàstrofes.

### Accés autoritzat

Assegurar que els usuaris autoritzats puguin continuar accedint a la informació quan ho necessitin.

## Què és la seguretat passiva?

*Definició i fonaments*

### Base sòlida

La **seguretat passiva** estudia els aspectes més importants de la **seguretat física** per minimitzar riscos en els equips informàtics.

!!! warning "Impacte d'una fallada física"
    Decidir correctament la seguretat física és la base dels altres elements. Una fallada física pot **comprometre directament la seguretat lògica i la integritat de la informació**, per molt sofisticades que siguin les mesures de ciberseguretat implementades.

## Protecció física i ambiental dels equips

*Mesures clau*

### Emplaçament

Triar ubicacions amb poca visibilitat per no cridar l'atenció de possibles atacants. Tenir en compte el risc de catàstrofes naturals (incendis, inundacions...).

### Prevenció d'incendis

Vital tenir detectors de fum i sistemes d'extinció. Molt important utilitzar sistemes adequats als equips elèctrics per evitar agreujar els danys.

### Condicions ambientals

És crucial controlar constantment la temperatura, la humitat i la ventilació de les sales o CPDs.

!!! example "Exemple d'infraestructura crítica"
    CPD de Banco Sabadell a Madrid.

## Categories de mesures de seguretat física

*Classificació de recursos*

### Mesures dissuasives

Elements visibles per fer canviar d'opinió als atacants (ex: tanques, guardes de seguretat, il·luminació nocturna).

### Dificultats d'accés

Impedir el pas a personal no autoritzat (cadenats, biometria, targetes, teclats numèrics, seguretat perimetral o mantraps).

### Detecció d'intrusos

Sensors interns/externs (lumínics, acústics, de moviment). Cal que tinguin **subministrament elèctric aïllat** per evitar sabotatges.

### Avaluació d'incidències

Procediments clars quan salti una alarma, monitoratge de sistemes i una estructura de comunicació definida.

## Garantint el subministrament: els SAI

*Protecció elèctrica*

### Risc elèctric

Les alteracions del subministrament elèctric (sobretensions, baixades) representen un risc greu per als components electrònics, podent causar **danys irreparables**.

### Protecció SAI

Un SAI protegeix els equips i, en cas de tall, subministra energia el temps suficient per poder **apagar els equips de manera ordenada i segura**.

| Tipus de SAI | Cost |
|--------------|------|
| **SAI bàsic** (APC / monofàsic) | entre 45 € i 90 € |
| **SAI server/rack** (EATON / trifàsic) | entre 550 € i 3.500 € |

## Autenticació i autorització

*Control d'accés lògic*

### Autenticació

Verificació de la identitat d'un usuari o entitat basada en:

- **Alguna cosa que se sap:** contrasenya, PIN.
- **Alguna cosa que es té:** clau física, targeta d'accés, token.
- **Alguna cosa que s'és o es fa:** biometria (empremta, iris).

### Autorització

Concessió d'un dret o d'un permís específic a una entitat prèviament autenticada per poder accedir a un recurs del sistema.

## Requisits per a contrasenyes segures

*Bones pràctiques*

- **Complexitat:** majúscules, minúscules, números i símbols alfanumèrics.
- **Longitud:** com a mínim 10 caràcters de longitud.
- **Impredictible:** no ha d'aparèixer al diccionari ni basar-se en dades personals.
- **Única per servei:** mai utilitzar la mateixa contrasenya per a tot.

!!! example "Exemple de contrasenya robusta"
    `K#zu4^40\12`

    Combina símbols, majúscules, minúscules i números.

## Tipus de gestors de contrasenyes

*Eines de gestió*

### Basats en cloud

Dades guardades xifrades en servidors remots.

**Exemples:** LastPass, Passit, 1Password.

### Gestió local

Dades guardades xifrades localment a l'ordinador.

**Exemple clau:** KeePass.

### Integrats al navegador

Molt còmodes, però poden ser menys segurs que les apps dedicades.

**Exemple:** Gestor de Google.

## Resum de seguretat passiva

La seguretat física i les bones pràctiques en contrasenyes són el pilar fonamental per protegir qualsevol sistema informàtic.