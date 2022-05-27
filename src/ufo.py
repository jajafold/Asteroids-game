from random import randint

import pygame

from game_objects import GameObjects, detect_collision
from src.bullet import Bullet
from src.heal import Heal
from src.ship import Ship
from src.triple import Triplet
from src.utils.Vector2D import Vector2D
from src.utils.obj_type import ObjectType


class Ufo(pygame.sprite.Sprite):
    skin = "img/enemy.png"
    UFO_ATTACK_DELAY = 100

    def __init__(self, x, y, ship: Ship):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.image = pygame.image.load(Ufo.skin)
        self.rect = self.image.get_rect()
        self.delay = 0
        self.ship = ship

        GameObjects.ufos[self] = self.offset_rect

    def update(self):
        self.detect_collision()
        if self.delay < Ufo.UFO_ATTACK_DELAY:
            self.delay += 1
        else:
            self.shoot()

        GameObjects.window.blit(self.image, (self.x, self.y))

    def shoot(self):
        direction = Vector2D(self.ship.x - self.x, self.ship.y - self.y)
        direction /= direction.length
        Bullet(
            self.x +
            direction.x *
            50,
            self.y +
            direction.y *
            50,
            direction /
            direction.length)
        self.delay = 0

    def detect_collision(self):
        collided_bullet = detect_collision(self, ObjectType.BULLET)
        if collided_bullet is not None:
            GameObjects.score += 50
            collided_bullet.kill()
            self.kill()
            if randint(0, 1):
                Heal(self.x, self.y, self.ship)
            else:
                Triplet(self.x, self.y, self.ship)
            del GameObjects.ufos[self]
            del GameObjects.bullets[collided_bullet]
        return collided_bullet

    @property
    def offset_rect(self):
        size = self.image.get_size()
        self.rect.center = (self.x + size[0] / 2, self.y + size[1] / 2)
        return self.rect
