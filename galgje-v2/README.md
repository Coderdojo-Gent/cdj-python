# Galgje V2

In onze eerste versie van galgje is het te raden woord op voorhand bepaald in de code van het programma.

Het zou veel leuker zijn als het programma zelf een willekeurig woord kiest!

## Stap 0: Woordenlijst downloaden

Op de website https://www.opentaal.org/bestanden/file/2-woordenlijst-v-2-10g-bronbestanden kan je een zip-bestand downloaden. Hierin zitten een aantal bestanden, waarvan we enkel `OpenTaal-210G-basis-gekeurd.txt` nodig hebben. Kopieer dat bestand naar dezelfde map waarin je Python code staat.

Als je het bestand open zie je hele lange lijst woorden.

## Stap 1: Bestand inlezen en willekeurig woord kiezen

Om te beginnen schrijven we een klein programma dat het bestand inleest en een willekeurig woord print.

Tips:
* Een bestand openen doe je met de functie `open`. Bvb.

```python
with open("bestandsnaam.txt") as bestand:
    inhoud = bestand.read()
```

* Het zal later handig zijn als we het bestand met woorden inlezen in een Python lijst (`list`) van `string`s, waarbij elke lijn uit het bestand een element wordt in de lijst. Dit kan je doen met de functie `splitlines()`.
* Om een willekeurig element uit een lijst de kiezen gebruik je de functie `random.choice()`. Hiervoor moet je wel eerst de `random` module importeren.

## Stap 2: Goede woorden kiezen

Het is je misschien al opgevallen dat de woordenlijst een aantal elementen bevat die wel erg moeilijk te raden zijn. Bvb. woorden met aanhalingstekens en/of spaties (`'s nachts`), getallen (`1 aprilgrap`), acroniemen/afkorting (`ADHD`), speciale tekens (`beëdigd`).

In deze stap bekijken we elke woord uit het bestand en houden we enkel woorden die we willen over.

Maak een nieuwe woordenlijst met de woorden waarin enkel de "gewone" letters `a` tot `z` in voorkomen (dus ook geen hoofdletters).

Tips:
* De string functie `isalpha()` kijkt of de string enkel uit letters bestaat
* De string functie `islower()` kijkt of de string enkel uit kleine letters bestaat (geen hoofdletters)
* De string functie `isascii()` kijkt of de string enkel uit gewone letters bestaat (bvb geen `ë`)

## Stap 3: Woordlengte kiezen

We willen natuurlijk een willekeurig woord van een welbepaalde lengte. Breid de code uit stap 2 uit zodat enkel woorden van een bepaalde lengte overblijven. Gebruik eventueel een variable om de lengte bij te houden zodat wie die later makkelijk kunnen aanpassen.

Tips:
* Met de functie `len()` kan je te lengte van een `string` bepalen

## Step 4: Code samenvoegen

Nu kunnen we de code uit onze eerste versie van galgje samenvoegen met onze nieuwe code zodat het programma een willekeurig woord kiest.
