import pygame

class Racket:
    def __init__(self, x, y, bredde, hoyde, farge):
        self.rect = pygame.Rect(x, y, bredde, hoyde)
        self.farge = farge

    def move_racket(self, taster):
        if taster[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= 5
        if taster[pygame.K_RIGHT] and self.rect.right < 500:
            self.rect.x += 5

    def draw(self, vindu):
        pygame.draw.rect(vindu, self.farge, self.rect)
