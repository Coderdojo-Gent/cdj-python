"""Flappy Bird - Stap 4"""

import pygame

ACHTERGROND = pygame.image.load("afbeeldingen/achtergrond.png")
GROND = pygame.image.load("afbeeldingen/grond.png")

VENSTER_BREEDTE = ACHTERGROND.get_width()
VENSTER_HOOGTE = ACHTERGROND.get_height() + GROND.get_height()


class Vogel(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("afbeeldingen/vogel-midden.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.snelheid = 0

    def update(self, vlieg_omhoog=False):
        if vlieg_omhoog:
            self.snelheid = -10
        else:
            self.snelheid += 0.5
            self.rect.y += int(self.snelheid)


pygame.init()

venster = pygame.display.set_mode((VENSTER_BREEDTE, VENSTER_HOOGTE))

vogel = Vogel(100, VENSTER_HOOGTE // 2)
vogel_groep = pygame.sprite.Group()
vogel_groep.add(vogel)

klok = pygame.time.Clock()
grond_x = 0


while True:
    klok.tick(60)

    # Stop het programma als de speler op het kruisje klikt
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                vogel_groep.update(vlieg_omhoog=True)

    grond_x -= 5
    if grond_x + GROND.get_width() <= VENSTER_BREEDTE:
        grond_x = 0

    venster.blit(ACHTERGROND, (0, 0))
    venster.blit(GROND, (grond_x, ACHTERGROND.get_height()))

    vogel_groep.update()
    vogel_groep.draw(venster)

    pygame.display.update()
