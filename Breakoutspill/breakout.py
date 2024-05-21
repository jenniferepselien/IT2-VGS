import pygame
import sys
from ball import Ball
from racket import Racket
from blokk import Blokk

pygame.init()


BREDDE = 500
HOYDE = 600
FPS = 60
BALL_FARGE = ("white")
RACKET_FARGE = ("white")
BAKGRUNNSFARGE = ("pink")
BLOKK_FARGE = ("white")
RACKET_BREDDE = 100
RACKET_HOYDE = 10
BALL_RADIUS = 10


vindu = pygame.display.set_mode((BREDDE, HOYDE))
pygame.display.set_caption("Breakout Spill")
klokke = pygame.time.Clock()


ball = Ball(BREDDE // 2, HOYDE // 2, BALL_RADIUS, BALL_FARGE)
racket = Racket(BREDDE // 2 - RACKET_BREDDE // 2, HOYDE - 50, RACKET_BREDDE, RACKET_HOYDE, RACKET_FARGE)

blokker = [
    Blokk(150, 50, 80, 20, BLOKK_FARGE),
    Blokk(250, 50, 80, 20, BLOKK_FARGE),
    Blokk(350, 50, 80, 20, BLOKK_FARGE)
]


while True:
    hendelser = pygame.event.get()
    for hendelse in hendelser:
        if hendelse.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    taster = pygame.key.get_pressed()
    racket.move_racket(taster)


    ball.move_ball()
    ball.kollisjon(racket, blokker)

    if all(blokk.destroyed for blokk in blokker):
        print("Gratulerer, du har vunnet!")
        pygame.quit()
        sys.exit()

    vindu.fill(BAKGRUNNSFARGE)
    ball.draw(vindu)
    racket.draw(vindu)

    for blokk in blokker:
        blokk.draw(vindu)

    pygame.display.flip()
    klokke.tick(FPS)
