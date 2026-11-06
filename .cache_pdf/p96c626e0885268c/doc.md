# Seguretat Física 3.0 - Material d'Estudi Ampliat

## Diapositiva 1

![Imatge 1](@@IMG@@/img-001.jpg){ loading=lazy }

![Imatge 2](@@IMG@@/img-002.png){ loading=lazy }

**GESTIÓ D'INCIDENTS I PROVES DIGITALS**

**Seguretat Física 3.0**

Anàlisi Forense Informàtica, Protecció de l'Escena, Adquisició d'Evidències i Cadena de Custòdia

## Diapositiva 2

**TIPOLOGIA D'AMENACES**

**Amenaces Físiques vs Lògiques**

**Factors Ambientals, Estructurals i Mecànics**

**Amenaces Físiques**

**Malware i Atacs Telemàtics**

**Amenaces Lògiques**

• **Condicions ambientals:** Excessos de temperatura, humitat o pols que deterioren els components electrònics.

• **Software maliciós:** Virus, troians, cucs, spyware, ransomware i fons de codi maliciós (exploits).

• **Subministrament:** Descàrregues electrostàtiques, picos de tensió o talls de corrent prolongats.

• **Intrusions telemàtiques:** Atacs de denegació de servei (DoS/DDoS), injeccions SQL, XSS i accessos no autoritzats per xarxa.

• **Desastres i accessos:** Incendis, inundacions, terratrèmols i intromissió física directament a les instal·lacions o servidors.

• **Alteració de dades:** Manipulació il·lícita o esborrament no autoritzat de registres interns.

## Diapositiva 3

**INVESTIGACIÓ PERICIAL**

**Les 6 Preguntes de l'Anàlisi Forense**

Metodologia científica aplicada als sistemes informàtics per a la identificació i preservació d'evidències:

**Què s'ha comès?**

**Quan ha passat?**

**On s'ha comès?**

Identificació clara de l'incident: intrusió no autoritzada, fuga d'informació confidencial o danys al sistema.

Construcció de la cronologia i línia temporal dels fets basant-se en els logs de sistema i metadades.

Ubicació física o lògica: ordinadors locals, servidors remots, mòbils o plataformes Cloud (Dropbox, OneDrive).

**Qui ho ha comès?**

**Com s'ha dut a terme?**

**Per què s'ha comès?**

Atribució de l'autor o compte d'usuari (intern o extern) responsable de les accions registrades.

Anàlisi dels vectors d'atac, eines emprades, vulnerabilitats explotades i la tècnica utilitzada.

Comprensió de la motivació (econòmica, sabotatge, espionatge industrial) o del context de l'atac.

## Diapositiva 4

**PROTECCIÓ DE L'ESCENA**

**Assegurament i Protecció de l'Escena**

**1. Perímetre i Xarxa**

**2. Documentació i Temps**

**3. Gestió d'Equips**

Delimitar la zona de l'incident per evitar la manipulació d'equips. Desconnectar totes les interfícies de xarxa (cable ethernet, Wi-Fi i Bluetooth) per evitar alteracions o ordres d'esborrat remot.

Enregistrar en foto/vídeo l'estat inicial dels equips, cablejat i pantalles. Controlar el desfase temporal registrant la data/hora del sistema respecte a l'hora real abans de qualsevol acció. Etiquetar tots els components.

**Equips apagats:** Desconnectar el corrent posterior i extreure la bateria en portàtils per evitar l'autoencesa. 
 **Equips encesos:** Desendollar directament de la xarxa elèctrica exceptuant si cal abocar la memòria RAM en viu.

## Diapositiva 5

**TÈCNIQUES D'EXTRACCIÓ**

**Adquisició de Proves i Còpia Bit a Bit**

**Imatge Forense (Bit a Bit)**

**Integritat i Preparació**

La investigació s'ha de realitzar **sempre sobre una còpia exacte (bit a bit)** del disc original, preservant la font primària intacta. S'hi inclouen espais no assignats, particions ocultes i fitxers de sistema.

• **Calcul de Hash d'Integritat:** Generació d'un valor resum (ex. SHA-256) tant a la font d'origen com a la còpia de destinació per certificar legalment que són 100% idèntiques.

