---
description: Conceptes de monitoratge de xarxes, protocol SNMP, enginyeria social, phishing, hoaxes i pharming.
pdf: ""
---

# Monitoratge de xarxes i seguretat d'usuaris

## Conceptes bàsics
El **monitoratge de les xarxes** és el conjunt d'eines i mecanismes utilitzats per analitzar la informació transportada a la xarxa per extreure informació sobre el seu funcionament, garantir la qualitat del servei i assegurar que només els usuaris legítims hi accedeixin.

## Inventari i control de serveis
En xarxes complexes, un inventari actualitzat permet detectar intrusos no autoritzats fàcilment. Elements clau:
- Rang d'adreces IP
- Inventari d'adreces MAC
- Ports oberts i serveis actius
- Protocol SNMP

## Protocol SNMP (Simple Network Management Protocol)
Permet la comunicació entre dispositius de xarxa (routers, switches, servidors) i una consola central de gestió.

### Arquitectura SNMP
- **Agent SNMP:** Programari que s'executa en el dispositiu a vigilar.
- **NMS (Network Management Station):** Servidor central que recull les dades (ej. Zabbix, Nagios, PRTG).
- **MIB (Management Information Base):** Base de dades jeràrquica amb els paràmetres consultables.

### Versions
- **SNMPv1 / v2c:** Insegurs (envien la contrasenya/comunitat en text pla).
- **SNMPv3:** Versió segura amb **autenticació** i **privadesa (xifratge)**.

## Fraus informàtics i enginyeria social
L'**enginyeria social** és la manipulació d'usuaris legítims per obtenir informació confidencial.

- **Phishing:** Correus o missatges falsos per robar credencials. *Defensa principal:* Conscienciació i formació, no respondre correus sol·licitant dades personals, autenticació de doble factor (2FA) i contrasenyes segures.
- **Hoax (Fake News):** Missatges falsos difosos per xarxes socials per enganyar o generar dades virals falses.
- **Pharming:** Redirecció de l'usuari a una web falsa manipulant el sistema DNS o el fitxer hosts. A diferència del phishing, l'usuari escriu l'adreça web correcta però és redirigit automàticament.