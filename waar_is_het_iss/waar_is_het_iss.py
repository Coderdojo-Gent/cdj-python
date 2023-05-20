from time import sleep
import urllib.request
import json
import turtle

# Laad de JSON file met alle informatie over de astronauten van de webservice:
url_astronatuen = 'http://api.open-notify.org/astros.json'
file_astronauten = urllib.request.urlopen(url_astronatuen)
dict_astronauten = json.loads(file_astronauten.read())
print(dict_astronauten)

# Aantal astronauten in de ruimte:
print(f"Aantal astronauten in de ruimte: {dict_astronauten['number']}")

# Namen van de astronauten in de ruimte:
astronauten = dict_astronauten['people']
lijst_namen = []
for astronaut in astronauten:
    lijst_namen.append(astronaut['name'])
print(f"De volgende astronauten zijn momenteel in de ruimte: {lijst_namen}")

# Namen van de astronauten in de ruimte, met het ruimtestation waarop ze zich bevinden:
for astronaut in astronauten:
    print(f"{astronaut['name']} in ruimtestation {astronaut['craft']}")

# Laad de JSON file met alle informatie over locatie van het ISS van de webservice:
url_locatie = 'http://api.open-notify.org/iss-now.json'
file_locatie = urllib.request.urlopen(url_locatie)
dict_locatie = json.loads(file_locatie.read())
print(dict_locatie)

# Locatie van het ISS op dit moment:
locatie = dict_locatie['iss_position']
latitude = float(locatie['latitude'])
longitude = float(locatie['longitude'])
print(f"De positie van het ISS is op dit moment: latitude: {latitude} - longitude: {longitude}")

# De kaart visualiseren:
scherm = turtle.Screen()
scherm.setup(720, 360)
scherm.setworldcoordinates(-180, -90, 180, 90)
scherm.bgpic('map.gif')

# Een icoontje toevoegen met de huidige locatie van het ISS:
scherm.register_shape('iss.gif')
iss = turtle.Turtle()
iss.shape('iss.gif')
iss.setheading(90)
iss.penup()
iss.goto(longitude, latitude)

# Tekst toevoegen met het aantal mensen die zich momenteel in het ISS bevinden:
tekst_astronauten = turtle.Turtle()
tekst_astronauten.penup()
tekst_astronauten.color('yellow')
tekst_astronauten.goto(-175,-25)
tekst_astronauten.write(f"Aantal astronauten in de ruimte: {dict_astronauten['number']}")

# Het programma even pauzeren zodat je tijd hebt om de kaart te bewonderen:
sleep(10)
