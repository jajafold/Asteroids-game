import pygame
from game_objects import GameObjects


class Bullet():
    VELOCITY_CONST = 50

    def __init__(self, x, y, velocity):
        self.x = x
        self.y = y
        self.bullet_image = pygame.image.load("bullet.png")
        self.velocity = velocity * Bullet.VELOCITY_CONST
        self.rect = self.bullet_image.get_rect()

        GameObjects.bullets[self] = self.offset_rect

    def update(self):
        self.x += self.velocity.x
        self.y += self.velocity.y

        GameObjects.window.blit(self.bullet_image, (self.x, self.y))


    @property
    def offset_rect(self):
        size = self.bullet_image.get_size()
        self.rect.center = (self.x + size[0] / 2, self.y + size[1] / 2)
        return self.rect
