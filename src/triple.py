import pygame

import src.item
from game_objects import GameObjects


class Triplet(src.item.Item):
    def __init__(self, x, y, ship):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.ship = ship
        self.image = pygame.image.load("img/ship.png")
        self.rect = self.image.get_rect()

        GameObjects.items_group.add(self)
        GameObjects.items[self] = self.offset_rect

    def update(self):
        GameObjects.window.blit(self.image, (self.x, self.y))

    def use(self):
        self.ship.triple_bullets = 10
        self.kill()
        del GameObjects.items[self]

    @property
    def offset_rect(self):
        size = self.image.get_size()
        self.rect.center = (self.x + size[0] / 2, self.y + size[1] / 2)
        return self.rect
