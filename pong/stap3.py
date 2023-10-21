"""PONG stap 3"""
import pygame

VENSTER_BREEDTE = 800
VENSTER_HOOGTE = 600

KLEUR_ZWART = (0, 0, 0)
KLEUR_WIT = (255, 255, 255)

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

    bal_x += bal_x_snelheid
    bal_y += bal_y_snelheid

    # Vul (fill) het volledig venster met de kleur zwart
    venster.fill(KLEUR_ZWART)

    pygame.draw.circle(venster, KLEUR_WIT, [bal_x, bal_y], 10)

    # Pas alle verandering aan alle schermen toe (bijwerken)
    pygame.display.update()
    clock.tick(60)
