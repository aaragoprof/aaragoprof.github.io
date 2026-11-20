# Firewall i VPN

<p class="md-kicker">MÒDUL DE SEGURETAT I XARXES</p>

Material d'estudi: Protecció Perimetral, Arquitectura DMZ, Servidors Proxy i Túnels Xifrats de Xarxa Privada Virtual

## Què és i per a què serveix un Firewall (Tallafocs)?

<p class="md-kicker">PROTECCIÓ PERIMETRAL</p>

Si la xarxa corporativa és un edifici, el **Firewall** és el porter situat a l'entrada decidint de manera rigorosa quin trànsit té permès l'accés i quin queda bloquejat.

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### Inspecció de Paquets

Examina cada paquet de dades que intenta creuar entre xarxes (per exemple, d'Internet a la xarxa local) aplicant un conjunt de regles definides.

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### Polítiques de Configuració

- **Permissiva:** Tot el que no està prohibit, està permès.
- **Restrictiva (Recomanada):** Tot el que no està permès, està estrictament prohibit.

</div>

</div>

## Filtre de Paquets Clàssic vs. NGFW (Next-Gen)

<p class="md-kicker">EVOLUCIÓ TECNOLÒGICA</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#64748B" markdown="1">

### Filtre Clàssic (Capa 3 / 4)

Només avalua adreces IP d'origen/destí i el número de port.

<div class="md-callout" markdown="1">

**Analogia:** Com un porter que només revisa el DNI a la porta sense comprovar què porta la persona a la bossa.

</div>

</div>

<div class="md-card" style="--card:#0284C7" markdown="1">

### NGFW - Next-Generation (Capa 7)

Inspecciona el contingut real de l'aplicació dins del paquet (Deep Packet Inspection).

<div class="md-callout" style="--card:#0284C7" markdown="1">

**Detecta si el trànsit pel port segur 443 (HTTPS) és navegació legítima o un malware intentant camuflar-se.**

</div>

</div>

</div>

## Què és una DMZ (Zona Desmilitaritzada)?

<p class="md-kicker">DISSENY DE XARXA SEGURA</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#F59E0B" markdown="1">

### Aïllament de Servidors Públics

Xarxa intermèdia aïllada on es col·loquen els servidors que han de rebre connexions des d'Internet (Web, Correu, DNS).

**Objectiu:** Si un atacant compromet un servidor de la DMZ, el Firewall impedeix que pugui saltar directament a la xarxa interna.

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### Estrutura de 3 Potes (Zones)

- **1. Internet:** Zona no fiable (pública).
- **2. DMZ:** Zona de servidors d'accés extern.
- **3. LAN Interna:** Zona d'alta seguretat (equips d'usuaris i bases de dades).

</div>

</div>

## Què és el Servidor Proxy?

<p class="md-kicker">INTERMEDIACIÓ D'APLICACIÓ</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### El "Missatger" d'Aplicació

Actua com a intermediari entre el client i el servidor de destinació. L'usuari mai no connecta directament a la web final.

- El client demana el contingut al Proxy.
- El Proxy sol·licita la pàgina a Internet i la lliura al client.

</div>

<div class="md-card" style="--card:#8B5CF6" markdown="1">

### Avantatges Principals

- **Filtratge de contingut:** Bloqueig de categories o llocs web no permesos.
- **Caché local:** Emmagatzema continguts freqüents per accelerar la xarxa.
- **Privadesa d'IP:** Mascara l'adreça IP real del client intern.

</div>

</div>

## Diapositiva 6

**DIFERÈNCIES CLAU**

**Firewall vs. Proxy: Roles i Diferències**

| Característica | El Firewall ("El Porter") | El Proxy ("L'Intermediari") |
|---|---|---|
| Capa d'Actuació | Nivell de Xarxa i Transport (Capa 3 / 4) | Nivell d'Aplicació (Capa 7 - Navegador Web) |
| Criteri de Decisió | Adreces IP d'origen/destí i número de port | Contingut del fitxer, lloc web i usuari concret |
| Acció Principal | Obre o tanca la connexió física de trànsit | Fa la petició en nom de l'usuari i gestiona memòria cau |
| Exemple d'Ús | "Bloquejar totes les connexions d'entrada al port 22" | "Bloquejar l'accés a xarxes socials durant l'horari lectiu" |

