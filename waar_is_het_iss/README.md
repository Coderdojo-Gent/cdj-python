# Waar is het ISS?

* **Level**: 2 - Gevorderd 
* **Onderwerpen**: Webservices, Dictionaries, Turtle

Weet jij waar het International Space Station (ISS) zich momenteel bevindt? Met dit project gaan we gebruik maken van een webservice om de huidige locatie van het ISS op te zoeken en op een kaart te tonen. Een webservice is te vergelijken met een website: een webservice heeft ook een adres (URL), maar in plaats van een mooie interface toont een webservice enkel data. Deze data kunnen we in Python inlezen om verder te gebruiken en visualiseren. 

## Wie is er in de ruimte?
Via onderstaande url kun je de webservice met informatie over de astronauten die zich momenteel in de ruimte bevinden, terug vinden. Open deze eens in je webbrower om te zien welke gegevens over de astronauten we allemaal kunnen gebruiken.

http://api.open-notify.org/astros.json

Als eerste stap gaan we de data van de webservice inlezen in Python. Hiervoor gaan we gebruik maken van twee modules: `urllib.request` en `json`. De eerste module zullen we gebruiken om de data van het internet in te lezen en json is het dataformaat van de data in de webservice. Deze modules moet je in het begin van je project importeren om verder in je code te kunnen gebruiken.

Gebruik onderstaande code om de data van de webservice in te laden in python. Eerst gaan we de url opslaan in een variabele. De tweede lijn code zal dan url openen en de data downloaden in een variabele `file_astronauten`. Deze file of bestand is van het type JSON, dewelke we dan in de laatste lijn code zullen inlezen in een Python datastructuur `dict_astronauten`.
```
# Laad de JSON file met alle informatie over de astronauten van de webservice
url_astronatuen = 'http://api.open-notify.org/astros.json'
file_astronauten = urllib.request.urlopen(url_astronatuen)
dict_astronauten = json.loads(file_astronauten.read())
print(dict_astronauten)
```
Het resultaat is een Python woordenboek (Engels: dictionary). Een dictionary staat altijd tussen accolades {}, en bestaat uit sleutels (Engels: keys) en waarden (Engels: values). Je ziet in de dictionary dat elke sleutel verbonden is met een waarde via een dubbelpunt: `dict = {sleutel1: waarde1, sleutel2: waarde2}`. Om een bepaalde waarde op te vragen uit de dictionary, maak je gebruik van vierkante haakjes: `waarde1 = dict[sleutel1]`.

**Opdracht**: Hoeveel mensen zijn er momenteel in de ruimte? Dit kan je zoeken in de dictionary via de sleutel `number`.

**Opdracht**: Kan je ook de namen van de mensen in de ruimte printen? De namen zitten in de dictionary bij de sleutel `people`. De waarde bij deze sleutel is echter lijst van dictionaries! Maak een lijst van alle namen van de mensen om deze te kunnen printen.

**Hint**: Hiervoor kan je over alle dictionaries in de lijst met astronauten gaan in een lus, de naam in de dictionary opzoeken en deze dan toevoegen aan een lijst met namen.

**Uitdaging**: Kan je voor elk van de astronauten ook het ruimtestation weergeven waarop ze zich bevinden?

## Waar is het ISS?
Het internationale ruimtestation draait om de aarde. Het voltooit ongeveer elk anderhalf uur een baan om de aarde en reist met een gemiddelde snelheid van 7,66 km per seconde. Het gaat snel! We gaan een andere webservice gebruiken om uit te zoeken waar het internationale ruimtestation ISS zich op dit moment bevindt. De webservice die te bereiken is via onderstaande URL, levert de coördinaten op van de plek op aarde waarboven het ISS momenteel vliegt. Open deze webservice ook eens in de brower om te zien hoe de data gestructureerd is. Als je over een paar minuten nog eens gaat kijken naar de webservice, dan zul je zien dat de coördinaten al weer veranderd zijn!

http://api.open-notify.org/iss-now.json

### Wat zijn breedtegraad en lengtegraad?
Lengtegraad (latitude) en breedtegraad (longitude) worden gebruikt om coördinaten te bepalen voor locaties op het aardoppervlak. 

