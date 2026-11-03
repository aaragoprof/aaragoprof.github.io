# Virtual Hosts en Apache

I E S  D a n i e l  B l a n x a r t
Virtual Hosts en
Apache
Administració de servidors web
0614 Desplegament d'aplicacions Web

Apache
Apache és un servidor web de codi obert, el més popular que
trobem en el món del web. Com tot servidor web, gestiona
sol·licituds HTTP. És a dir, està atent a les demandes dels usuaris
que volen consultar una URL i els envia el contingut sol·licitat
com a resposta.
Segons les dades mes recents Apache es fa servir aprox en el 25%
dels servidors a nivell mundial i en el 20% dels servidors Top 1 000
000
0614 Desplegament d'aplicacions Web

Virtual Host
El "virtual host" és l’eina que Apache posa a la nostra disposició
per poder publicar més d’una pàgina web en un mateix servidor
Apache, i que, a més, ens permet mantenir configuracions
diferents per a cada host virtual.
 Quan es realitza una petició al servidor web, Apache pot
identificar a quin lloc (host virtual) volem accedir en funció de
tres variables relacionades amb la sol·licitud feta al servidor:
La IP
El nom del host (Host Name)
El port
0614 Desplegament d'aplicacions Web

0614 Desplegament d'aplicacions Web
Configuracio
Tota la configuració d'Apache 2 es troba sota la carpeta
/var/apache2 . Els fitxers de configuració per als virtual hosts
es troben dins de dues carpetes en particular:
1./var/apache2/sites-available: En aquesta carpeta es
troben tots els fitxers de configuració dels hosts virtuals,
cada host es correspon amb un fitxer.
2./var/apache2/sites-enabled: En aquesta carpeta es
crearan enllaços simbòlics als fitxers de la carpeta sites-
available per als hosts que vulguem activar en cada
moment.