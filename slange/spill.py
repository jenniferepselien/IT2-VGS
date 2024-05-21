import pygame
import sys
from main import Main

pygame.init()


pygame.display.set_caption('FAKE SNAKE')


STORRELSE = 40 
TALL = 20 

vindu = pygame.display.set_mode((STORRELSE * TALL, STORRELSE * TALL))
klokke = pygame.time.Clock()
FPS = 60 


main_spill = Main()

VINDU_OPPDATER = pygame.USEREVENT
pygame.time.set_timer(VINDU_OPPDATER, 150)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and main_spill.slange.rettning != (0, 1):
                main_spill.slange.rettning = (0, -1)
            if event.key == pygame.K_RIGHT and main_spill.slange.rettning != (-1, 0):
                main_spill.slange.rettning = (1, 0)
            if event.key == pygame.K_DOWN and main_spill.slange.rettning != (0, -1):
                main_spill.slange.rettning = (0, 1)
            if event.key == pygame.K_LEFT and main_spill.slange.rettning != (1, 0):
                main_spill.slange.rettning = (-1, 0)

        if event.type == VINDU_OPPDATER:
            main_spill.oppdater()
            main_spill.sjekk_kollisjon()
            if main_spill.sjekk_game_over():
                pygame.quit()
                sys.exit()

    vindu.fill(pygame.Color('pink'))
    
    main_spill.tegn_element(vindu)
    
    pygame.display.update()
    klokke.tick(FPS)
