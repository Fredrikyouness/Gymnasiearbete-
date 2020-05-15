from GameObjects import *

class Enemy(PhysicalObject):
    def __init__(self, texture, X, Y, speedX, speedY):
        super().__init__(texture, X, Y, speedX, speedY)

    def update(self, win_width, win_height):
        pass

class Mine(Enemy):
    def __init__(self, texture, X, Y, speedX, speedY):
        super().__init__(texture, X, Y, speedX, speedY)
        self.rect = self.texture.get_rect()
        self.rect.topleft = self.vector

    def update(self, win_width, win_height):
        self.vector.x += self.speed.x
        self.vector.y += self.speed.y
        self.rect.topleft = self.vector

        if self.vector.x > win_width - self.rect.width or self.vector.x < 0:
            self.speed.x *= -1

        if self.vector.y > win_height:
            self.isAlive = False

class Tripod(Enemy):
    def __init__(self, texture, X, Y, speedX, speedY):
        super().__init__(texture, X, Y, speedX, speedY)
        self.rect = self.texture.get_rect()
        self.rect.topleft = self.vector

    def update(self, win_width, win_height):
        self.vector.y += self.speed.y
        self.rect.topleft = self.vector

        if self.vector.y > win_height:
            self.isAlive = False
