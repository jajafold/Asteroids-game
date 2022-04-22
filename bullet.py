import pygame
from game_objects import GameConsts

class Bullet:
    VELOCITY_CONST = 50
    def __init__(self, x, y, velocity):
        self.x = x
        self.y = y
        self.bullet_image = pygame.image.load("bullet.png")
        self.velocity = velocity * Bullet.VELOCITY_CONST

    def update(self):
        self.x += self.velocity.x
        self.y += self.velocity.y
        GameConsts.window.blit(self.bullet_image, (self.x, self.y))