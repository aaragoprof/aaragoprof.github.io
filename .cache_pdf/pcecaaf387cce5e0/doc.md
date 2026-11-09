# BYOD i MDM

## Diapositiva 1

![Imatge 1](@@IMG@@/img-001.jpg){ loading=lazy }

![Imatge 2](@@IMG@@/img-002.png){ loading=lazy }

**Monitoratge de Xarxes 2: BYOD i MDM**

**MÒDUL DE SEGURETAT I MONITORATGE**

Material d'estudi: Gestió de Dispositius Personals en Entorns Corporatius, Vectors d'Intrusió i Solucions de Control MDM

## Diapositiva 2

**NOU ENTORN DE TREBALL**

**BYOD (Bring Your Own Device): Concepte i Evolució**

Tradicionalment, les empreses adquirien i configuraven cada equips. Amb el model **BYOD**, els empleats utilitzen els seus propis dispositius personals (portàtils, smartphones, tauletes) per fer feina.

**Canvi de Paradigmàtica**

**Connexió a Recursos Interns**

**Barreja de Dades**

Transició d'equips 100% corporatius homogenis a una xarxa heterogènia plena de dispositius personals de diferents fabricants i sistemes operatius.

El dispositiu privat s'ha de connectar directament als serveis crítics de l'empresa: correu, servidors de fitxers i aplicacions internes.

En un mateix aparell conviuen fotos personals, aplicacions d'oci i documents confidencials o dades de clients.

## Diapositiva 3

**DILEMA PRIVACITAT VS SEGURETAT**

**Coexistència de Dades Personals i Corporatives**

**Àmbit Personal**

**Àmbit Corporatiu**

• Fotografies, vídeos i fitxers privats.

• Documents confidencials, bases de dades i claus d'accés.

• Xarxes socials i aplicacions d'oci.

• Correu corporatiu i eines de comunicació interna.

• Drets de privacitat indiscutibles per a l'empleat.

• Requisits de compliment de protecció de dades (RGPD).

## Diapositiva 4

**AVALUACIÓ DE RISCS**

**BYOD Amplia el Vector d'Intrusió a la Xarxa**

**Programari no Controlat**

**Fuga de Dades per Pèrdua**

**Enginyeria Social i Phishing**

L'usuari pot tenir instal·lades aplicacions amb vulnerabilitats, eines sense actualitzar o jocs amb malware ocult.

Si el mòbil o el portàtil privat es perd o és robat, qualsevol persona pot accedir a la informació interna si no està xifrat.

Els dispositius personals tenen menys filtres i proteccions contra enganys de Phishing que els equips gestionats per TI.

## Diapositiva 5

**INSUFICIÈNCIA DE PROTECCIONS TRADICIONALS**

**Per què un Tallafoc Bàsic no és Suficient?**

**El Límit del Perímetre**

**L'Objectiu: Assegurar els Actius**

Un tallafoc (Firewall) tradicional protegeix la frontera de la xarxa, però quan un usuari connecta el seu dispositiu infectat per VPN o Wi-Fi interna, **l'amenaça ja està dins del perímetre**.

Cal exercir un control actiu directament sobre l'extrem (endpoint) sense violar la privacitat de l'usuari.

**Així neix la necessitat dels sistemes MDM (Mobile Device Management).**

## Diapositiva 6

**EINES DE CONTROL**

**MDM (Mobile Device Management): La Solució Corporativa**

**Definició de MDM**

**Equilibri entre Control i Privacitat**

Programari centralitzat que permet als administradors de TI monitoritzar, gestionar i aplicar polítiques de seguretat en els dispositius mòbils que accedeixen a la xarxa.

Permet a l'empresa protegir les seves dades **sense poder veure ni accedir a les fotos, xats o aplicacions personals** de l'empleat.

• Automatitza la configuració d'equips remots.

• Distribueix aplicacions autoritzades de forma segura.

## Diapositiva 7

