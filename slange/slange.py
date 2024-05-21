import pygame

class Slange:
    def __init__(self, storrelse, tall):
        self.kropp = [(5, 10), (4, 10), (3, 10)]
        self.rettning = (1, 0)
        self.storrelse = storrelse
        self.tall = tall

    def beveg(self):
        hode = (self.kropp[0][0] + self.rettning[0], self.kropp[0][1] + self.rettning[1])
        self.kropp.insert(0, hode)
        self.kropp.pop()

    def tegne_slange(self, vindu):
        for blokk in self.kropp:
            x_pos = blokk[0] * self.storrelse
            y_pos = blokk[1] * self.storrelse
            blokk_rekt = pygame.Rect(x_pos, y_pos, self.storrelse, self.storrelse)
            pygame.draw.rect(vindu, ("white"), blokk_rekt)

    def sjekk_kollisjon_vegger(self):
        hode = self.kropp[0]
        if hode[0] < 0 or hode[0] >= self.tall or hode[1] < 0 or hode[1] >= self.tall:
            return True
        return False

    def sjekk_kollisjon_seg_selv(self):
        hode = self.kropp[0]
        for blokk in self.kropp[1:]:
            if blokk == hode:
                return True
        return False
