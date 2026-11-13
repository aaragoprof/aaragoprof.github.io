# Seguretat Física 3.0

<p class="md-kicker">GESTIÓ D'INCIDENTS I PROVES DIGITALS</p>

Anàlisi Forense Informàtica, Protecció de l'Escena, Adquisició d'Evidències i Cadena de Custòdia

## Amenaces Físiques vs Lògiques

<p class="md-kicker">TIPOLOGIA D'AMENACES</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#F59E0B" markdown="1">

### Amenaces Físiques

**Factors Ambientals, Estructurals i Mecànics**

- **Condicions ambientals:** Excessos de temperatura, humitat o pols que deterioren els components electrònics.
- **Subministrament:** Descàrregues electrostàtiques, picos de tensió o talls de corrent prolongats.
- **Desastres i accessos:** Incendis, inundacions, terratrèmols i intromissió física directament a les instal·lacions o servidors.

</div>

<div class="md-card" style="--card:#EF4444" markdown="1">

### Amenaces Lògiques

**Malware i Atacs Telemàtics**

- **Software maliciós:** Virus, troians, cucs, spyware, ransomware i fons de codi maliciós (exploits).
- **Intrusions telemàtiques:** Atacs de denegació de servei (DoS/DDoS), injeccions SQL, XSS i accessos no autoritzats per xarxa.
- **Alteració de dades:** Manipulació il·lícita o esborrament no autoritzat de registres interns.

</div>

</div>

## Les 6 Preguntes de l'Anàlisi Forense

<p class="md-kicker">INVESTIGACIÓ PERICIAL</p>

Metodologia científica aplicada als sistemes informàtics per a la identificació i preservació d'evidències:

<div class="md-cards" markdown="1">

<div class="md-card" markdown="1">

**Què s'ha comès?**

Identificació clara de l'incident: intrusió no autoritzada, fuga d'informació confidencial o danys al sistema.

</div>

<div class="md-card" markdown="1">

**Quan ha passat?**

Construcció de la cronologia i línia temporal dels fets basant-se en els logs de sistema i metadades.

</div>

<div class="md-card" markdown="1">

**On s'ha comès?**

Ubicació física o lògica: ordinadors locals, servidors remots, mòbils o plataformes Cloud (Dropbox, OneDrive).

</div>

</div>

<div class="md-cards" markdown="1">

<div class="md-card" markdown="1">

**Qui ho ha comès?**

Atribució de l'autor o compte d'usuari (intern o extern) responsable de les accions registrades.

</div>

<div class="md-card" markdown="1">

**Com s'ha dut a terme?**

Anàlisi dels vectors d'atac, eines emprades, vulnerabilitats explotades i la tècnica utilitzada.

</div>

<div class="md-card" markdown="1">

**Per què s'ha comès?**

Comprensió de la motivació (econòmica, sabotatge, espionatge industrial) o del context de l'atac.

</div>

</div>

## Assegurament i Protecció de l'Escena

<p class="md-kicker">PROTECCIÓ DE L'ESCENA</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### 1. Perímetre i Xarxa

Delimitar la zona de l'incident per evitar la manipulació d'equips. Desconnectar totes les interfícies de xarxa (cable ethernet, Wi-Fi i Bluetooth) per evitar alteracions o ordres d'esborrat remot.

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### 2. Documentació i Temps

Enregistrar en foto/vídeo l'estat inicial dels equips, cablejat i pantalles. Controlar el desfase temporal registrant la data/hora del sistema respecte a l'hora real abans de qualsevol acció. Etiquetar tots els components.

</div>

<div class="md-card" style="--card:#EF4444" markdown="1">

### 3. Gestió d'Equips

**Equips apagats:** Desconnectar el corrent posterior i extreure la bateria en portàtils per evitar l'autoencesa. 
 **Equips encesos:** Desendollar directament de la xarxa elèctrica exceptuant si cal abocar la memòria RAM en viu.

</div>

</div>

## Adquisició de Proves i Còpia Bit a Bit

<p class="md-kicker">TÈCNIQUES D'EXTRACCIÓ</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### Imatge Forense (Bit a Bit)

La investigació s'ha de realitzar **sempre sobre una còpia exacte (bit a bit)** del disc original, preservant la font primària intacta. S'hi inclouen espais no assignats, particions ocultes i fitxers de sistema.

**Eines i dispositius:** Bloquejadors d'escriptura per maquinari (Write Blockers) i eines com dd, FTK Imager o duplicadors físics.

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### Integritat i Preparació

