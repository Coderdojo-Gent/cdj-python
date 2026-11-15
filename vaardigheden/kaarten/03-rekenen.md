# Getallen en rekenen

Python is een supersnelle rekenmachine. Er zijn 2 soorten getallen: gehele getallen (`int`, bv. `7`) en kommagetallen (`float`, bv. `7.5`). Let op: Python schrijft een **punt** in plaats van een komma!

## Rekentekens

| Teken | Betekenis | Voorbeeld | Resultaat |
|---|---|---|---|
| `+` | optellen | `7 + 2` | `9` |
| `-` | aftrekken | `7 - 2` | `5` |
| `*` | vermenigvuldigen | `7 * 2` | `14` |
| `/` | delen | `7 / 2` | `3.5` |
| `//` | delen zonder rest | `7 // 2` | `3` |
| `%` | de rest na deling (*modulo*) | `7 % 2` | `1` |
| `**` | macht | `7 ** 2` | `49` |

Net als in de wiskunde gaan `*` en `/` voor `+` en `-`. Met haakjes verander je dat: `(2 + 3) * 4` is `20`.

## Rest na deling: %

Met `%` ga je "rond", zoals de wijzer van een klok. Na 12 uur begin je terug bij 0:

```python
print(10 % 12)   # 10
print(14 % 12)   # 2  -> 14 uur is 2 uur op de klok
print(27 % 26)   # 1  -> na de z terug naar het begin van het alfabet
```

Handig: `getal % 2 == 0` betekent dat het getal even is.

## Omzetten: int(), float() en str()

```python
tekst = "12"                # dit is tekst, geen getal!
getal = int(tekst)          # 12    tekst wordt een geheel getal
komma = float("51.06")      # 51.06 tekst wordt een kommagetal
heel = int(7.9)             # 7     int() knipt de komma eraf
mooi = round(7.9)           # 8     round() rondt af
zin = "Score: " + str(10)   # "Score: 10"  str() maakt van een getal tekst
```

## Let op

- `"3" + "4"` geeft `"34"` (tekst aan elkaar plakken). `3 + 4` geeft `7`.
- `"Score: " + 10` geeft een `TypeError`: tekst en een getal kan je niet optellen. Gebruik `str(10)`.
- Na `/` krijg je altijd een kommagetal: `10 / 2` is `5.0`. Heb je een geheel getal nodig, bv. voor pixels? Gebruik `//` of `int()`.

## Probeer het zelf

1. Hoeveel seconden zitten er in een dag? Laat Python het uitrekenen.
2. Hoeveel minuten en seconden zijn 200 seconden? Tip: gebruik `//` en `%`.