Breedtegraad geeft de positie aan langs de noord-zuid-assen en kan elke waarde tussen 90 en -90 zijn. 0 markeert de evenaar. Lengtegraad geeft de positie langs de oost-west as aan en kan een waarde tussen -180 en 180 zijn. 0 markeert de hoofdmeridiaan, die loopt door Greenwich in Londen, VK.

Coördinaten worden gegeven als (latitude, longitude). De coördinaten van het Royal Observatory in Greenwich zijn (51.48, 0). Zoals je kunt zien, wordt eerst de breedtegraad (noord-zuid) positie gegeven. De coördinaten van het lokaal van CoderDojo zijn (51.06, 3.71), dit kun je opzoeken op de website [latlong.net](https://www.latlong.net/convert-address-to-lat-long.html).

**Opdracht**: Laad de webservice van de locatie van het ISS in Python en print de huidige coördinaten van het ISS. Om deze waarden verder te gebruiken in het project, maak je een kommagetal van deze waarden via de functie `float()`.

## Het ISS op een kaart tekenen
Dan kunnen we nu het ISS op een kaart tekenen. Hiervoor het je de package Turtle nodig, dewelke niet standaard geïnstalleerd is met Python. Als je deze nog niet geïnstalleerd hebt, kan je deze installeren door ```pip install PythonTurtle``` te runnen in de command line (het venster onderaan je scherm in Visual Studio Code, waar je anders de code runt.). Om Turtle dan te gebruiken in je code, voeg je bovenaan de volgende lijn code toe ```import turtle```.

De kaart en de icoontjes voor het ISS kun je downloaden van de CoderDojo Gent GitHub pagina. Sla ze vervolgens op in hetzelfde mapje als je code.
TODO: add link.

Dan kunnen we nu starten met de kaart te plotten. Hiervoor moeten we eerst een Turtle scherm aanmaken. We maken dit scherm 720 pixels op 360 pixels groot, want dat is de grootte van de afbeelding die we straks zullen inladen. We passen ook de coördinaten aan, zodat deze overeenkomen met de lengte- en breedtegraden.
```
scherm = turtle.Screen()
scherm.setup(720, 360)
scherm.setworldcoordinates(-180, -90, 180, 90)
scherm.bgpic('map.gif')
```

Dan kunnen we nu het icoontje toevoegen op de huidige locatie van het ISS. Er zijn twee icoontjes, namelijk `iss.gif` en `iss2.gif`, terug te vinden in de map op GitHub. Kies zelf maar dewelke je de mooiste vindt! Dan kunnen we met deze afbeelding een Turtle objectje aanmaken. Het ISS start altijd in het midden van de kaart, maar we kunnen het direct naar de juiste lcoatie bewegen met de `goto` functie.
```
scherm.register_shape('iss.gif')
iss = turtle.Turtle()
iss.shape('iss.gif')
iss.setheading(90)
iss.penup()
iss.goto(longitude, latitude)
```

Als je een paar minuten wacht, zie je dan dat het ISS ondertussen bewogen is?

**Hint**: Sluit je scherm onmiddelijk na het visualiseren van de kaart? Dan kan je onderaan je code `time.sleep(10)` toevoegen. Dit zal je code 10 seconden pauzeren, zodat je rustig de tijd hebt om je kaart te bewonderen voor deze sluit.

## Tekst toevoegen op de kaart
We willen nu ook een klein tekstje toevoegen op de kaart om te tonen hoeveel astronauten er zich momenteel in de ruimte vinden.
Hiervoor maken we opnieuw een turtle objectje aan, en voegen dit toe aan de afbeelding. Dit kan met onderstaande code:
```
tekst_astronauten = turtle.Turtle()
tekst_astronauten.penup()
```
**Opdracht**: Pas het turtle object `tekst_astronauten` aan zodat er een tekstje op de kaart verschijnt met het aantal astronauten die zich momenteel in de ruimte bevinden. Met de functie `goto` kun je de positie van de tekst kiezen, met de functie `color` kan je de kleur van de tekst kiezen, en tot slotte met `write` kun je de tekst zelf toevoegen aan de het turtle objectje.

## Oplossing

De oplossing van dit project kan je ook vinden op de CoderDojo GitHub, in dit bestandje.
Dit project is gebaseerd op [dit project](https://projects.raspberrypi.org/en/projects/where-is-the-space-station/0
) van de raspberry pi foundation.
