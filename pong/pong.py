"""PONG"""
import pygame

VENSTER_BREEDTE = 800
VENSTER_HOOGTE = 600

KLEUR_ZWART = (0, 0, 0)
KLEUR_WIT = (255, 255, 255)

BAL_X_SNELHEID = -2
BAL_Y_SNELHEID = -1
BAL_DIAMETER = 10
BAL_STRAAL = int(BAL_DIAMETER / 2)

PALET_HOOGTE = 50
PALET_BREEDTE = 10
PALET_MARGE = 40

bal_x = int(VENSTER_BREEDTE / 2)
bal_y = int(VENSTER_HOOGTE / 2)

palet_1_x = PALET_MARGE
palet_1_y = int(VENSTER_HOOGTE / 2) - int(PALET_HOOGTE / 2)

palet_2_x = VENSTER_BREEDTE - PALET_MARGE - PALET_BREEDTE
palet_2_y = int(VENSTER_HOOGTE / 2) - int(PALET_HOOGTE / 2)

score_1 = 0
score_2 = 0

pygame.init()
venster = pygame.display.set_mode((VENSTER_BREEDTE, VENSTER_HOOGTE))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit()

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_w]:
        palet_1_y -= 2
    elif pressed[pygame.K_s]:
        palet_1_y += 2
    if pressed[pygame.K_UP]:
        palet_2_y -= 2
    elif pressed[pygame.K_DOWN]:
        palet_2_y += 2

    if bal_y <= BAL_STRAAL or bal_y >= VENSTER_HOOGTE - BAL_STRAAL:
        BAL_Y_SNELHEID *= -1

    # Palet 1 raakt de bal
    if (bal_x <= PALET_MARGE + PALET_BREEDTE) and (bal_x > PALET_MARGE):
        if (bal_y > palet_1_y) and (bal_y < palet_1_y + PALET_HOOGTE):
            BAL_X_SNELHEID *= -1

    # Palet 2 raakt de bal
    if (bal_x >= VENSTER_BREEDTE - PALET_MARGE - PALET_BREEDTE) and (
        bal_x < VENSTER_BREEDTE - PALET_MARGE
    ):
        print("XXXXXXXXX")
        if (bal_y > palet_2_y) and (bal_y < palet_2_y + PALET_HOOGTE):
            BAL_X_SNELHEID *= -1

    # Speler 2 scoort
    if bal_x <= BAL_STRAAL or bal_x >= VENSTER_BREEDTE - BAL_STRAAL:
        score_1 += 1
        bal_x = int(VENSTER_BREEDTE / 2)
        bal_y = int(VENSTER_HOOGTE / 2)

    # Speler 1 scoort
    if bal_x >= VENSTER_BREEDTE - BAL_STRAAL:
        score_2 += 1
        bal_x = int(VENSTER_BREEDTE / 2)
        bal_y = int(VENSTER_HOOGTE / 2)

    bal_x += BAL_X_SNELHEID
    bal_y += BAL_Y_SNELHEID

    venster.fill(KLEUR_ZWART)
    pygame.draw.rect(
        venster,
        KLEUR_WIT,
        pygame.Rect((VENSTER_BREEDTE / 2) - 2, 0, 4, VENSTER_HOOGTE),
    )
    font = pygame.font.Font(None, 60)
    text = font.render(str(score_1), True, KLEUR_WIT)
    venster.blit(text, (VENSTER_BREEDTE / 2 - 80, 10))
    text = font.render(str(score_2), True, KLEUR_WIT)
    venster.blit(text, (VENSTER_BREEDTE / 2 + 20, 10))
    pygame.draw.circle(venster, KLEUR_WIT, [bal_x, bal_y], BAL_DIAMETER)
    pygame.draw.rect(
        venster,
        KLEUR_WIT,
        pygame.Rect(palet_1_x, palet_1_y, PALET_BREEDTE, PALET_HOOGTE),
    )
    pygame.draw.rect(
        venster,
        KLEUR_WIT,
        pygame.Rect(palet_2_x, palet_2_y, PALET_BREEDTE, PALET_HOOGTE),
    )
    pygame.display.update()
    clock.tick(60)
