import pygame
import sys

class Ball:
    def __init__(self, x, y, radius, farge):
        self.rect = pygame.Rect(x - radius, y - radius, radius * 2, radius * 2)
        self.farge = farge
        self.move = [1, -1]
        self.radius = radius

    def move_ball(self):
        self.rect.x += self.move[0]
        self.rect.y += self.move[1]

    def draw(self, vindu):
        pygame.draw.ellipse(vindu, self.farge, self.rect)

    def kollisjon(self, racket, blokker):
        if self.rect.colliderect(racket.rect):
            self.move[1] = -self.move[1]
        if self.rect.left <= 0 or self.rect.right >= 500:
            self.move[0] = -self.move[0]
        if self.rect.top <= 0:
            self.move[1] = -self.move[1]
        if self.rect.bottom >= 600:
            pygame.quit()
            sys.exit()

        for blokk in blokker:
            if self.rect.colliderect(blokk.rect) and not blokk.destroyed:
                self.move[1] = -self.move[1]
                blokk.destroyed = True
