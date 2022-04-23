from random import random
from game_objects import GameObjects
import pygame

import random
from Vector2D import Vector2D


class Asteroid:
    skins = ["meteor_big.png", "meteor_medium.png", "meteor_small.png"]
    
    def __init__(self, x, y, direction: Vector2D):
        self.x = x
        self.y = y
        self.direction = direction
        self.image = pygame.image.load(random.choice(Asteroid.skins))
    
    def update(self):
        self.x += self.direction.x
        self.y += self.direction.y
        self.check_inbounds()
        GameObjects.window.blit(self.image, (self.x, self.y))

    def check_inbounds(self):
        if self.y >= GameObjects.HEIGHT + 66:
            self.y = -33
        if self.y < -66:
            self.y = GameObjects.HEIGHT + 33
        if self.x >= GameObjects.WIDTH + 66:
            self.x = -33
        if self.x < -66:
            self.x = GameObjects.WIDTH + 33
