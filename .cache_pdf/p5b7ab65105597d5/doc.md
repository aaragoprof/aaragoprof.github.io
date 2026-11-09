# SAI

## Diapositiva 1

![Imatge 1](@@IMG@@/img-001.jpg){ loading=lazy }

**MÒDUL DE SEGURETAT FÍSICA I MAQUINARI**

**Sistemes d'Alimentació Ininterrompuda (SAI)**

Material d'estudi desenvolupat: Protecció Elèctrica, Paràmetres Tècnics, Topologies Offline/Online i Càlculs d'Autonomia

## Diapositiva 2

**PROTECCIÓ DEL SUBMINISTRAMENT**

**Concepte i Funció Principal del SAI / UPS**

Un **SAI (Sistema d'Alimentació Ininterrompuda)** és un dispositiu que conté bateries internes i circuits electrònics que es connecta entre la xarxa elèctrica i els equips informàtics per garantir la continuïtat del servei.

Els processos en funcionament no s'aturen i els usuaris no pateixen desconnexions o interrupcions brusques durant el treball.

**Procés Ininterromput**

El maquinari sensible (fonts d'alimentació, plaques base, discs SSD/HDD) no pateix danys per sobretensions o talls d'energia ràpids.

**Protecció Física del HW**

Evita la pèrdua de dades a la memòria cau i prevé la corrupció de bases de dades i fitxers de sistema oberts.

**Protecció de Dades**

## Diapositiva 3

**QUALITAT DE L'ENERGIA**

**Problemes Elèctrics i Correcció del Senyal**

**Pertorbacions de la Xarxa**

**Funció d'Adaptació del SAI**

• **Soroll en la línia:** Paràsits electromagnètics o de radiofreqüència que distorsionen l'ona elèctrica.

El SAI actua com un filtres de protecció actiu:

• **Compensa** les caigudes elevant el voltatge.

• **Pujades i crestes de tensió:** Voltatges per sobre dels 230V nominals que poden cremar components.

• **Retalla** les crestes perilloses de tensió.

• **Baixades de tensió (Brownouts):** Caigudes temporal de voltatge per sota dels 230V que provoquen reinicis inapropiats.

• **Atenua** el soroll elèctric de la línia.

• Protegeix línies addicionals com Ethernet (RJ45) i línia telefònica (RJ11).

• **Interrupció elèctrica total (Blackout):** Absència completa de senyal elèctric.

• **Diferències de freqüència:** Variacions en els 50Hz esperats de la xarxa.

## Diapositiva 4

**CONCEPTES DE MAGNITUD**

**Unitats de Mesura i Paràmetres del SAI**

| Concepte | Unitat / Magnitud | Descripció Tècnica i Funció |
|---|---|---|
| Potència Real | W (Watts) | Potència activa realment consumida pels equips informàtics connectats. |
| Potència Aparent | VA (Voltampers) | Capacitat nominal màxima de treball del SAI. És el valor de referència per dimensionar la càrrega. |
| Tensió de Bateria | V (Volts) | Tensió de treball interna del banc de bateries del SAI. |
| Capacitat Bateria | Ah (Ampers-hora) | Indica la quantitat de càrrega elèctrica que pot emmagatzemar la bateria. |
| Càrrega i Autonomia | Equips i Temps | Càrrega: Suma del consum dels equips connectats. Autonomia: Temps que el SAI manté l'alimentació sense xarxa. |

## Diapositiva 5

**ARQUITECTURA INTERNA**

**Topologies: SAI Offline vs SAI Online**

Alimenta els equips directament des de la xarxa elèctrica. Només si detecta una fallada, commuta a la bateria interna.

**SAI Offline (Standby)**

Alimenta **sempre** els equips des de la seva bateria interna mentre la recarrega contínuament des de la xarxa.

**SAI Online (Doble Conversió)**

• **Temps de transferència:** Triga uns mil·lisisegons a commutar. Aquesta micro-alteració en el senyal pot ser crítica per a servidors molt sensibles.

• **Temps de transferència ZERO:** No pateix cap alteració en el senyal elèctric.

• **Cost:** Més econòmic i eficient en repòs. Ideal per a PCs d'escritori.

• **Cost i complexitat:** Disseny més complex, preu més elevat i major generació de calor. Obligatori per a CPDs i servidors crítics.

## Diapositiva 6

**RENDIMENT ELÈCTRIC**

**Eficiència Energètica i Pèrdues per Calor**

**Conversió CC a CA i Disipació**

**Exemple Pràctic d'Eficiència**

En situació d'autonomia, el SAI ha de transformar el Corrent Continu (CC) de les bateries en Corrent Altern (CA) per als equips informàtics. En aquest procés, **una part de l'energia es perd necessàriament en forma de calor**.

Si disposem d'una bateria amb 100 Wh i el SAI té un factor d'eficiència del **90% (0.90)**:

Per tant, els càlculs d'autonomia han d'utilitzar l'**energia útil** real i no l'energia total emmagatzemada.

**100 Wh × 0.90 = 90 Wh útils**

\* Els 10 Wh restants es disipen en forma de calor durant la conversió. En la pràctica real cal consultar la fitxa tècnica del fabricant.

## Diapositiva 7

**CÀLCUL PRÀCTIC DE DIMENSIONAMENT**

**Pas 1: Determinar els VA Requerits**

Primer cal sumar el consum de tots els equips que es connectaran al SAI. Si l'etiqueta d'un equip no dona els VA directament, cal aplicar les conversions següents:

Multiplicar la tensió per la intensitat:

**Si tenim Volts (V) i Amperes (A)**

Dividir el valor en Watts pel factor de potència (aprox. 0.7):

**Si tenim Watts (W)**

**VA = Volts × Amperes**

**VA = Watts / 0.7**

Ex: 230 V × 1.5 A = **345 VA**

Ex: 80 W / 0.7 = **114.3 VA**

## Diapositiva 8

**CÀLCUL PRÀCTIC DE DIMENSIONAMENT**

**Pas 2: Marge de Seguretat (75% Càrrega Màxima)**

**Regla del 75% de Càrrega**

**Exemple de Selecció**

A la pràctica, la demanda total de VA dels equips **mai no ha de superar el 75%** de la capacitat màxima de VA que pot subministrar el SAI triat.

Si la demanda total dels nostres equips és de **375 VA**:

Aquest marge garanteix que el SAI no treballi al límit de la seva capacitat, evita sobreescalfaments i deixa espai per a futures ampliacions.

**SAI Mínim = 375 VA / 0.75 = 500 VA**

**✓ Cal triar un SAI de com a mínim 500 VA de capacitat nominal.**

## Diapositiva 9

**CÀLCUL D'AUTONOMIA AMPLIADA**

**Pas 3: Quocient de Càrrega i Factor d'Autonomia**

Quan la demanda de VA connectada és inferior a la màxima capacitat del SAI, el temps d'autonomia augmenta. Es calcula el **Quocient d'alimentació extra**:

**Quocient = VA del SAI / VA de Consum dels Equips**

**Quocient &lt; 1.3**

**1.3 ≤ Quocient &lt; 3.0**

**Quocient ≥ 3.0**

El SAI està treballant a prop del seu límit. No aporta un temps d'autonomia extra significatiu respecte al valor base de la fitxa tècnica.

**FACTOR = 1.3** 
 S'aplica un multiplicador d'autonomia del 30% extra sobre el temps base.

**FACTOR = 1.5** 
 La càrrega és molt baixa. S'aplica un multiplicador d'autonomia del 50% extra sobre el temps base.

## Diapositiva 10

**EXERCICI RESOLUT**

**Exemple Pràctic Resolut de Factor d'Autonomia**

**Enunciat del Cas**

**Resolució Pas a Pas**

Disposem d'un **SAI de 1.100 VA** de capacitat nominal i hi volem connectar un conjunt d'equips informàtics que sumen un consum total de **375 VA**.

1\. Càlcul del quocient d'alimentació:

**Quin factor de temps extra obtindrem en l'autonomia d'aquest equipament?**

**Quocient = 1.100 VA / 375 VA = 2.9333**

2\. Comprobació de l'escala de valors:

**Com que 1.3 ≤ 2.9333 &lt; 3.0, el resultat es troba en el primer tram d'ampliació.**

**Resultat: FACTOR D'AUTONOMIA = 1.3**

## Diapositiva 11

![Imatge 2](@@IMG@@/img-002.jpg){ loading=lazy }

![Imatge 3](@@IMG@@/img-003.png){ loading=lazy }

**Resum d'Estudi - Sistemes SAI / UPS**

Un SAI garanteix la fiabilitat elèctrica i la protecció de dades. Per a servidors crítics cal triar la tecnologia **Online**, aplicar la **regla del 75% de càrrega màxima** (marge de seguretat en VA) i considerar les pèrdues d'eficiència en el càlcul d'autonomia.
