import pygame
from asteroids import *

VELOCITY_CONST = 5
class Bullet:
    def __init__(self, x, y, velocity):
        self.x = x
        self.y = y
        self.bullet_image = pygame.image.load("bullet.png")
        self.velocity = velocity * 5

    def update(self):
        print("here")
        self.x += self.velocity.x
        self.y += self.velocity.y