from GameObjects import *

class Player(PhysicalObject):
    def __init__(self, texture, X, Y, speedX, speedY):
        super().__init__(texture, X, Y, speedX, speedY)
        self.rect = self.texture.get_rect()
        self.rect.topleft = self.vector
        self.points = 0

    def update(self, win_width, win_height):
        keys = pygame.key.get_pressed()

        if self.vector.x <= win_width - self.rect.width or self.vector.x >= 0:
            if keys[pygame.K_LEFT]:
                self.vector.x -= self.speed.x
            if keys[pygame.K_RIGHT]:
                self.vector.x += self.speed.x

        if self.vector.y <= win_height - self.rect.height or self.vector.y >= 0:
            if keys[pygame.K_UP]:
                self.vector.y -= self.speed.y
            if keys[pygame.K_DOWN]:
                self.vector.y += self.speed.y

        self.rect.topleft = self.vector

        if self.vector.x < 0:
            self.vector.x = 0

        if self.vector.x > win_width - self.rect.width:
            self.vector.x = win_width - self.rect.width

        if self.vector.y < 0:
            self.vector.y = 0

        if self.vector.y > win_height - self.rect.height:
            self.vector.y = win_height - self.rect.height




class Bullet(PhysicalObject):
    def __init__(self, texture, X, Y, speedX, speedY):
        super().__init__(texture, X, Y, speedX, speedY)
        self.rect = self.texture.get_rect()
        self.rect.topleft = self.vector

    def update(self):
        self.vector.y -= self.speed.y
        self.rect.topleft = self.vector

        if self.vector.y < 0:
           self.isAlive = False