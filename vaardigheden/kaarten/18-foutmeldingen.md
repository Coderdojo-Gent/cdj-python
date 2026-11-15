# Foutmeldingen lezen

Elke programmeur krijgt foutmeldingen, ook de beste. Een foutmelding is geen straf: Python vertelt je **waar** en **wat** er mis is.

## Zo lees je een foutmelding

```text
Traceback (most recent call last):
  File "galgje.py", line 7, in <module>
    print("Je hebt nog " + levens + " levens")
TypeError: can only concatenate str (not "int") to str
```

1. Begin **onderaan**: de laatste regel zegt wat er mis is. Hier: tekst en een getal optellen.
2. Kijk erboven: in welk bestand, op welke **regel** (`line 7`), en welke code daar staat.
3. Soms zit de echte fout een regel **hoger**, bv. een haakje dat niet gesloten is.

## De foutmeldingen die je het meest ziet

| Foutmelding | Wat is er meestal mis? |
|---|---|
| `SyntaxError` | Python snapt de zin niet: `:` vergeten, haakje of aanhalingsteken niet gesloten, `=` in plaats van `==`. |
| `IndentationError` | Het inspringen klopt niet. Gebruik altijd 4 spaties per niveau. |
| `NameError` | Typfout in een naam (hoofdletters tellen!), of de variabele heeft nog geen waarde. |
| `TypeError` | Verkeerde soort gegevens, bv. `"tekst" + 5`. Gebruik `str()` of `int()`. |
| `ValueError` | Juiste soort, verkeerde waarde, bv. `int("hallo")`. |
| `IndexError` | Die plaats bestaat niet, bv. `lijst[5]` in een lijst met 5 elementen. |
| `KeyError` | Die sleutel zit niet in de dictionary. |
| `ModuleNotFoundError` | Module niet geïnstalleerd (`pip install`), of de naam is verkeerd getypt. |
| `FileNotFoundError` | Bestand niet gevonden. Staat het in dezelfde map? |

## Geen foutmelding, maar het werkt toch niet?

Zet extra `print()`-regels in je code. Zo zie je welke waarde je variabelen echt hebben:

```python
print("gok is:", gok, "- woord is:", woord)
```

## Stappenplan als je vastzit

1. Lees de foutmelding, de onderste regel eerst.
2. Kijk naar die regel, en naar de regel erboven.
3. Vergelijk letter per letter met het voorbeeld: hoofdletters, haakjes, dubbelpunten, inspringen.
4. Leg aan iemand anders (of aan een knuffel) uit wat elke regel doet. Vaak zie je de fout dan zelf!
5. Nog altijd vast? Vraag een coach.

## Probeer het zelf

Er zitten 3 fouten in deze code. Vind en verbeter ze:

```python
naam = input("Hoe heet je? ")
if naam = "Sam"
    print("Hallo " + Naam)
```
