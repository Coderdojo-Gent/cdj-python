"""PONG stap 1"""
import pygame

# Pygame moet eerst ingeladen worden
pygame.init()

# Teken een venster van 800 pixels breed and 600 pixels hoog
venster = pygame.display.set_mode((800, 600))

stoppen = False
while not stoppen:
    # Bekijk alle events (gebeurtenissen)
    for event in pygame.event.get():
        print(event)

        # De event "pygame.QUIT" krijgen we als het venster wordt gesloten
        if event.type == pygame.QUIT:
            stoppen = True

    # Vul (fill) het volledig venster met de kleur zwart (= 0, 0, 0)
    venster.fill((0, 0, 0))

    # Pas alle verandering aan alle schermen toe (bijwerken)
    pygame.display.update()
