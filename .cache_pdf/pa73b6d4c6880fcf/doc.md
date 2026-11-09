# Firewall i VPN - Protecció Perimetral i Túnels Segurs

## Diapositiva 1

![Imatge 1](@@IMG@@/img-001.jpg){ loading=lazy }

![Imatge 2](@@IMG@@/img-002.png){ loading=lazy }

**Firewall i VPN**

**MÒDUL DE SEGURETAT I XARXES**

Material d'estudi: Protecció Perimetral, Arquitectura DMZ, Servidors Proxy i Túnels Xifrats de Xarxa Privada Virtual

## Diapositiva 2

**PROTECCIÓ PERIMETRAL**

**Què és i per a què serveix un Firewall (Tallafocs)?**

Si la xarxa corporativa és un edifici, el **Firewall** és el porter situat a l'entrada decidint de manera rigorosa quin trànsit té permès l'accés i quin queda bloquejat.

**Inspecció de Paquets**

**Polítiques de Configuració**

Examina cada paquet de dades que intenta creuar entre xarxes (per exemple, d'Internet a la xarxa local) aplicant un conjunt de regles definides.

• **Permissiva:** Tot el que no està prohibit, està permès.

• **Restrictiva (Recomanada):** Tot el que no està permès, està estrictament prohibit.

## Diapositiva 3

**EVOLUCIÓ TECNOLÒGICA**

**Filtre de Paquets Clàssic vs. NGFW (Next-Gen)**

**Filtre Clàssic (Capa 3 / 4)**

**NGFW - Next-Generation (Capa 7)**

Només avalua adreces IP d'origen/destí i el número de port.

Inspecciona el contingut real de l'aplicació dins del paquet (Deep Packet Inspection).

**Analogia:** Com un porter que només revisa el DNI a la porta sense comprovar què porta la persona a la bossa.

**Detecta si el trànsit pel port segur 443 (HTTPS) és navegació legítima o un malware intentant camuflar-se.**

## Diapositiva 4

**DISSENY DE XARXA SEGURA**

**Què és una DMZ (Zona Desmilitaritzada)?**

**Aïllament de Servidors Públics**

**Estrutura de 3 Potes (Zones)**

Xarxa intermèdia aïllada on es col·loquen els servidors que han de rebre connexions des d'Internet (Web, Correu, DNS).

• **1. Internet:** Zona no fiable (pública).

**Objectiu:** Si un atacant compromet un servidor de la DMZ, el Firewall impedeix que pugui saltar directament a la xarxa interna.

• **2. DMZ:** Zona de servidors d'accés extern.

• **3. LAN Interna:** Zona d'alta seguretat (equips d'usuaris i bases de dades).

## Diapositiva 5

**INTERMEDIACIÓ D'APLICACIÓ**

**Què és el Servidor Proxy?**

**El "Missatger" d'Aplicació**

**Avantatges Principals**

Actua com a intermediari entre el client i el servidor de destinació. L'usuari mai no connecta directament a la web final.

• **Filtratge de contingut:** Bloqueig de categories o llocs web no permesos.

• El client demana el contingut al Proxy.

• **Caché local:** Emmagatzema continguts freqüents per accelerar la xarxa.

• El Proxy sol·licita la pàgina a Internet i la lliura al client.

• **Privadesa d'IP:** Mascara l'adreça IP real del client intern.

## Diapositiva 6

**DIFERÈNCIES CLAU**

**Firewall vs. Proxy: Roles i Diferències**

| Característica | El Firewall ("El Porter") | El Proxy ("L'Intermediari") |
|---|---|---|
| Capa d'Actuació | Nivell de Xarxa i Transport (Capa 3 / 4) | Nivell d'Aplicació (Capa 7 - Navegador Web) |
| Criteri de Decisió | Adreces IP d'origen/destí i número de port | Contingut del fitxer, lloc web i usuari concret |
| Acció Principal | Obre o tanca la connexió física de trànsit | Fa la petició en nom de l'usuari i gestiona memòria cau |
| Exemple d'Ús | "Bloquejar totes les connexions d'entrada al port 22" | "Bloquejar l'accés a xarxes socials durant l'horari lectiu" |

## Diapositiva 7

**TÚNELS DE SEGURETAT**

**Què és una VPN (Virtual Private Network)?**

**L'Analogia de l'Autopista i el Túnel**

**Protecció contra l'Escoltai**

Internet és com una **autopista pública** per on circula el trànsit de tothom. Si envies paquets sense protecció, qualsevol *sniffer* pot veure les dades.

Encara que un atacant estigui monitoritzant la xarxa pública, no pot desxifrar les dades que circulen a l'interior del túnel VPN.

**Una VPN construeix un túnel privat i acorçat que discorre per dins d'aquesta autopista pública. Tot el que viatja pel túnel va xifrat.**

## Diapositiva 8

**MECANISME TÈCNIC**

**Com Funciona una Connexió VPN?**

**1. Xifratge de dades:** L'ordinador del client embolcalla les dades originals en un sobre xifrat que només el servidor VPN destí pot obrir.

**2. Encapsulament (Tunneling):** Aquest sobre xifrat s'introdueix dins d'un altre paquet estàndard per poder viatjar per Internet sense ser interceptat.

**3. Desencapsulament i Lliurament:** En arribar al servidor VPN de l'empresa, es desxifra el contingut i es lliura a la LAN com si el client estigués connectat per cable presencial.

## Diapositiva 9

**APLICACIONS PRÀCTIQUES**

**Per a què es Fà Servir una VPN?**

**Teletreball Segur**

**Protecció en Wi-Fi Públiques**

**Privadesa d'Ubicació (IP)**

Permet que els empleats accedeixin a carpetes compartides i aplicacions internes des de casa de forma xifrada.

Mantingues les dades il·legibles per a altres usuaris o hackers que estiguin a la mateixa xarxa en cafeteries o aeroports.

Oculta la IP real del client; a ulls d'Internet la connexió prové de la IP pública del servidor VPN.

## Diapositiva 10

**TECNOLOGIES DE TÚNEL**

**Principals Protocols de VPN**

**OpenVPN**

**WireGuard**

**IPsec**

L'estàndard tradicional més utilitzat. De codi obert, altament segur i compatible amb la majoria de sistemes operatius.

El protocol més modern. Extremadament ràpid, eficient en codi i basat en criptografia d'última generació.

S'utilitza principalment per connectar dues seus corporatives fixes entre si (túnel Site-to-Site entre routers).

## Diapositiva 11

**SÍNTESI DEL RA**

**Integració: Firewall, DMZ, Proxy i VPN**

**1. Filtre Externe (FW + DMZ)**

**2. Control d'Aplicació (Proxy)**

**3. Accés Remot (VPN)**

El Firewall controla l'accés perimetral i aïlla els servidors públics a la DMZ per evitar intrusions a la LAN.

El Proxy gestiona la navegació web dels usuaris interns, aplicant filtratge de continguts i acceleració per caché.

La VPN garanteix un túnel xifrat per connectar equips remots o seus de forma 100% segura.

## Diapositiva 12

![Imatge 3](@@IMG@@/img-003.jpg){ loading=lazy }

![Imatge 4](@@IMG@@/img-004.png){ loading=lazy }

**Resum d'Estudi - Firewall i VPN**

Una arquitectura de xarxa robusta exigeix la combinació de **Firewalls NGFW** per al control de paquets, estructures **DMZ** per a servidors públics, **Proxies** per al filtratge web d'aplicació i túnels **VPN (WireGuard/OpenVPN)** per garantir el xifratge d'extrem a extrem.
