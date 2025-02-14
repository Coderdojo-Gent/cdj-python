"""Flappy Bird - Stap 7"""

import random
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


class Buis(pygame.sprite.Sprite):

    def __init__(self, x, y, flip=False):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("afbeeldingen/buis.png")
        self.rect = self.image.get_rect()
        if flip:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft = (x, y)
        else:
            self.rect.topleft = (x, y)

    def update(self):
        self.rect.x -= 5
        if self.rect.right < 0:
            self.kill()


pygame.init()

venster = pygame.display.set_mode((VENSTER_BREEDTE, VENSTER_HOOGTE))

vogel = Vogel(100, VENSTER_HOOGTE // 2)
vogel_groep = pygame.sprite.Group()
vogel_groep.add(vogel)

laatste_buis = pygame.time.get_ticks()
buis_interval = 1500
buis_groep = pygame.sprite.Group()

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

    vogel_groep.update()
    vogel_groep.draw(venster)

    if pygame.time.get_ticks() >= laatste_buis + buis_interval:
        midden = ACHTERGROND.get_height() // 2
        buis_midden = random.randrange(midden - 200, midden + 200)
        buis_onder = Buis(VENSTER_BREEDTE, buis_midden + 75)
        buis_boven = Buis(VENSTER_BREEDTE, buis_midden - 75, flip=True)
        buis_groep.add(buis_onder)
        buis_groep.add(buis_boven)
        laatste_buis = pygame.time.get_ticks()

    buis_groep.update()
    buis_groep.draw(venster)

    venster.blit(GROND, (grond_x, ACHTERGROND.get_height()))

    if (
        pygame.sprite.groupcollide(vogel_groep, buis_groep, False, False)
        or vogel.rect.top < 0
        or vogel.rect.bottom > ACHTERGROND.get_height()
    ):
        buis_groep.empty()
        vogel.rect.x = 100
        vogel.rect.y = VENSTER_HOOGTE // 2

    pygame.display.update()
