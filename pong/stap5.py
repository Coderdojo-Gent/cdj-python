"""PONG stap 3"""
import pygame

VENSTER_BREEDTE = 800
VENSTER_HOOGTE = 600

PALET_HOOGTE = 50
PALET_BREEDTE = 10
PALET_MARGE = 40

BAL_DIAMETER = 10
BAL_STRAAL = int(BAL_DIAMETER / 2)

KLEUR_ZWART = (0, 0, 0)
KLEUR_WIT = (255, 255, 255)

# Start positie voor palet 1
palet_1_x = PALET_MARGE
palet_1_y = int(VENSTER_HOOGTE/2 - PALET_HOOGTE/2)

# Start positie voor palet 2
palet_2_x = VENSTER_BREEDTE - PALET_MARGE - PALET_BREEDTE
palet_2_y = int(VENSTER_HOOGTE/2 - PALET_HOOGTE/2)

bal_x = 400
bal_y = 300
bal_x_snelheid = 2
bal_y_snelheid = 2

# Pygame moet eerst ingeladen worden
pygame.init()
clock = pygame.time.Clock()

# Teken een venster van 800 pixels breed and 600 pixels hoog
venster = pygame.display.set_mode((VENSTER_BREEDTE, VENSTER_HOOGTE))

stoppen = False
while not stoppen:
    # Bekijk alle events (gebeurtenissen)
    for event in pygame.event.get():
        print(event)

        # De event "pygame.QUIT" krijgen we als het venster wordt gesloten
        if event.type == pygame.QUIT:
            stoppen = True

    # Bal bots met rand onder
    if bal_y + BAL_STRAAL >= VENSTER_HOOGTE:
        bal_y_snelheid = bal_y_snelheid * -1

    # Bal bots met rand boven
    if bal_y - BAL_STRAAL <= 0:
        bal_y_snelheid = bal_y_snelheid * -1

    # Bal bots met rand rechts
    if bal_x + BAL_STRAAL >= VENSTER_BREEDTE:
        bal_x_snelheid = bal_x_snelheid * -1

    # Bal bots met rand links
    if bal_x - BAL_STRAAL <= 0:
        bal_x_snelheid = bal_x_snelheid * -1

    bal_x += bal_x_snelheid
    bal_y += bal_y_snelheid

    # Vul (fill) het volledig venster met de kleur zwart
    venster.fill(KLEUR_ZWART)

    pygame.draw.circle(venster, KLEUR_WIT, [bal_x, bal_y], BAL_DIAMETER)

    # Palet 1
    pygame.draw.rect(
        venster,
        KLEUR_WIT,
        pygame.Rect(palet_1_x, palet_1_y, PALET_BREEDTE, PALET_HOOGTE),
    )

    # Palet 2
    pygame.draw.rect(
        venster,
        KLEUR_WIT,
        pygame.Rect(palet_2_x, palet_2_y, PALET_BREEDTE, PALET_HOOGTE),
    )

    # Pas alle verandering aan alle schermen toe (bijwerken)
    pygame.display.update()
    clock.tick(60)
