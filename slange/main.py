from frukt import Frukt
from slange import Slange

class Main:
    def __init__(self):
        self.frukt = Frukt(40, 20)
        self.slange = Slange(40, 20)

    def oppdater(self):
        self.slange.beveg()

    def tegn_element(self, vindu):
        self.frukt.tegne_frukt(vindu)
        self.slange.tegne_slange(vindu)

    def sjekk_kollisjon(self):
        if self.slange.kropp[0] == self.frukt.posisjon:
            self.frukt = Frukt(40, 20)  # Generer ny frukt
            self.slange.kropp.append(self.slange.kropp[-1])  # Legg til en blokk til slangen

    def sjekk_game_over(self):
        if self.slange.sjekk_kollisjon_vegger() or self.slange.sjekk_kollisjon_seg_selv():
            return True
        return False
