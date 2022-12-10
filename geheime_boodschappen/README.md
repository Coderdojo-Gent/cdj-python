* Level: Beginner
* Onderwerpen: If-else, for-loops, strings

In dit project gaan we leren hoe we een codeerprogramma kunnen maken om boodschappen te versleutelen en nadien ook weer te ontcijferen. Zo kan je geheime berichten versturen naar je vrienden!

## Het Caesarcijfer

(meer info: [https://nl.wikipedia.org/wiki/Caesarcijfer](https://nl.wikipedia.org/wiki/Caesarcijfer))

Het Caesarcijfer is een klassieke substitutieversleuteling, waarbij elke letter vervangen wordt door een andere letter om zo de boodschap te versleutelen. Het is vernoemd naar Julius Caesar, de Romeinse keizer, die deze versleuteling al meer dan 2000 jaar geleden gebruikte om geheime boodschappen door te geven aan zijn veldheren!

Deze versleuteling techniek maakt gebruik van twee alfabetten. Het eerste alfabet wordt opgeschreven in de gewone volgorde die we kennen. Het tweede alfabet staat ook in de gewone volgorde, maar dan enkele posities verplaatst. Bijvoorbeeld bij drie posities verplaatst, dan beginnen we met de letter D en zo naar E, helemaal tot Z en dan achteraan komen de letters A, B en C. Het aantal posities dat we het tweede alfabet verplaatsen wordt de sleutel genoemd. Hier is de sleutel dus 3.

| A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z | A | B | C |

Elke letter uit de bovenste rij wordt bij de versleuteling dan vervangen door de letter die er onder staat. Om de boodschap dan te ontcijferen wordt elke letter uit de onderste rij vervangen door de letter die er boven staat.

**Vraag:** Als we een versleuteling met sleutel 3 gebruiken, wat is dan de geheime boodschap van het woord `CoderDojo`? (Antwoord: `FrghuGrmr`)

## Stap 1: Versleutel 1 letter

**Opdracht:** Schrijf een Python programma die 1 enkele letter kan versleutelen volgens de Caesarversleuteling met sleutel 3. 

**Hint:** Wat gebeurd er als je de letter “Y” gaat versleutelen? De nieuwe positie is 27, maar er zijn helemaal geen 27 letters in het alfabet! Hiervoor kan je het teken `%` gebruiken om aan te geven dat we terug naar positie 0 gaan als we positie 26 bereikt hebben, bijvoorbeeld: `27 % 26 = 1`, zodat `Y` versleuteld zal worden als `B`.

**Oplossing:** De oplossing kan je terug vinden in `stap1.py`.

## Stap 2: Meerdere sleutels

**Opdracht:** Pas je programma aan zodat men zelf de sleutel kan meegeven aan je programma, en sla deze dan op in een “sleutel” variabele. Vergeet niet om de functie `int()` te gebruiken om je input naar een getal om te zetten.

**Oplossing:** De oplossing kan je terug vinden in `stap2.py`.

## Stap 3: Boodschappen versleutelen

**Opdracht:** Nu kunnen we al een enkele letter versleutelen, maar graag willen we ook volledige boodschappen versleutelen. Pas je programma aan zodat men een volledige boodschap kan versleutelen. Probeer dan je programma uit met sleutel 3 om je versleuteling van `CoderDojo` te controleren.

**Hint:** Gebruik een for-loop om elke letter van je boodschap te versleutelen.

**Oplossing:** De oplossing kan je terug vinden in `stap3.py`.

## Stap 4: Extra karakters

**Vraag:** Probeer je programma dan nu eens uit met sleutel 3 voor een boodschap waar ook andere karakters buiten letters in zitten, bijvoorbeeld: `CoderDojo is super leuk!!`. Wat is het resultaat? (Antwoord:  De spaties en leestekens worden vervangen door de letter “c”. Als een character namelijk niet in het alfabet bevat is, dan zal de position gelijk zijn aan -1. Als we werken met versleuteling 3, dan is new_character gelijk aan 2, en dus de letter “c”.)

**Opdracht:** Pas je code aan zodat enkel letters die bevat zitten in het alfabet versleuteld worden volgens de versleuteling, en zodat de overige karakters als spaties en leestekens gewoon overgenomen worden.

**Oplossing:** De oplossing kan je terug vinden in `stap4.py`.

## Stap 5: Ontcijfer de boodschap

**Opdracht:** Hoe moet je de code aanpassen om een versleutelde boodschap terug te ontcijferen?

**Oplossing:** De oplossing kan je terug vinden in `stap5.py`.

Als je klaar bent kan je enkele boodschappen versleutelen voor je vrienden in CoderDojo. Kunnen zij de boodschap terug ontcijferen?