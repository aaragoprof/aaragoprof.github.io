# Monitoratge\_de\_xarxes\_SNMP\_Phishing

## Diapositiva 1

Monitoratge de Xarxes i Enginyeria Social

SNMP, Gestió d'Inventaris, Phishing, Hoax i Pharming

## Introducció al Monitoratge de Xarxes

2 / 12

<div class="md-callout" markdown="1">

Per garantir la Qualitat de Servei (QoS) i la seguretat en una xarxa informàtica, cal disposar de mecanismes de control continu.

Definició: Conjunt d'eines i mecanismes utilitzats per capturar, analitzar i interpretar la informació que circula a la xarxa.

Control d'accés legítim: Assegura que només els usuaris autoritzats accedeixen als recursos en els termes establerts.

Avaluació del rendiment i detecció d'anomalies: Identifica colls d'ampolla i comportaments inusuals abans de caigudes del sistema.

</div>

## Inventari i Control dels Serveis de Xarxa

3 / 12

<div class="md-callout" markdown="1">

En xarxes complexes, la gestió comença per conèixer de manera exacta tots els recursos de la xarxa.

Mètode de protecció: Saber quins equips i serveis formen part de la xarxa facilita la detecció immediata d'intrusos.

Rang d'adreces IP i MAC: Control de l'assignació lògica i física de les targetes de xarxa autoritzades.

Ports oberts i serveis actius: Monitoratge dels serveis en execució (web, DNS, correu, bases de dades) i ús de SNMP.

</div>

## Què és el Protocol SNMP?

4 / 12

<div class="md-callout" markdown="1">

SNMP (Simple Network Management Protocol): Protocol estàndard de la capa d'aplicació per a l'intercanvi d'informació de gestió.

Funció principal: Permet que dispositius heterogenis (routers, switches, servidors, impressores, SAI) parlin amb una consola central.

Inventari dinàmic: Permet conèixer en temps real els equips connectats i serveis actius.

Control de rendiment: Mesura constant de l'ús de CPU, memòria RAM, espai en disc i tràfic de xarxa per evitar col·lapses.

</div>

## Arquitectura i Components SNMP

5 / 12

<div class="md-callout" markdown="1">

Agent SNMP: Programari o servei executat al dispositiu a vigilar (router, switch, servidor) que recull informació local.

NMS (Network Management Station): Servidor central de gestió que recull i visualitza les dades (ex: Zabbix, Nagios, PRTG).

MIB (Management Information Base): Base de dades jeràrquica que defineix quines variables es poden consultar en cada equip.

Flux de treball: El NMS envia una petició (GET), l'Agent consulta la MIB i retorna la informació corresponent.

</div>

## Versions i Seguretat en SNMP

6 / 12

<div class="md-callout" markdown="1">

SNMPv1 i SNMPv2c: Ampliament utilitzats històricament, però insegurs perquè transmeten la 'comunitat' (contrasenya) en text pla.

SNMPv3 - Estàndard actual i segur: Incorpora el xifratge i l'autenticació com a característiques imprescindibles.

Mecanisme d'Autenticació: Garanteix que la petició prové d'una font legítima i autoritzada.

Mecanisme de Privadesa: Xifra tot el tràfic de gestió (AES/DES) per evitar la lectura de dades no autoritzada a la xarxa.

</div>

## Fraus Informàtics i Enginyeria Social

7 / 12

<div class="md-callout" markdown="1">

Enginyeria Social: Pràctica d'obtenir informació confidencial, credencials o accés mitjançant la manipulació psicològica d'usuaris.

Focus de l'atac: En lloc d'atacar fallades de maquinari o programari, s'aprofita de l'element humà com a punt feble.

Phishing: Suplantació d'identitat mitjançant correus o missatges fraudulents per robar dades confidencials.

Estafes bancàries: Robatori de credencials financeres utilitzant plataformes o trucades falses (Vishing/Smishing).

</div>

## Mecanismes de Defensa contra el Phishing

8 / 12

<div class="md-callout" markdown="1">

Mesura principal: Conscienciació i formació contínua dels usuaris davant els riscos de l'enginyeria social.

Regla general d'or: Ignorar qualsevol correu electrònic o missatge que sol·liciti dades personals o privades.

Doble Verificació (2FA/MFA): Implementació d'un segon factor d'autenticació obligatori per accedir als serveis.

Higiene digital: Contrasenyes segures i úniques, navegació amb VPN en xarxes públiques i actualització de sistemes.

</div>

## HOAX i Fake News en la Xarxa

9 / 12

<div class="md-callout" markdown="1">

Concepte de HOAX: Missatge fals difós massivament per internet (correu, xarxes socials, missatgeria) per enganyar o crear alarma.

Impacte en la xarxa: Provoca desinformació, col·lapsa la xarxa i pot servir de mètode de redistribució de malware.

Impacte de la Intel·ligència Artificial: Generació d'imatges i vídeos falsos d'alt realisme (Deepfakes) per viralitzar hoaxos.

Exemple pràctic: Circulació de contingut manipulat per IA sobre esquerdes fictícies en vies de tren en incidents de trànsit.

</div>

## Pharming: Redirecció Invisible

10 / 12

<div class="md-callout" markdown="1">

Concepte de Pharming: Atac que redirecciona l'usuari a una web falsa encara que hagi escrit correctament l'adreça URL.

Objectiu maliciós: Robatori d'informació sensible com contrasenyes, dades personals o credencials bancàries.

Mecanisme d'atac: Es realitza manipulant el servidor DNS (DNS Poisoning) o l'arxiu local 'hosts' de la víctima.

Risc elevat: L'usuari no detecta l'engany a l'adreça teclejada, ja que la URL introduïda és la legítima.

</div>

## Diferència Clau: Phishing vs. Pharming

11 / 12

<div class="md-callout" markdown="1">

Phishing (Acció de clic): L'engany es produeix quan l'usuari fa clic en un enllaç fraudulent enviat per correu o missatge.

Pharming (Redirecció tècnica): L'usuari escriu la web bona, però la infraestructura DNS manipulada el porta a la web falsa.

Nivell de dificultat de detecció: El Pharming és molt més difícil de detectar i requereix verificar el certificat SSL/TLS.

Defensa preventiva: Protecció dels servidors DNS (DNSSEC) i instal·lació d'antivirus amb protecció web en temps real.

</div>

## Resum i Integració de Seguretat de Xarxa

12 / 12

<div class="md-callout" markdown="1">

Monitoratge d'Infraestructura: SNMPv3 com a aliat clau per mantenir inventari actiu i controlar el rendiment.

Protecció del Perímetre i Serveis: Filtratge de ports, inventari IP/MAC i segmentació per mantenir la integritat.

Mitigació de l'Enginyeria Social: Programes de capacitació contra Phishing, Hoax i noves amenaces generades per IA.

Seguretat Web Global: Verificació de certificats digitals HTTPS i encriptació per fer front al Pharming i sniffing.

</div>
