from game_objects import GameObjects, detect_bullet
from src.bullet import Bullet
from src.ship import Ship
from src.utils.Vector2D import Vector2D
import pygame


class Ufo(pygame.sprite.Sprite):
    skin = "img/enemy.png"
    UFO_ATTACK_DELAY = 100

    def __init__(self, x, y, ship: Ship):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.image = pygame.image.load(Ufo.skin)
        self.rect = self.image.get_bounding_rect()
        self.delay = 0
        self.ship = ship

        print(f"spawned on {self.x} {self.y}")
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
        Bullet(self.x + direction.x * 50, self.y + direction.y * 50, direction/direction.length)
        self.delay = 0

    def detect_collision(self):
        collision = detect_bullet(self)
        if collision is not None:
            GameObjects.score += 50
            collision.kill()
            self.kill()
            del GameObjects.ufos[self]
            del GameObjects.bullets[collision]

    @property
    def offset_rect(self):
        size = self.image.get_size()
        self.rect.center = (self.x + size[0] / 2, self.y + size[1] / 2)
        return self.rect