- **Calcul de Hash d'Integritat:** Generació d'un valor resum (ex. SHA-256) tant a la font d'origen com a la còpia de destinació per certificar legalment que són 100% idèntiques.
- **Neteja de Suport (Wipe):** El disc on es desa la còpia ha de ser totalment verge o haver estat esborrat de manera segura (zeroitzat) abans de l'ús.

</div>

</div>

## Cadena de Custòdia i Informe Pericial

<p class="md-kicker">VALIDESA JUDICIAL</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### Cadena de Custòdia

Procés de documentació rigorós i ininterromput que registra la identitat de qualsevol persona que recull, custodia, transporta o analitza l'evidència digital, garantint que no ha estat alterada ni substituïda.

</div>

<div class="md-card" style="--card:#8B5CF6" markdown="1">

### Anàlisi i Eines

Inspecció de fitxers accessibles, recuperació d'arxius esborrats i examen de *Slack Space* (espai no utilitzat del clúster). Utilització d'eines com EnCase, FTK, Autopsy o Volatility (memòria RAM).

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### Informe i Defensa

Redacció de l'informe pericial en un llenguatge comprensible per a jutges, advocats o directius. Preparat per a la ratificació judicial i la defensa de la metodologia empleada durant el judici.

</div>

</div>

## Les 6 Preguntes de l'Anàlisi Forense

<p class="md-kicker">INVESTIGACIÓ PERICIAL</p>

<div class="md-cards" markdown="1">

<div class="md-card" markdown="1">

**Què s'ha comès?**

Tipificació del delicte o incident (intrusió, fuga de dades).

</div>

<div class="md-card" markdown="1">

**Quan ha passat?**

Establiment de la línia temporal exacta dels fets.

</div>

<div class="md-card" markdown="1">

**On s'ha comès?**

Localització: equips locals, servidors remots o serveis Cloud.

</div>

</div>

<div class="md-cards" markdown="1">

<div class="md-card" markdown="1">

**Qui ho ha comès?**

Atribució precisa de l'autor o compte d'usuari.

</div>

<div class="md-card" markdown="1">

**Com s'ha fet?**

Identificació dels vectors d'atac i exploits utilitzats.

</div>

<div class="md-card" markdown="1">

**Per què s'ha comès?**

Determinació de la motivació o context de l'atac.

</div>

</div>

## Assegurament de l'Evidència Digital

<p class="md-kicker">PROTECCIÓ DE L'ESCENA</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### Perímetre i Xarxa

Aïllar la zona i desconnectar immediatament totes les connexions de xarxa (Cable, Wi-Fi i Bluetooth).

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### Documentació Visual

Fotografiar i filmar l'estat dels equips, el cablejat, l'hora del sistema i realitzar l'etiquetat exhaustiu de dispositius.

</div>

<div class="md-card" style="--card:#EF4444" markdown="1">

### Equips Encesos vs Apagats

**Apagats:** Desconnectar corrent i treure bateria. **Encesos:** Desendollar de cop excepte si cal extreure la memòria RAM.

</div>

</div>

## Adquisició i Còpia Bit a Bit

<p class="md-kicker">TÈCNIQUES D'EXTRACCIÓ</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### Imatge Forense (Bit a Bit)

Treballar sempre sobre una duplicació exactíssima del suport original, incloent particions ocultes i espai no assignat.

**Eines:** Duplicadors per maquinari (Write Blockers) o software com dd o FTK Imager.

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### Integritat i Wipe

- **Verificació Hash:** Comparar el hash (ex: SHA-256) d'origen i destí per garantir que la còpia sigui 100% idèntica.
- **Neteja Segura (Wipe):** El disc de destinació ha de ser nou o haver estat esborrat de manera irrecuperable.

</div>

</div>

## Cadena de Custòdia i Informe Pericial

<p class="md-kicker">VALIDESA JUDICIAL</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### Cadena de Custòdia

Registre ininterromput que documenta qui té, trasllada i emmagatzema les evidències digitals en tot moment.

</div>

<div class="md-card" style="--card:#8B5CF6" markdown="1">

### Eines d'Anàlisi

Examen de dades accessibles, fitxers esborrats i *File Slack* emprant programari com EnCase, Autopsy o Volatility.

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### Informe i Ratificació

Redacció clara i accessible per a jutges i directius, preparada per a la defensa rigorosa en la seu judicial.

</div>

</div>

## Resum de Seguretat Física 3.0

L'anàlisi forense exigeix el rigor del mètode científic: aïllar l'escena, realitzar clonacions bit a bit amb verificació Hash i mantenir una **cadena de custòdia ininterrompuda** per a la seva ratificació judicial.
