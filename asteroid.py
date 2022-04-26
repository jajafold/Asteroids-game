from random import random
from game_objects import GameObjects
import pygame

import random
from Vector2D import Vector2D


class Asteroid(pygame.sprite.Sprite):
    skins = ["meteor_big.png", "meteor_medium.png", "meteor_small.png"]
    
    def __init__(self, x, y, direction: Vector2D):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.direction = direction * random.randint(1, 3)
        self.image = pygame.image.load(random.choice(Asteroid.skins))
        self.rect = self.image.get_bounding_rect()

        GameObjects.asteroids[self] = self.offset_rect
    
    def update(self):
        self.x += self.direction.x
        self.y += self.direction.y
        self.check_inbounds()

        self.detect_collision()

        GameObjects.window.blit(self.image, (self.x, self.y))

    def detect_collision(self):
        bullet_to_delete = None
        for bullet in GameObjects.bullets.keys():
            if pygame.Rect.colliderect(self.offset_rect, GameObjects.bullets[bullet]):
                bullet_to_delete = bullet
                break
        if bullet_to_delete is not None:
            GameObjects.alive_asteroids -= 1
            bullet_to_delete.kill()
            self.kill()
            del GameObjects.asteroids[self]
            del GameObjects.bullets[bullet_to_delete]

    @property
    def offset_rect(self):
        size = self.image.get_size()
        self.rect.center = (self.x + size[0] / 2, self.y + size[1] / 2)
        return self.rect

    def check_inbounds(self):
        if self.y >= GameObjects.HEIGHT + 66:
            self.y = -33
        if self.y < -66:
            self.y = GameObjects.HEIGHT + 33
        if self.x >= GameObjects.WIDTH + 66:
            self.x = -33
        if self.x < -66:
            self.x = GameObjects.WIDTH + 33
