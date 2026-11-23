# Anàlisi de Programari Maliciós

<p class="md-kicker">MÒDUL DE SEGURETAT ACTIVA</p>

Detecció d'amenaces, anàlisi en entorns aïllats, gestió d'accessos i criptografia aplicada

## Evolució i Propagació del Malware

<p class="md-kicker">CONTEXT DE L'AMENAÇA</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### 1972 – 2005

De Creeper al dany tècnic per guanyar notorietat.

</div>

<div class="md-card" style="--card:#EAB308" markdown="1">

### Des del 2005

Enfocament econòmic amb spyware, phishing i troians bancaris.

</div>

<div class="md-card" style="--card:#EF4444" markdown="1">

### Tendència Actual

Entrada per correu o USB i desplaçament cap a mòbils.

</div>

</div>

## Detecció del Codi Maliciós

<p class="md-kicker">SUPERVISIÓ D'INTEGRITAT</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#EF4444" markdown="1">

### Metadades (Limitada)

Dates i mides manipulables mitjançant tècniques de timestomping.

</div>

<div class="md-card" style="--card:#0284C7" markdown="1">

### Control Hash (FIM)

Empremtes SHA-256 immutables en eines com Wazuh o OSSEC.

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### Temps Real (EDR)

Antivirus NGAV i EDR bloquegen el comportament maliciós abans d'executar-se.

</div>

</div>

## Preparació d'un Entorn Aïllat (Sandbox)

<p class="md-kicker">LABORATORI SEGUR</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### Aïllament Total

Màquines virtuals separades o sandboxes com Cuckoo i ANY.RUN.

</div>

<div class="md-card" style="--card:#8B5CF6" markdown="1">

### Línia Base i Snapshots

Instantànies prèvies i registre de ports, processos i usuaris actius.

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### Eines d'Inspecció

Monitoratge amb Wireshark per xarxa i Process Monitor o Sysmon.

</div>

</div>

## Anàlisi Estàtica, Dinàmica i Extracció d'IoCs

<p class="md-kicker">METODOLOGIA TÈCNICA</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### Anàlisi Estàtica (En Repòs)

- Estudi sense executar el fitxer maliciós.
- Revisió de hashes, cadenes de text (strings) i capçaleres.

</div>

<div class="md-card" style="--card:#EAB308" markdown="1">

### Anàlisi Dinàmica i DFIR

- Observació en viu de connexions C2 i canvis al registre.
- Extracció d'IoCs (IPs, dominis) per bloquejar atacs reals.

</div>

</div>

## Gestió Segura de Contrasenyes

<p class="md-kicker">PREVENCIÓ A L'USUARI</p>

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

<p class="md-kicker">NIVELLS DE PROTECCIÓ FÍSICA</p>

<div class="md-card" markdown="1">



</div>

| Nivell d'Arrencada | Funció de Seguretat | Tecnologies Clau |
|---|---|---|
| 1. Firmware (UEFI / BIOS) | Impedeix iniciar des d'un Live USB extern | Secure Boot, xip TPM i xifratge de disc |
| 2. Gestor (GRUB 2) | Bloqueja l'edició del nucli i el mode root | Contrasenyes protegides amb hash PBKDF2 |
| 3. Sistema Operatiu | Inici de sessió (feble en comptes locals sense xifrar) | Vulnerable a chntpw sobre SAM sense BitLocker |

## Control d'Accés, Permisos i Quotes de Disc

<p class="md-kicker">GOVERNANÇA DEL SISTEMA</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### Permisos Linux / Unix

Control rwx per propietari (u), grup (g) i altres (o); hashes a /etc/shadow.

</div>

<div class="md-card" style="--card:#8B5CF6" markdown="1">

### Llistes ACL

Permisos granulars per usuaris específics amb setfacl o NTFS.

</div>

<div class="md-card" style="--card:#EAB308" markdown="1">

### Quotes de Disc

Límits amb FSRM o xfs\_quota per evitar denegacions de servei (DoS).

</div>

</div>

## Protecció de Dades mitjançant Criptografia

<p class="md-kicker">CONFIDENCIALITAT I INTEGRITAT</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### Dades en Repòs (At Rest)

- Protecció de discs, particions i còpies de seguretat.
- Eines: **BitLocker**, **LUKS**, **FileVault** i **VeraCrypt** (AES-256).

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### Dades en Trànsit (In Transit)

- Evita sniffing i atacs Man-in-the-Middle a la xarxa.
- Protocols: **SSH**, **TLS (HTTPS)** i túnels **VPN** (WireGuard / IPsec).

</div>

</div>

## Resum d'Estudi - Anàlisi de Malware i Hardening

La defensa en profunditat combina detecció **EDR/FIM**, anàlisi en **Sandbox**, protecció de l'arrencada, gestió d'accessos i **criptografia** en repòs i en trànsit.