**Eines i dispositius:** Bloquejadors d'escriptura per maquinari (Write Blockers) i eines com dd, FTK Imager o duplicadors físics.

• **Neteja de Suport (Wipe):** El disc on es desa la còpia ha de ser totalment verge o haver estat esborrat de manera segura (zeroitzat) abans de l'ús.

## Diapositiva 6

**VALIDESA JUDICIAL**

**Cadena de Custòdia i Informe Pericial**

**Cadena de Custòdia**

**Anàlisi i Eines**

**Informe i Defensa**

Procés de documentació rigorós i ininterromput que registra la identitat de qualsevol persona que recull, custodia, transporta o analitza l'evidència digital, garantint que no ha estat alterada ni substituïda.

Inspecció de fitxers accessibles, recuperació d'arxius esborrats i examen de *Slack Space* (espai no utilitzat del clúster). Utilització d'eines com EnCase, FTK, Autopsy o Volatility (memòria RAM).

Redacció de l'informe pericial en un llenguatge comprensible per a jutges, advocats o directius. Preparat per a la ratificació judicial i la defensa de la metodologia empleada durant el judici.

## Diapositiva 7

**INVESTIGACIÓ PERICIAL**

**Les 6 Preguntes de l'Anàlisi Forense**

**Què s'ha comès?**

**Quan ha passat?**

**On s'ha comès?**

Tipificació del delicte o incident (intrusió, fuga de dades).

Establiment de la línia temporal exacta dels fets.

Localització: equips locals, servidors remots o serveis Cloud.

**Qui ho ha comès?**

Atribució precisa de l'autor o compte d'usuari.

**Com s'ha fet?**

Identificació dels vectors d'atac i exploits utilitzats.

**Per què s'ha comès?**

Determinació de la motivació o context de l'atac.

## Diapositiva 8

**PROTECCIÓ DE L'ESCENA**

**Assegurament de l'Evidència Digital**

**Perímetre i Xarxa**

**Documentació Visual**

**Equips Encesos vs Apagats**

Aïllar la zona i desconnectar immediatament totes les connexions de xarxa (Cable, Wi-Fi i Bluetooth).

Fotografiar i filmar l'estat dels equips, el cablejat, l'hora del sistema i realitzar l'etiquetat exhaustiu de dispositius.

**Apagats:** Desconnectar corrent i treure bateria. **Encesos:** Desendollar de cop excepte si cal extreure la memòria RAM.

## Diapositiva 9

**TÈCNIQUES D'EXTRACCIÓ**

**Adquisició i Còpia Bit a Bit**

**Imatge Forense (Bit a Bit)**

**Integritat i Wipe**

Treballar sempre sobre una duplicació exactíssima del suport original, incloent particions ocultes i espai no assignat.

• **Verificació Hash:** Comparar el hash (ex: SHA-256) d'origen i destí per garantir que la còpia sigui 100% idèntica.

**Eines:** Duplicadors per maquinari (Write Blockers) o software com dd o FTK Imager.

• **Neteja Segura (Wipe):** El disc de destinació ha de ser nou o haver estat esborrat de manera irrecuperable.

## Diapositiva 10

**VALIDESA JUDICIAL**

**Cadena de Custòdia i Informe Pericial**

**Cadena de Custòdia**

**Eines d'Anàlisi**

**Informe i Ratificació**

Registre ininterromput que documenta qui té, trasllada i emmagatzema les evidències digitals en tot moment.

Examen de dades accessibles, fitxers esborrats i *File Slack* emprant programari com EnCase, Autopsy o Volatility.

Redacció clara i accessible per a jutges i directius, preparada per a la defensa rigorosa en la seu judicial.

## Diapositiva 11

![Imatge 3](@@IMG@@/img-003.jpg){ loading=lazy }

![Imatge 4](@@IMG@@/img-004.png){ loading=lazy }

**Resum de Seguretat Física 3.0**

L'anàlisi forense exigeix el rigor del mètode científic: aïllar l'escena, realitzar clonacions bit a bit amb verificació Hash i mantenir una **cadena de custòdia ininterrompuda** per a la seva ratificació judicial.
