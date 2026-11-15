# Werken met tekst (strings)

Tekst heet in Python een *string*: een rij tekens (letters, cijfers, spaties...) achter elkaar. Je zet een string tussen aanhalingstekens: `"galgje"` of `'galgje'`.

## Elke letter heeft een plaats

| g | a | l | g | j | e |
|---|---|---|---|---|---|
| 0 | 1 | 2 | 3 | 4 | 5 |

```python
woord = "galgje"
print(woord[0])          # g   de eerste letter heeft plaats 0!
print(woord[-1])         # e   -1 is de laatste letter
print(len(woord))        # 6   het aantal tekens
print(woord.find("l"))   # 2   op welke plaats staat "l"? (-1 als ze er niet in zit)
print("j" in woord)      # True
```

## Handige bewerkingen

| Code | Resultaat |
|---|---|
| `"Hallo " + "Jan"` | `"Hallo Jan"` (aan elkaar plakken) |
| `"ha" * 3` | `"hahaha"` |
| `"CoderDojo".lower()` | `"coderdojo"` (alles klein) |
| `"CoderDojo".upper()` | `"CODERDOJO"` (alles groot) |
| `"ga oost".split()` | `["ga", "oost"]` (knippen bij de spaties, zie kaart 9) |
| `"abc".isalpha()` | `True` (alleen letters?) |

## Een nieuwe string opbouwen

Je kan 1 letter van een string niet veranderen. Je kan wel een nieuwe string opbouwen, letter per letter:

```python
bericht = "kat"
nieuw = ""                     # begin met een lege string
for letter in bericht:
    nieuw += letter.upper()    # plak er telkens een letter achter
print(nieuw)                   # KAT
```

## f-strings: variabelen in je tekst

Zet een `f` voor de aanhalingstekens. Dan mag je variabelen tussen `{ }` zetten:

```python
naam = "Sam"
score = 7
print(f"{naam} heeft {score} punten")   # Sam heeft 7 punten
```

## Let op

- `"galgje"` heeft plaatsen 0 tot 5. `woord[6]` geeft een `IndexError`.
- `woord.lower()` verandert `woord` zelf niet, maar maakt een nieuwe string. Bewaar ze: `woord = woord.lower()`.

## Probeer het zelf

Vraag een woord en print het achterstevoren. Tip: begin met `omgekeerd = ""` en plak elke letter er **voor**: `omgekeerd = letter + omgekeerd`.
