import pygame

V = pygame.math.Vector2

class GameObject(pygame.sprite.Sprite):
    def __init__(self, texture, X, Y):
        pygame.sprite.Sprite.__init__(self)
        self.texture = texture
        self.vector = V(X, Y)

    def draw(self, win):
        win.blit(self.texture, self.vector)

class MovingObject(GameObject):
    def __init__(self, texture, X, Y, speedX, speedY):
        super().__init__(texture, X, Y)
        self.speed = V(speedX, speedY)

class PhysicalObject(MovingObject):
    def __init__(self, texture, X, Y, speedX, speedY):
        super().__init__(texture, X, Y, speedX, speedY)
        self.isAlive = True

    def CheckCollision(self, other):
        pass