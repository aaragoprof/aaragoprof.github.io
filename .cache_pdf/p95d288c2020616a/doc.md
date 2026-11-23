# Monitoratge de Xarxes, SNMP i Enginyeria Social

<p class="md-kicker">MÒDUL DE SEGURETAT I MONITORATGE</p>

Inventari d'actius, gestió centralitzada amb SNMPv3 i defensa davant fraus informàtics

## Objectius del Monitoratge de Xarxes

<p class="md-kicker">QUALITAT I CONTROL</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### Qualitat de Servei

Anàlisi contínua del trànsit per garantir un rendiment òptim.

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### Usuaris Legítims

Control d'accés estrictament sota les polítiques dels administradors.

</div>

<div class="md-card" style="--card:#EAB308" markdown="1">

### Detecció d'Intrusos

Visibilitat total dels recursos per identificar equips no autoritzats.

</div>

</div>

## Factors Clau d'Inventari de Xarxa

<p class="md-kicker">GESTIÓ D'ACTIUS</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### Adreçament IP i MAC

Control de rangs lògics IP i inventari físic d'adreces MAC.

</div>

<div class="md-card" style="--card:#0284C7" markdown="1">

### Ports i Serveis Actius

Supervisió de ports oberts i serveis crítics exposats.

</div>

<div class="md-card" style="--card:#0284C7" markdown="1">

### Protocol SNMP

Consulta automatitzada d'estat i mètriques en temps real.

</div>

</div>

## Protocol SNMP (Simple Network Management Protocol)

<p class="md-kicker">ESTÀNDARD DE GESTIÓ</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### Llenguatge Comú de Xarxa

Permet que encaminadors, commutadors, servidors i impressores es comuniquin amb una consola central.

</div>

<div class="md-card" style="--card:#0284C7" markdown="1">

### Funcions Principals

- **Inventari dinàmic:** Equips connectats.
- **Rendiment:** Ús de CPU, RAM i trànsit.
- **Anomalies:** Alerta de canvis sospitosos.

</div>

</div>

## Com Funciona l'Arquitectura SNMP?

<p class="md-kicker">COMPONENTS TÈCNICS</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### 1. Agent SNMP

Programari integrat dins el dispositiu vigilat (router, switch o servidor).

</div>

<div class="md-card" style="--card:#8B5CF6" markdown="1">

### 2. Base MIB

Base de dades jeràrquica que defineix els paràmetres consultables.

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### 3. Estació NMS

Servidor central que recull i visualitza dades (Zabbix, Nagios, PRTG).

</div>

</div>

## Versions i Seguretat del Protocol SNMP

<p class="md-kicker">EVOLUCIÓ I XIFRATGE</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#EF4444" markdown="1">

### SNMPv1 / SNMPv2c (Insegur)

- Envia la contrasenya (comunitat) en text pla.
- Sense xifratge de dades durant el trànsit.

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### SNMPv3 (Estàndard Segur)

- **Autenticació:** Verifica la identitat de l'origen.
- **Privadesa:** Xifratge imprescindible dels paquets.

</div>

</div>

## Fraus Informàtics i Enginyeria Social

<p class="md-kicker">AMENACES HUMANES</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#E11D48" markdown="1">

### Manipulació Psicològica

Pràctica d'obtenir informació confidencial mitjançant l'engany o la manipulació d'usuaris legítims.

</div>

<div class="md-card" style="--card:#EAB308" markdown="1">

### Vectors Habituals

- **Phishing:** Suplantació via correu o SMS.
- **Estafes bancàries:** Robatori de credencials.

</div>

</div>

## Mecanismes de Defensa contra el Phishing

<p class="md-kicker">PREVENCIÓ ACTIVA</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### Conscienciació

Formar els usuaris per ignorar correus que demanin dades personals.

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### Doble Verificació

Activar 2FA i usar contrasenyes complexes i úniques per servei.

</div>

<div class="md-card" style="--card:#8B5CF6" markdown="1">

### Higiene Digital

Actualitzar sistemes, usar antivirus i evitar xarxes Wi-Fi obertes.

</div>

</div>

## Hoax i Notícies Falses (Fake News)

<p class="md-kicker">DESINFORMACIÓ VIRAL</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#EAB308" markdown="1">

### Definició de Hoax

Missatge fals difós massivament per correu o xarxes socials per enganyar i provocar la seva viralització.

</div>

<div class="md-card" style="--card:#EF4444" markdown="1">

### Cas Pràctic: Vídeo Adamuz

Difusió viral de suposades esquerdes ferroviàries creades amb contingut multimèdia generat per IA.

</div>

</div>

## Pharming: Manipulació de la Resolució Web

<p class="md-kicker">REDIRECCIÓ MALICIOSA</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#EF4444" markdown="1">

### Desviament Invisible

Redirigeix la víctima a una web falsa encara que escrigui l'URL correcta.

</div>

<div class="md-card" style="--card:#0284C7" markdown="1">

### Alteració del DNS

Manipula servidors DNS o el fitxer local d'adreces del dispositiu.

</div>

<div class="md-card" style="--card:#EAB308" markdown="1">

### Objectiu de l'Atac

Captura silenciosa de contrasenyes i credencials bancàries.

</div>

</div>

## Diferència Clau: Phishing vs. Pharming

<p class="md-kicker">COMPARATIVA TECNOLÒGICA</p>

<div class="md-card" markdown="1">



</div>

| Aspecte | Phishing | Pharming |
|---|---|---|
| Vector d'atac | Missatge enganyós (correu, SMS) | Enverinament de DNS o configuració local |
| Acció de la víctima | Fa clic en un enllaç fraudulent | Escriu l'adreça web legítima |
| Resultat tècnic | Obre un domini fals semblant | Redirecció automàtica a servidor fals |

## Resum d'Estudi - Monitoratge i Seguretat

Garantir la seguretat de la xarxa exigeix inventari constant, supervisió xifrada amb **SNMPv3** i formació dels usuaris contra el **Phishing**, **Hoax** i **Pharming**.
