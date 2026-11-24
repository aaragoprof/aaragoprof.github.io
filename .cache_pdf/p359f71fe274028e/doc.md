# Eines Preventives

<p class="md-kicker">MÒDUL DE SEGURETAT ACTIVA</p>

Gestió de contrasenyes, seguretat a l'arrencada, permisos a Linux, ACL, quotes i criptografia

## Gestió Segura de Contrasenyes

<p class="md-kicker">PROTECCIÓ DE CREDENCIALS</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### Creació Robusta

Mínim 12–16 caràcters o frases de pas úniques sense reutilització.

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### Gestors i MFA

Emmagatzematge xifrat (Bitwarden, KeePass) i autenticació multifactor obligatòria.

</div>

<div class="md-card" style="--card:#8B5CF6" markdown="1">

### Control Proactiu

Filtres contra contrasenyes filtrades i bloqueig davant força bruta.

</div>

</div>

## Nivells de Contrasenyes a l'Arrencada

<p class="md-kicker">PROTECCIÓ FÍSICA DE L'EQUIP</p>

<div class="md-card" markdown="1">



</div>

| Nivell d'Arrencada | Funció Preventiva | Tecnologies i Riscos |
|---|---|---|
| 1. Firmware (UEFI / BIOS) | Bloqueja l'arrencada des d'un Live USB extern | Secure Boot, xip TPM i xifratge complet de disc |
| 2. Gestor (GRUB 2) | Impedeix editar el nucli o iniciar en mode root | Contrasenyes emmagatzemades amb hash PBKDF2 |
| 3. Sistema Operatiu | Autenticació d'inici de sessió d'usuari | Feble en comptes locals sense xifrar (fitxer SAM) |

## Control d'Accés, ACL i Quotes de Disc

<p class="md-kicker">GOVERNANÇA DE RECURSOS</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### Protecció Crítica

Contrasenyes xifrades a accessibles només per root.

/etc/shadow

</div>

<div class="md-card" style="--card:#8B5CF6" markdown="1">

### Granularitat ACL

Permisos específics per a múltiples usuaris amb o NTFS.

setfacl

</div>

<div class="md-card" style="--card:#EAB308" markdown="1">

### Quotes de Disc

Límits amb FSRM o per evitar denegació de servei.

xfs\_quota

</div>

</div>

## Tipus de Permisos Bàsics (r, w, x)

<p class="md-kicker">SEGURETAT LÒGICA LINUX</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### Lectura (r / read)

Permet visualitzar el contingut d'un fitxer o llistar un directori.

</div>

<div class="md-card" style="--card:#EAB308" markdown="1">

### Escriptura (w / write)

Permet modificar el fitxer o crear i esborrar dins del directori.

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### Execució (x / execute)

Executa el fitxer com a programa o permet entrar al directori ().

cd

</div>

</div>

## Notació Simbòlica de 10 Caràcters

<p class="md-kicker">VISUALITZACIÓ AMB LS -L</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0F172A" markdown="1">

### - / d / l

**Caràcter 1: Tipus**

Fitxer (), directori () o enllaç ().

\-

d

l

</div>

<div class="md-card" style="--card:#EF4444" markdown="1">

### r w x

**Caràcters 2–4: Propietari**

Permisos de l'usuari propietari ().

u

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### r - x

**Caràcters 5–7: Grup**

Permisos del grup propietari ().

g

</div>

<div class="md-card" style="--card:#0284C7" markdown="1">

### r - x

**Caràcters 8–10: Altres**

Permisos de la resta d'usuaris ().

o

</div>

</div>

## Conversió de Notació Simbòlica a Octal

<p class="md-kicker">CÀLCUL AMB CHMOD</p>

<div class="md-card" markdown="1">



</div>

| Entitat | Propietari (Owner) | Grup (Group) | Altres (Other) |
|---|---|---|---|
| Notació Simbòlica | rwx | r-x | r-x |
| Suma Binària / Pesos | 4 + 2 + 1 | 4 + 0 + 1 | 4 + 0 + 1 |
| Valor Octal (chmod 755) | 7 (Control total) | 5 (Lectura i execució) | 5 (Lectura i execució) |

## ACL a Linux i Funció de la Màscara (Mask)

<p class="md-kicker">PERMISOS AVANÇATS</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### Sintaxi ACL (setfacl)

- / : Usuari específic

u

user

- / : Grup específic

g

group

- / : Resta d'usuaris

o

other

- / : Sostre màxim efectiu

m

mask

</div>

<div class="md-card" style="--card:#EAB308" markdown="1">

### Cas Pràctic de la Màscara

La màscara limita el sostre màxim de permisos sense esborrar les regles individuals dels usuaris.

Bloqueig ràpid: 
 Restauració:

setfacl -m m::--- carpeta

setfacl -m m::rwx carpeta

</div>

</div>

## Protecció de Dades mitjançant Criptografia

<p class="md-kicker">CONFIDENCIALITAT I INTEGRITAT</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### Dades en Repòs (Data at Rest)

- Protegeix discs, particions i còpies emmagatzemades.
- Eines: **BitLocker**, **LUKS**, **FileVault** i **VeraCrypt** (AES-256).

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### Dades en Trànsit (Data in Transit)

- Evita intercepcions sniffing i Man-in-the-Middle.
- Protocols: **SSH**, **TLS (HTTPS)** i **VPN** (WireGuard / IPsec).

</div>

</div>

## Resum d'Estudi - Eines Preventives

La prevenció integral combina contrasenyes robustes, bloqueig a l'arrencada, permisos i **ACL** a Linux, quotes de disc i **criptografia** en repòs i en trànsit.