**AÏLLAMENT DE DADES**

**Funcionalitat MDM: Contenidors Segurs**

**Separació Lògica a l'Ordinador/Mòbil**

**Protecció contra Malware Personal**

L'MDM crea un **"espai de treball xifrat i aïllat"** (sandbox) dins del dispositiu personal.

• Les aplicacions corporatives (Outlook, Teams, Drives) funcionen dins del contenidor.

Si un usuari descarrega una aplicació infectada al seu entorn personal, el malware **no pot creuar la frontera del contenidor segur** per extreure fitxers de l'empresa.

• Es bloqueja la possibilitat de copiar/enganxar dades de l'espai corporatiu cap a l'espai personal.

## Diapositiva 8

**RESPOSTA DAVANT DE PÈRDUES**

**Funcionalitat MDM: Esborrat Remot (Wipe)**

**Esborrat Corporatiu Selectiu**

**Bloqueig de Seguretat**

Si l'empleat perd el telèfon o deixa l'empresa, l'administrador pot enviar una ordre d'esborrat que destrueix **únicament les dades de l'empresa**.

Permet bloquejar el terminal a l'acte i revocar els certificats d'accés a la xarxa des del moment en què es notifica la pèrdua.

**Les fotos i documents personals de l'usuari no es veuen afectats.**

## Diapositiva 9

**CONTROL D'ACCÉS**

**Funcionalitat MDM: Polítiques de Seguretat Requerides**

**Autenticació Forta (PIN / Biometria)**

Verifica que el dispositiu tingui el xifratge integrat activat (BitLocker, FileVault, Android/iOS Encryption).

**Xifratge Obligatori de Disc**

**Verificació d'Integritat (No Root / Jailbreak)**

Obliga l'usuari a establir un PIN complex o desbloqueig biomètric per poder connectar-se a la xarxa corporativa.

Denega l'accés si es detecta que el dispositiu ha estat alterat (root o jailbreak), ja que inhabilita les proteccions del SO.

## Diapositiva 10

**COMPARATIVA TECNOLÒGICA**

**Escenari BYOD: Sense MDM vs. Amb MDM**

| Característica / Afectació | Escenari BYOD Sense MDM | Escenari BYOD Amb MDM |
|---|---|---|
| Aïllament de Dades | Nul. Dades personals i de l'empresa barrejades | Alt. Contenidors corporatius xifrats i aïllats |
| Acció davant de Pèrdua | Fuga imminent de dades confidencials | Esborrat remot selectiu de les dades de l'empresa |
| Compliment de Requisits | Depèn de la bona voluntat de l'usuari | Automàtic. Bloqueig si no es compleix la política PIN/Xifratge |
| Risc de Malware | Alt. Infecta la xarxa des del dispositiu privat | Mitigat. El malware no pot accedir al contenidor de feina |

## Diapositiva 11

**ARQUITECTURA GLOBAL**

**Integració de BYOD en una Estratègia Zero Trust**

**1. Validació de Salut (Posture Check)**

El dispositiu BYOD només rep accés a les aplicacions estrictament necessàries per al seu treball, no a tota la xarxa.

**2. Mínim Privilegi**

El monitoratge contínuament verifica si el patró del dispositiu canvia o si mostra comportaments anòmals.

**3. Continuïtat de Vigilància**

Abans de connectar, el sistema comprova si el dispositiu compleix les regles de l'MDM (sistema actualitzat, sense root).

## Diapositiva 12

![Imatge 3](@@IMG@@/img-003.jpg){ loading=lazy }

![Imatge 4](@@IMG@@/img-004.png){ loading=lazy }

**Resum d'Estudi - BYOD i MDM**

Adoptar el model **BYOD** permet flexibilitat, però amplia el vector d'intrusió. La implementació de solucions **MDM** és indispensable per crear **contenidors segurs**, executar **esborrats remots selectius** i mantenir la seguretat corporativa sense vulnerar la privacitat dels usuaris.
