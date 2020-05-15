from Player import *
from Enemy import *
from GoldCoin import *
import random
import time



class Game:
    def __init__(self):
        pygame.init()
        self.win_width = 800
        self.win_height = 480
        self.win = pygame.display.set_mode((self.win_width, self.win_height))
        self.run = True
        self.clock = pygame.time.Clock()
        self.font = pygame.font.match_font('arial')

        self.player_sprite = pygame.image.load("images/ship.png")
        self.bullet_sprite = pygame.image.load("images/bullet.png")
        self.mine_sprite = pygame.image.load("images/mine.png")
        self.tripod_sprite = pygame.image.load("images/tripod.png")
        self.goldCoin_sprite = pygame.image.load("images/coin.png")

        self.enemies = []
        self.goldCoins = []
        self.bullets = []
        self.timeSinceLastBullet = 10

    def LoadContent(self):
        self.start_time = time.time()
        self.player = Player(self.player_sprite, 380, 400, 2.5, 4.5)

        i = 0
        while i < 10:
            i += 1
            rndX = random.randint(0, self.win_width - self.mine_sprite.get_size()[0])
            rndY = random.randint(0, self.win_height / 2)
            temp = Mine(self.mine_sprite, rndX, rndY, 6, 0.3)
            self.enemies.append(temp)

        i = 0
        while i < 5:
            i += 1
            rndX = random.randint(0, self.win_width - self.tripod_sprite.get_size()[0])
            rndY = random.randint(0, self.win_height / 2)
            temp = Tripod(self.tripod_sprite, rndX, rndY, 0, 3)
            self.enemies.append(temp)

        self.MainGame()


    def MainGame(self):
        while self.run:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False

            self.update()
            self.draw()

    def update(self):
        self.timeSinceLastBullet += 1
        keys = pygame.key.get_pressed()

        self.player.update(self.win_width, self.win_height)

        for enemy in self.enemies:
            if enemy.isAlive:
                for bullet in self.bullets:
                    if bullet.rect.colliderect(enemy.rect):
                        enemy.isAlive = False
                        self.player.points += 1

                if enemy.rect.colliderect(self.player.rect):
                    self.player.isAlive = False

                enemy.update(self.win_width, self.win_height)

            else:
                self.enemies.remove(enemy)

        if keys[pygame.K_ESCAPE]:
            self.run = False

        if keys[pygame.K_SPACE]:
            if self.timeSinceLastBullet >= 10:
                self.timeSinceLastBullet = 0
                temp = Bullet(self.bullet_sprite, self.player.rect.center, self.player.rect.top, 0, 3)
                self.bullets.append(temp)

        for bullet in self.bullets:
            if bullet.isAlive:
                bullet.update()
            else:
                self.bullets.remove(bullet)

        newCoin = random.randint(1, 200)
        if newCoin == 1:
            rndX = random.randint(0, self.win_width - self.goldCoin_sprite.get_size()[0])
            rndY = random.randint(0, self.win_height)
            temp = GoldCoin(self.goldCoin_sprite, rndX, rndY, 0, 0)
            self.goldCoins.append(temp)

        for gc in self.goldCoins:
            if gc.isAlive:
                if gc.rect.colliderect(self.player.rect):
                    gc.isAlive = False
                    self.player.points += 1
                gc.update()

            else:
                self.goldCoins.remove(gc)

        if not(self.player.isAlive):
            self.run = False


    def draw(self):
        self.win.fill((100, 149, 237))

        self.player.draw(self.win)

        for enemy in self.enemies:
            enemy.draw(self.win)

        for bullet in self.bullets:
            bullet.draw(self.win)

        for gc in self.goldCoins:
            gc.draw(self.win)

        self.text("Points: " + str(self.player.points), 48, (255, 255, 255), 0, 0)

        pygame.display.flip()

        
    def text(self, text, size, color, x, y):
        font = pygame.font.Font(self.font, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.topleft = (x, y)
        self.win.blit(text_surface, text_rect)



game = Game()
game.LoadContent()

pygame.quit()