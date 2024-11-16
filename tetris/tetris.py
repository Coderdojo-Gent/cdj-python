"""Tetris."""

import pygame

KOLOMMEN = 10
RIJEN = 20
CELL_GROOTTE = 40

SPEELVELD_BREEDTE = KOLOMMEN * CELL_GROOTTE
SPEELVELD_HOOGTE = RIJEN * CELL_GROOTTE

RAND_BREEDTE = 20

VENSTER_HOOGTE = SPEELVELD_HOOGTE + 2 * RAND_BREEDTE
VENSTER_BREEDTE = SPEELVELD_BREEDTE + 2 * RAND_BREEDTE

GEEL = "#F1E60D"
ROOD = "#E51B20"
BLAUW = "#204B9B"
GROEN = "#65B32E"
PAARS = "#7B217F"
ORANJE = "#F07E13"
GRIJS = "#1C1C1C"
WIT = "#FFFFFF"


class Block(pygame.sprite.Sprite):
    def __init__(self, group, kleur, kolom, rij):
        super().__init__(group)
        self.image = pygame.Surface((CELL_GROOTTE, CELL_GROOTTE))
        self.image.fill(kleur)

        x = kolom * CELL_GROOTTE
        y = rij * CELL_GROOTTE
        self.rect = self.image.get_rect(topleft=(x, y))


pygame.init()
pygame.display.set_caption("Tetris!")
venster = pygame.display.set_mode((VENSTER_BREEDTE, VENSTER_HOOGTE))
speelveld = pygame.Surface((SPEELVELD_BREEDTE, SPEELVELD_HOOGTE))
clock = pygame.time.Clock()
sprites = pygame.sprite.Group()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    venster.fill(GRIJS)
    venster.blit(speelveld, (RAND_BREEDTE, RAND_BREEDTE))

    # BLOKKEN
    block = Block(sprites, "red", 3, 5)
    block = Block(sprites, "red", 3, 6)
    block = Block(sprites, "red", 3, 7)
    sprites.draw(speelveld)

    # ROOSTER
    for kolom in range(1, KOLOMMEN):
        x = kolom * CELL_GROOTTE
        pygame.draw.line(speelveld, WIT, (x, 0), (x, SPEELVELD_HOOGTE), 2)
    for rij in range(1, RIJEN):
        y = rij * CELL_GROOTTE
        pygame.draw.line(speelveld, WIT, (0, y), (SPEELVELD_BREEDTE, y), 2)
    pygame.draw.rect(speelveld, WIT, (0, 0, SPEELVELD_BREEDTE, SPEELVELD_HOOGTE), 2)

    pygame.display.update()
    clock.tick()
