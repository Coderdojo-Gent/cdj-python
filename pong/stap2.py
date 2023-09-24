"""PONG stap 1"""
import pygame

VENSTER_BREEDTE = 800
VENSTER_HOOGTE = 600

KLEUR_ZWART = (0, 0, 0)
KLEUR_WIT = (255, 255, 255)

# Pygame moet eerst ingeladen worden
pygame.init()

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

    # Vul (fill) het volledig venster met de kleur zwart
    venster.fill(KLEUR_ZWART)

    pygame.draw.circle(venster, KLEUR_WIT, [400, 300], 5)

    # Pas alle verandering aan alle schermen toe (bijwerken)
    pygame.display.update()
