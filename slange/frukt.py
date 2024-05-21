import pygame
import random

class Frukt:
    def __init__(self, storrelse, tall):
        self.posisjon = (random.randint(0, tall-1), random.randint(0, tall-1))
        self.storrelse = storrelse

    def tegne_frukt(self, vindu):
        x_pos = self.posisjon[0] * self.storrelse
        y_pos = self.posisjon[1] * self.storrelse
        frukt_rekt = pygame.Rect(x_pos, y_pos, self.storrelse, self.storrelse)
        pygame.draw.rect(vindu, ("red"), frukt_rekt)
