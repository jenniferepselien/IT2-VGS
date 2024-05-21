import pygame

class Blokk:
    def __init__(self, x, y, bredde, hoyde, farge):
        self.rect = pygame.Rect(x, y, bredde, hoyde)
        self.farge = farge
        self.destroyed = False

    def draw(self, vindu):
        if not self.destroyed:
            pygame.draw.rect(vindu, self.farge, self.rect)
