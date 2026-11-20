# Sistemes d'Alimentació Ininterrompuda (SAI)

<p class="md-kicker">MÒDUL DE SEGURETAT FÍSICA I MAQUINARI</p>

Material d'estudi desenvolupat: Protecció Elèctrica, Paràmetres Tècnics, Topologies Offline/Online i Càlculs d'Autonomia

## Concepte i Funció Principal del SAI / UPS

<p class="md-kicker">PROTECCIÓ DEL SUBMINISTRAMENT</p>

Un **SAI (Sistema d'Alimentació Ininterrompuda)** és un dispositiu que conté bateries internes i circuits electrònics que es connecta entre la xarxa elèctrica i els equips informàtics per garantir la continuïtat del servei.

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### Procés Ininterromput

Els processos en funcionament no s'aturen i els usuaris no pateixen desconnexions o interrupcions brusques durant el treball.

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### Protecció Física del HW

El maquinari sensible (fonts d'alimentació, plaques base, discs SSD/HDD) no pateix danys per sobretensions o talls d'energia ràpids.

</div>

<div class="md-card" style="--card:#8B5CF6" markdown="1">

### Protecció de Dades

Evita la pèrdua de dades a la memòria cau i prevé la corrupció de bases de dades i fitxers de sistema oberts.

</div>

</div>

## Problemes Elèctrics i Correcció del Senyal

<p class="md-kicker">QUALITAT DE L'ENERGIA</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#EF4444" markdown="1">

### Pertorbacions de la Xarxa

- **Soroll en la línia:** Paràsits electromagnètics o de radiofreqüència que distorsionen l'ona elèctrica.
- **Pujades i crestes de tensió:** Voltatges per sobre dels 230V nominals que poden cremar components.
- **Baixades de tensió (Brownouts):** Caigudes temporal de voltatge per sota dels 230V que provoquen reinicis inapropiats.
- **Interrupció elèctrica total (Blackout):** Absència completa de senyal elèctric.
- **Diferències de freqüència:** Variacions en els 50Hz esperats de la xarxa.

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### Funció d'Adaptació del SAI

El SAI actua com un filtres de protecció actiu:

- **Compensa** les caigudes elevant el voltatge.
- **Retalla** les crestes perilloses de tensió.
- **Atenua** el soroll elèctric de la línia.
- Protegeix línies addicionals com Ethernet (RJ45) i línia telefònica (RJ11).

</div>

</div>

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

## Topologies: SAI Offline vs SAI Online

<p class="md-kicker">ARQUITECTURA INTERNA</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#F59E0B" markdown="1">

### SAI Offline (Standby)

Alimenta els equips directament des de la xarxa elèctrica. Només si detecta una fallada, commuta a la bateria interna.

- **Temps de transferència:** Triga uns mil·lisisegons a commutar. Aquesta micro-alteració en el senyal pot ser crítica per a servidors molt sensibles.
- **Cost:** Més econòmic i eficient en repòs. Ideal per a PCs d'escritori.

</div>

<div class="md-card" style="--card:#0284C7" markdown="1">

### SAI Online (Doble Conversió)

Alimenta **sempre** els equips des de la seva bateria interna mentre la recarrega contínuament des de la xarxa.

- **Temps de transferència ZERO:** No pateix cap alteració en el senyal elèctric.
- **Cost i complexitat:** Disseny més complex, preu més elevat i major generació de calor. Obligatori per a CPDs i servidors crítics.

</div>

</div>

## Eficiència Energètica i Pèrdues per Calor

<p class="md-kicker">RENDIMENT ELÈCTRIC</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#8B5CF6" markdown="1">

### Conversió CC a CA i Disipació

En situació d'autonomia, el SAI ha de transformar el Corrent Continu (CC) de les bateries en Corrent Altern (CA) per als equips informàtics. En aquest procés, **una part de l'energia es perd necessàriament en forma de calor**.

Per tant, els càlculs d'autonomia han d'utilitzar l'**energia útil** real i no l'energia total emmagatzemada.

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### Exemple Pràctic d'Eficiència

Si disposem d'una bateria amb 100 Wh i el SAI té un factor d'eficiència del **90% (0.90)**:

<div class="md-callout" style="--card:#BAE6FD" markdown="1">

**100 Wh × 0.90 = 90 Wh útils**

</div>

\* Els 10 Wh restants es disipen en forma de calor durant la conversió. En la pràctica real cal consultar la fitxa tècnica del fabricant.

</div>

</div>

## Pas 1: Determinar els VA Requerits

<p class="md-kicker">CÀLCUL PRÀCTIC DE DIMENSIONAMENT</p>

Primer cal sumar el consum de tots els equips que es connectaran al SAI. Si l'etiqueta d'un equip no dona els VA directament, cal aplicar les conversions següents:

<div class="md-cards" markdown="1">

<div class="md-card" markdown="1">

### Si tenim Volts (V) i Amperes (A)

Multiplicar la tensió per la intensitat:

<div class="md-callout" style="--card:#BAE6FD" markdown="1">

**VA = Volts × Amperes**

</div>

Ex: 230 V × 1.5 A = **345 VA**

</div>

<div class="md-card" markdown="1">

### Si tenim Watts (W)

Dividir el valor en Watts pel factor de potència (aprox. 0.7):

<div class="md-callout" style="--card:#BAE6FD" markdown="1">

**VA = Watts / 0.7**

</div>

Ex: 80 W / 0.7 = **114.3 VA**

</div>

</div>

## Pas 2: Marge de Seguretat (75% Càrrega Màxima)

<p class="md-kicker">CÀLCUL PRÀCTIC DE DIMENSIONAMENT</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### Regla del 75% de Càrrega

A la pràctica, la demanda total de VA dels equips **mai no ha de superar el 75%** de la capacitat màxima de VA que pot subministrar el SAI triat.

Aquest marge garanteix que el SAI no treballi al límit de la seva capacitat, evita sobreescalfaments i deixa espai per a futures ampliacions.

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### Exemple de Selecció

Si la demanda total dels nostres equips és de **375 VA**:

<div class="md-callout" style="--card:#BAE6FD" markdown="1">

**SAI Mínim = 375 VA / 0.75 = 500 VA**

</div>

**✓ Cal triar un SAI de com a mínim 500 VA de capacitat nominal.**

</div>

</div>

## Pas 3: Quocient de Càrrega i Factor d'Autonomia

<p class="md-kicker">CÀLCUL D'AUTONOMIA AMPLIADA</p>

Quan la demanda de VA connectada és inferior a la màxima capacitat del SAI, el temps d'autonomia augmenta. Es calcula el **Quocient d'alimentació extra**:

<div class="md-callout" style="--card:#BAE6FD" markdown="1">

**Quocient = VA del SAI / VA de Consum dels Equips**

</div>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#EF4444" markdown="1">

**Quocient &lt; 1.3**

El SAI està treballant a prop del seu límit. No aporta un temps d'autonomia extra significatiu respecte al valor base de la fitxa tècnica.

</div>

<div class="md-card" style="--card:#F59E0B" markdown="1">

**1.3 ≤ Quocient &lt; 3.0**

**FACTOR = 1.3** 
 S'aplica un multiplicador d'autonomia del 30% extra sobre el temps base.

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

**Quocient ≥ 3.0**

**FACTOR = 1.5** 
 La càrrega és molt baixa. S'aplica un multiplicador d'autonomia del 50% extra sobre el temps base.

</div>

</div>

## Exemple Pràctic Resolut de Factor d'Autonomia

<p class="md-kicker">EXERCICI RESOLUT</p>

<div class="md-cards" markdown="1">

<div class="md-card" style="--card:#0284C7" markdown="1">

### Enunciat del Cas

Disposem d'un **SAI de 1.100 VA** de capacitat nominal i hi volem connectar un conjunt d'equips informàtics que sumen un consum total de **375 VA**.

**Quin factor de temps extra obtindrem en l'autonomia d'aquest equipament?**

</div>

<div class="md-card" style="--card:#16A34A" markdown="1">

### Resolució Pas a Pas

1\. Càlcul del quocient d'alimentació:

<div class="md-callout" style="--card:#BAE6FD" markdown="1">

**Quocient = 1.100 VA / 375 VA = 2.9333**

</div>

2\. Comprobació de l'escala de valors:

**Com que 1.3 ≤ 2.9333 &lt; 3.0, el resultat es troba en el primer tram d'ampliació.**

<div class="md-callout" style="--card:#22C55E" markdown="1">

**Resultat: FACTOR D'AUTONOMIA = 1.3**

</div>

</div>

</div>

## Resum d'Estudi - Sistemes SAI / UPS

Un SAI garanteix la fiabilitat elèctrica i la protecció de dades. Per a servidors crítics cal triar la tecnologia **Online**, aplicar la **regla del 75% de càrrega màxima** (marge de seguretat en VA) i considerar les pèrdues d'eficiència en el càlcul d'autonomia.
