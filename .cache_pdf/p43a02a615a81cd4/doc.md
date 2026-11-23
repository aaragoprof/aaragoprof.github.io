# Monitoratge de Xarxes, SNMP i Enginyeria Social

## Diapositiva 1

**SEGURETAT I ADMINISTRACIÓ DE SISTEMES**

**Monitoratge de Xarxes, SNMP i Enginyeria Social**

Inventari de recursos, gestió centralitzada i defensa davant fraus informàtics

## El Monitoratge de Xarxes

<div class="md-card" markdown="1">

**Qualitat de servei:** Rendiment òptim.

**Control d'accés:** Només usuaris autoritzats.

**Anàlisi proactiva:** Detecció ràpida d'errors.

</div>

**Anàlisi contínua del trànsit i estat de la xarxa.**

Garanteix la qualitat de servei i assegura l'ús exclusiu per part d'usuaris legítims.

## Factors Clau d'Inventari i Control

<div class="md-cards" markdown="1">

<div class="md-card" markdown="1">

### Adreces IP i MAC

Identificació lògica i física d'equips.

</div>

<div class="md-card" markdown="1">

### Ports i Serveis

Control de serveis crítics actius.

</div>

<div class="md-card" markdown="1">

### Protocol SNMP

Supervisió centralitzada de dispositius.

</div>

</div>

## Protocol SNMP

**Simple Network Management Protocol**

Estàndard que permet als dispositius de xarxa comunicar-se amb una consola central.

<div class="md-cards" markdown="1">

<div class="md-card" markdown="1">

### Inventari Dinàmic

Detecta equips i serveis actius.

</div>

<div class="md-card" markdown="1">

### Control de Rendiment

Vigila CPU, memòria i trànsit.

</div>

<div class="md-card" markdown="1">

### Detecció d'Anomalies

Alerta davant canvis no autoritzats.

</div>

</div>

## Arquitectura del Sistema SNMP

<div class="md-cards" markdown="1">

<div class="md-card" markdown="1">

### 1

**Agent SNMP**

Programari integrat al dispositiu vigilat.

</div>

<div class="md-card" markdown="1">

### 2

**Base MIB**

Base jeràrquica de paràmetres consultables.

</div>

<div class="md-card" markdown="1">

### 3

**Estació NMS**

Servidor central (Zabbix, Nagios, PRTG).

</div>

</div>

## Seguretat en les Versions SNMP

<div class="md-cards" markdown="1">

<div class="md-card" markdown="1">

### SNMPv1 / v2c

- **Sense xifratge:** Dades en text pla.
- **Comunitat exposada:** Contrasenya vulnerable.

</div>

<div class="md-card" markdown="1">

### SNMPv3 (Recomanat)

- **Autenticació:** Verifica identitat de l'origen.
- **Privadesa:** Xifratge imprescindible del trànsit.

</div>

</div>

## Diapositiva 7

**SEGONA PART**

**Fraus Informàtics i Enginyeria Social**

## Diapositiva 8

**Concepte d'Enginyeria Social**

**«Obtenció d'informació confidencial mitjançant la manipulació o l'engany d'usuaris legítims.»**

Exemples principals: Phishing i estafes bancàries

## Defensa contra el Phishing

<div class="md-cards" markdown="1">

<div class="md-card" markdown="1">

### Conscienciació

Desconfiar de correus que demanin dades.

</div>

<div class="md-card" markdown="1">

### Autenticació (2FA)

Doble verificació i contrasenyes úniques.

</div>

</div>

<div class="md-cards" markdown="1">

<div class="md-card" markdown="1">

### Sistemes al Dia

Actualitzacions i antivirus actius.

</div>

<div class="md-card" markdown="1">

### Xarxes Segures

Evitar xarxes Wi-Fi públiques obertes.

</div>

</div>

## Hoax i Notícies Falses (Fake News)

<div class="md-card" markdown="1">

### Exemple: Cas Adamuz

Vídeo fals sobre esquerdes ferroviàries generat amb IA.

</div>

**Missatges falsos difosos massivament per enganyar o viralitzar contingut.**

Sovint utilitzen vídeos o imatges manipulades amb Intel·ligència Artificial per generar alarma social.

## Diferència Clau: Phishing vs. Pharming

<div class="md-card" markdown="1">



</div>

| Característica | Phishing | Pharming |
|---|---|---|
| Mecanisme | Engany directe via correu o missatge | Manipulació del sistema DNS |
| Acció de l'usuari | Fa clic en un enllaç fraudulent | Escriu l'adreça web correcta |
| Resultat | Accedeix a una web falsa | Redirecció automàtica a web falsa |

## Diapositiva 12

**Seguretat Integral a la Xarxa**

Combina la supervisió tècnica amb **SNMPv3** i la formació constant dels usuaris contra l'enginyeria social.
