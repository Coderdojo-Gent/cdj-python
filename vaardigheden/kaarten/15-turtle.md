# Tekenen met turtle

Met de module `turtle` teken je met een schildpad. De schildpad loopt over het scherm en trekt een lijn waar ze komt, net als de pen in Scratch.

## Zo werkt het

```python
import turtle

elsa = turtle.Turtle()     # maak een schildpad met de naam elsa
elsa.forward(100)          # 100 stappen vooruit
elsa.right(90)             # 90 graden naar rechts draaien

turtle.done()              # hou het venster open tot je het sluit
```

## Een vierkant met een for-lus

```python
import turtle

elsa = turtle.Turtle()
for i in range(4):
    elsa.forward(100)
    elsa.right(90)
turtle.done()
```

Een ster? Herhaal 5 keer en draai telkens 144 graden.

## De belangrijkste opdrachten (`t` is je schildpad)

| Code | Wat doet het? |
|---|---|
| `t.forward(50)` en `t.backward(50)` | vooruit en achteruit |
| `t.right(90)` en `t.left(90)` | draaien, in graden |
| `t.penup()` en `t.pendown()` | pen omhoog (niet tekenen) en omlaag |
| `t.goto(x, y)` | naar een plaats gaan: (0, 0) is het midden (kaart 14) |
| `t.setheading(90)` | in een richting kijken: 0 = rechts, 90 = boven |
| `t.circle(50)` | een cirkel met straal 50 |
| `t.color("red")` en `t.pensize(5)` | kleur en dikte van de pen |
| `t.begin_fill()` ... `t.end_fill()` | de vorm daartussen inkleuren |
| `t.shape("turtle")` en `t.stamp()` | vorm kiezen (`"arrow"`, `"turtle"`, `"circle"`...) en stempelen |
| `t.write("Hallo")` en `t.speed(0)` | tekst schrijven, en zo snel mogelijk tekenen |

## Het scherm

```python
scherm = turtle.Screen()
scherm.bgcolor("black")    # achtergrondkleur
scherm.setup(720, 360)     # breedte en hoogte van het venster
```

## Let op

- Gaat het venster meteen dicht? Zet `turtle.done()` helemaal onderaan.
- Noem je bestand niet `turtle.py`!
- Op veel online Python-websites werkt turtle niet. Gebruik Python op je computer.

## Probeer het zelf

Teken een huisje: een vierkant met een driehoek erop. Tip: voor een driehoek draai je 3 keer 120 graden.
