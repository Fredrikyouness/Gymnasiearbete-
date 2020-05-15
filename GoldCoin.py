from GameObjects import *

class GoldCoin(PhysicalObject):
    def __init__(self, texture, X, Y, speedX, speedY):
        super().__init__(texture, X, Y, speedX, speedY)
        self.rect = self.texture.get_rect()
        self.rect.topleft = self.vector
        self.timeToDie = 300

    def update(self):
        self.timeToDie -= 1

        if self.timeToDie <= 0:
            self.isAlive = False