# Kubernetes

I E S  D a n i e l  B l a n x a r t
Kubernetes
0614 Desplegament d'aplicacions Web

Que es Kubernetes?
Kubernetes és una paraula grega que significa
“capità”.
Kubernetes (de vegades abreujat com a K8s) és un
sistema de codi obert per implementar, escalar i
administrar aplicacions allotjades en contenidors a
qualsevol lloc.
Kubernetes automatitza les tasques operatives de
l'administració de contenidors i inclou ordres
integrades per implementar aplicacions,
actualitzar-les, escalar-les perquè s'ajustin a les
teves necessitats, supervisar-les i molt més. 
Tot això facilita l’administració de les aplicacions.
0614 Desplegament d'aplicacions Web

0614 Desplegament d'aplicacions Web
Com funciona Kubernetes?
Per a Kubernetes, la unitat més petita no és el contenidor, sinó el Pod. Tu no
desplegues un contenidor de Docker directament; desplegues un Pod que
conté un (o diversos) contenidors.
En lloc de gestionar cada contenidor per separat, Kubernetes els col·loca dins
d'una "càpsula" o Pods

Compartir recursos "com si fossin un
sol equip"
0614 Desplegament d'aplicacions Web
Quan agrupes contenidors en un mateix Pod, aquests
comparteixen:
Adreça IP única: Tots els contenidors del Pod es veuen entre
ells a través de localhost.
Emmagatzematge (Volumes): Poden compartir fitxers de
manera local i instantània.
Cicle de vida: Si el Pod es mou d'un servidor a un altre, tots els
seus contenidors es mouen junts.

El model "Sidecar" (Per què posar-ne més d'un?)
0614 Desplegament d'aplicacions Web
La majoria de vegades, un Pod només té un contenidor. Però
s'agrupen quan n'hi ha un de principal i un d'ajudant (anomenat
Sidecar). Per exemple:
Contenidor A (Principal): L'aplicació web.
Contenidor B (Ajudant): Un programa que recull els logs
(registres) de l'aplicació i els envia a una base de dades.

El Cicle de Vida de Kubernetes en 3 Fases
0614 Desplegament d'aplicacions Web
1. Definició i Declaració (L'usuari actua)
Tot comença amb la intenció. Tu no instales coses
manualment, sinó que escrius les teves "instruccions":
Fitxers YAML: Defineixes l'estat desitjat (quants contenidors
vols, quanta CPU necessiten i com es connecten).
kubectl: Envies aquestes instruccions al "cervell" de
Kubernetes (l'API).

El Cicle de Vida de Kubernetes en 3 Fases
0614 Desplegament d'aplicacions Web
2. Orquestració i Desplegament (El sistema actua)
Un cop el sistema rep la teva ordre, les peces internes es posen en marxa:
Scheduler (El programador): Decideix en quina màquina (node) física o
virtual encaixa millor cada Pod segons els recursos lliures.
kubelet: És l'agent que viu a cada màquina. Rep l'ordre i s'encarrega
d'encendre els contenidors realment.
Services: Creen una "porta d'entrada" única (IP o DNS) perquè l'usuari
pugui arribar a l'aplicació, sense importar si els contenidors canvien de
lloc.

El Cicle de Vida de Kubernetes en 3 Fases
0614 Desplegament d'aplicacions Web
3. Manteniment i Evolució (El sistema supervisa)
Kubernetes no només engega l'app, sinó que la cuida:
Controladors: Comparen l'estat real amb el desitjat. Si alguna
cosa es trenca, la reparen sola (autorecuperació).
Escalat i Actualitzacions: Permet augmentar el nombre de
còpies o actualitzar el programari a una versió nova sense
aturar mai el servei (zero downtime).

Quins són els beneficis de Kubernetes?
0614 Desplegament d'aplicacions Web
 Operacions automatitzades: actua com un pilot automàtic que gestiona i
corregeix les operacions diàries de les teves aplicacions per garantir que
funcionin sempre tal com les vas configurar.
Abstracció de la infraestructura: gestiona tota la infraestructura
(processament, xarxa i emmagatzematge) perquè els desenvolupadors es
puguin centrar exclusivament a crear codi sense preocupar-se de les
màquines.
Supervisió de l'estat dels serveis: garanteix la màxima disponibilitat
supervisant constantment la salut dels contenidors, reiniciant-los si fallen i
bloquejant l'accés als usuaris fins que confirma que el servei funciona
correctament.

Quins són els beneficis de Kubernetes?
0614 Desplegament d'aplicacions Web
Ús de recursos optimitzat:  maximitza l'estalvi i l'eficiència assignant de
manera intel·ligent els contenidors a les màquines, aprofitant al màxim cada
recurs disponible i reduint costos innecessaris.
Administració simplificada d'aplicacions: estandarditza la gestió
d'aplicacions oferint un mètode únic i coherent per desplegar, actualitzar i
administrar qualsevol programari, sense importar la seva complexitat.
Portabilitat millorada: garanteix la total flexibilitat i portabilitat de les
empreses en oferir una plataforma de codi obert que funciona de la mateixa
manera en servidors propis que en qualsevol proveïdor de l'esfera pública
(núvol).

Kubernetes en comparació amb Docker
0614 Desplegament d'aplicacions Web
Kubernetes i Docker són tecnologies molt diferents pero són
complementàries per executar aplicacions en contenidors. 
Docker et permet col·locar tot el necessari per executar la teva aplicació en
una caixa que es pot emmagatzemar i obrir quan i on sigui necessari.
Kubernetes administra aquestes caixes i és responsable de traslladar i lliurar
les caixes de forma segura a les ubicacions on es puguin utilitzar.

Kubernetes en comparació amb Docker
0614 Desplegament d'aplicacions Web
Kubernetes es pot utilitzar amb Docker o sense
Docker no és una alternativa a Kubernetes, per la qual cosa no és una qüestió
de triar entre "Kubernetes o Docker". Es tracta de fer servir Kubernetes i
Docker per col·locar les aplicacions en contenidors i executar-les a gran escala
La diferència entre Docker i Kubernetes rau en el rol que cadascú compleix en
la creació de contenidors i l'execució de les aplicacions
Docker és un estàndard de la indústria per empaquetar i distribuir aplicacions
en contenidors
Kubernetes utilitza Docker per implementar, administrar i escalar aplicacions
en contenidors