---
description: Arquitectura de Firewall, servidors Proxy, estructures DMZ i túnels VPN.
pdf: ""
---

# Tallafocs, Proxies, DMZ i Xarxes Privades Virtuals (VPN)

## Tallafocs (Firewall)
Examina i aconsegueix o denega el tràfic de dades entre xarxes segons un conjunt de regles.

- **Polítiques:**
  - **Permissiva:** Tot el que no està prohibit explicitament, està permès.
  - **Restrictiva:** Tot el que no està permès explicitament, està prohibit (recomanada).
- **Tipus:**
  - **Filtre de paquets clàssic:** Analitza només IP origen/destí i ports (Capa 3 i 4).
  - **NGFW (Next-Generation Firewall):** Inspecciona el contingut del paquet (Capa 7 - Aplicació) per detectar amenaces amagades.

## Xarxa DMZ (Zona Desmilitaritzada)
Zona d'aïllament intermèdia entre Internet i la xarxa local interna (LAN).
- S'hi ubiquen els servidors públics (Web, Correu, DNS).
- Si un servidor de la DMZ és conculcat, el tallafocs impedeix l'accés directe cap a la LAN interna.

## Servidor Proxy
Intermediari a nivell d'aplicació per a les peticions dels usuaris a Internet.
- **Funcions:** Filtratge de continguts, emmagatzematge en memòria cau (*cache*) i ocultació de la IP client per privadesa.

### Comparativa: Firewall vs Proxy
| Concepte | Firewall (El Porter) | Proxy (L'Intermediari) |
|---|---|---|
| **Nivell d'actuació** | Capa de Xarxa / Transport (IP, Ports) | Capa d'Aplicació (HTTP, Fitxers) |
| **Objectiu** | Permetre o bloquejar connexions | Processar la petició en nom de l'usuari |

## VPN (Virtual Private Network)
Crea un túnel privat i xifrat que circula a través d'una xarxa pública com Internet.

- **Mecanisme:** Les dades se xifren i s'encapsulen dins de paquets estàndard d'Internet.
- **Casos d'ús:** Teletreball segur, connexió a Wi-Fi públiques i privadesa d'IP.
- **Protocols comuns:**
  - **OpenVPN:** Estàndard de codi obert, altament segur.
  - **WireGuard:** Protocol modern, extremadament ràpid i eficient.
  - **IPsec:** Utilitzat principalment per a unions xarxa-a-xarxa (*Site-to-Site*).