## Què és una VPN (Virtual Private Network)?

<p class="md-kicker">TÚNELS DE SEGURETAT</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### L'Analogia de l'Autopista i el Túnel

Internet és com una **autopista pública** per on circula el trànsit de tothom. Si envies paquets sense protecció, qualsevol *sniffer* pot veure les dades.

<div class="md-callout" style="--card:#0284C7" markdown="1">

**Una VPN construeix un túnel privat i acorçat que discorre per dins d'aquesta autopista pública. Tot el que viatja pel túnel va xifrat.**

</div>

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### Protecció contra l'Escoltai

Encara que un atacant estigui monitoritzant la xarxa pública, no pot desxifrar les dades que circulen a l'interior del túnel VPN.

</div>

</div>

## Com Funciona una Connexió VPN?

<p class="md-kicker">MECANISME TÈCNIC</p>

<div class="md-callout" style="--card:#0284C7" markdown="1">

**1. Xifratge de dades:** L'ordinador del client embolcalla les dades originals en un sobre xifrat que només el servidor VPN destí pot obrir.

</div>

<div class="md-callout" style="--card:#EAB308" markdown="1">

**2. Encapsulament (Tunneling):** Aquest sobre xifrat s'introdueix dins d'un altre paquet estàndard per poder viatjar per Internet sense ser interceptat.

</div>

<div class="md-callout" style="--card:#16A34A" markdown="1">

**3. Desencapsulament i Lliurament:** En arribar al servidor VPN de l'empresa, es desxifra el contingut i es lliura a la LAN com si el client estigués connectat per cable presencial.

</div>

## Per a què es Fà Servir una VPN?

<p class="md-kicker">APLICACIONS PRÀCTIQUES</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### Teletreball Segur

Permet que els empleats accedeixin a carpetes compartides i aplicacions internes des de casa de forma xifrada.

</div>

<div class="md-card" style="--card:#EF4444" markdown="1">

### Protecció en Wi-Fi Públiques

Mantingues les dades il·legibles per a altres usuaris o hackers que estiguin a la mateixa xarxa en cafeteries o aeroports.

</div>

<div class="md-card" style="--card:#8B5CF6" markdown="1">

### Privadesa d'Ubicació (IP)

Oculta la IP real del client; a ulls d'Internet la connexió prové de la IP pública del servidor VPN.

</div>

</div>

## Principals Protocols de VPN

<p class="md-kicker">TECNOLOGIES DE TÚNEL</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### OpenVPN

L'estàndard tradicional més utilitzat. De codi obert, altament segur i compatible amb la majoria de sistemes operatius.

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### WireGuard

El protocol més modern. Extremadament ràpid, eficient en codi i basat en criptografia d'última generació.

</div>

<div class="md-card" style="--card:#8B5CF6" markdown="1">

### IPsec

S'utilitza principalment per connectar dues seus corporatives fixes entre si (túnel Site-to-Site entre routers).

</div>

</div>

## Integració: Firewall, DMZ, Proxy i VPN

<p class="md-kicker">SÍNTESI DEL RA</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### 1. Filtre Externe (FW + DMZ)

El Firewall controla l'accés perimetral i aïlla els servidors públics a la DMZ per evitar intrusions a la LAN.

</div>

<div class="md-card" style="--card:#8B5CF6" markdown="1">

### 2. Control d'Aplicació (Proxy)

El Proxy gestiona la navegació web dels usuaris interns, aplicant filtratge de continguts i acceleració per caché.

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### 3. Accés Remot (VPN)

La VPN garanteix un túnel xifrat per connectar equips remots o seus de forma 100% segura.

</div>

</div>

## Resum d'Estudi - Firewall i VPN

Una arquitectura de xarxa robusta exigeix la combinació de **Firewalls NGFW** per al control de paquets, estructures **DMZ** per a servidors públics, **Proxies** per al filtratge web d'aplicació i túnels **VPN (WireGuard/OpenVPN)** per garantir el xifratge d'extrem a extrem.
