---
description: Què és un SAI, problemes elèctrics, característiques, SAI offline i online, i com calcular la potència i l'autonomia necessàries.
# Enllaç de Google Drive per descarregar el PDF complet (si el deixes buit, el botó no es mostra):
pdf: ""
---

# SAI (Sistemes d'Alimentació Ininterrompuda)

## Com garantim l'electricitat?

Hi ha tres maneres de garantir el subministrament elèctric:

- **Generadors**
- **SAI**
- **Línies extres**

## Què és i per a què serveix un SAI

Un **SAI** (Sistema d'alimentació ininterrompuda) és un dispositiu amb maquinari i programari propis que, connectat entre el nostre sistema i la xarxa elèctrica, ens evitarà alguns problemes quan l'alimentació falli:

- Els processos en funcionament no s'aturaran.
- Els usuaris del nostre sistema no veuran interrompudes les seves tasques.
- El maquinari no patirà.
- No es perdran dades a causa d'una aturada inesperada del sistema.

## Problemes elèctrics

Un SAI ens protegeix dels problemes elèctrics més habituals a la xarxa:

- **Soroll en la línia.**
- **Pujades de tensió i crestes de tensió:** el voltatge de la línia és més alt del que hauria de ser (més de 230 V).
- **Baixades de tensió:** el voltatge de la línia és inferior al que hauria de ser (menys de 230 V).
- **Interrupció elèctrica total:** no hi ha senyal elèctric (tall de corrent).
- **Diferències de freqüència:** les freqüències del senyal són diferents dels 50 Hz esperats.

## Característiques bàsiques

Davant aquests problemes, el SAI adapta el senyal elèctric que rep al que espera el nostre equip. Concretament:

- Compensa les baixades de tensió.
- Retalla les crestes.
- Atenua el soroll.
- Manté durant un cert temps el subministrament elèctric en cas d'un tall del senyal.

Els models de SAI més nous porten protecció de filtratge de soroll i supressió de crestes per a Ethernet i línia telefònica.

### Magnituds d'un SAI

| Concepte | Què és | Què cal mirar |
|---|---|---|
| **W** (watts) | Potència real que consumeixen els equips. | El SAI ha de tenir més W que la suma dels equips. |
| **VA** (voltampers) | Capacitat aparent del SAI. | El SAI ha de tenir més VA que els necessaris. |
| **V** (volts) | Tensió de la bateria. | Exemple habitual: 12 V. |
| **Ah** (ampers hora) | Capacitat de la bateria. | Com més Ah, més energia pot guardar. |
| **Wh** (watt-hora) | Energia emmagatzemada a la bateria. | Wh = V × Ah. Serveix per estimar l'autonomia. |

!!! tip "Què fer servir en cada cas"
    Per triar la potència del SAI: **W i VA**. Per calcular l'autonomia: **V, Ah, Wh i eficiència**.

### Càrrega, autonomia i capacitat

Aquests conceptes relacionen quins equips podem connectar i quant de temps aguantaran:

- **Càrrega:** conjunt d'equips connectats al SAI. És la suma del consum dels equips.
- **Autonomia:** temps que el SAI pot mantenir els equips funcionant amb bateria.
- **Capacitat:** potència màxima que el SAI pot subministrar a la càrrega. Pot aparèixer com *330 W / 700 VA*.
- **Nombre de bateries:** més bateries o més capacitat acostumen a donar més energia disponible.
- **Eficiència:** una part de l'energia es perd en calor. Als exercicis pot ser del 90–95 %.
- **Marge de seguretat:** reserva extra de potència. Als exercicis utilitzarem sovint el 25 %.

!!! warning "Important"
    Un SAI no deixa de ser una bateria, i es degrada amb el temps.

## Tipus de SAI

### SAI offline

Alimenta l'equipament connectat fent-li arribar directament el senyal de la xarxa elèctrica. Si detecta un problema (en menys de 5 mil·lisegons), passa a alimentar l'equipament amb el senyal elèctric que ell mateix produeix.

Això produeix una **alteració en el senyal**, i les alteracions als senyals poden provocar danys en els circuits; per tant, és important minimitzar-les. Aquest és el desavantatge més gran d'aquest tipus de SAI.

Com més petit sigui aquest temps (**temps de transferència**), de més qualitat (i més car) és el SAI.

### SAI online

Alimenta l'equipament connectat amb el senyal elèctric generat per la seva bateria interna i, mentrestant, la recarrega contínuament.

Com que el seu disseny és més complex, són **més cars**. I, per donar permanentment senyal des de la bateria, aquests dispositius han de consumir més energia i generen més calor.

## Eficiència: una part es perd en calor

Els càlculs d'autonomia utilitzen **energia útil**, no només energia teòrica.

**Què passa?** El SAI transforma el corrent continu (CC) de la bateria en corrent altern (CA) per als equips. En aquesta conversió es perd una part de l'energia en forma de calor.

**Exemple:** 100 Wh × 0,90 = **90 Wh útils** (els 10 Wh restants es dissipen en calor).

!!! note
    El 0,90 és un exemple. En un cas real cal consultar la fitxa tècnica o l'autonomia publicada pel fabricant.

## Paràmetres d'un SAI

- Cada SAI té un valor **VA** (volt-ampers) que indica el màxim nombre de volts × ampers que pot subministrar.
- La demanda de VA **no pot ser major** que la que pot donar el SAI. A la pràctica, no pot ser major del **75 %** del valor del SAI.
- També té un valor de **temps d'alimentació autònoma**, que es pot ampliar si la demanda de VA és inferior a la màxima.

## Com calcular el SAI necessari

1. **Obtenir els VA de cada equip** que hem de connectar.
   *Exemple:* 230 V a 1,5 A → 230 × 1,5 = **345 VA**.
2. **Si només tenim els watts**, cal dividir aquest valor per 0,7.
   *Exemple:* 80 W → 80 / 0,7 = **114,3 VA**.
3. **Sumar** tots els VA dels dispositius a connectar.
4. **Triar un SAI** que doni un valor de VA superior als que requereix l'equipament, amb un marge de seguretat: els VA requerits no han de suposar més del **75 %** del que pot oferir el SAI.
   *Exemple:* si l'equipament requereix 250 VA, caldria un SAI d'almenys 250 / 0,75 = **333 VA**. D'aquesta manera, 250 és el 75 % del que pot arribar a donar el SAI.

## Càlcul del temps extra

1. Dividim el valor VA del SAI entre el valor VA de consum total dels dispositius connectats.
   *Exemple:* dispositius de 375 VA i SAI d'1.100 VA → 1.100 / 375 = **2,9333**.
2. Segons el quocient obtingut:
    - Si el quocient és **inferior a 1,3**, el SAI no està prou sobredimensionat per donar temps extra.
    - Si **1,3 ≤ quocient < 3**, el factor és **1,3**.
    - Si **quocient ≥ 3**, el factor és **1,5**.

    Amb l'exemple, el factor és 1,3.
3. El temps de funcionament autònom ampliat és:

    **temps ampliat = temps nominal × quocient × factor**

    *Exemple:* si el SAI té un temps nominal de 10 minuts → 10 × 2,9333 × 1,3 = **38,13 minuts**.
