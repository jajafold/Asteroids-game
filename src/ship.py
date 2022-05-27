import math

import pygame

from game_objects import GameObjects, detect_collision
from src.bullet import Bullet
from src.utils.Vector2D import Vector2D
from src.utils.obj_type import ObjectType


class Ship(pygame.sprite.Sprite):
    delay = 10
    ACCELERATION = 0.5
    REVERSE_ACCELERATION = -0.05
    MAX_VELOCITY = 15
    ROTATION_ANGLE = math.pi / 18

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.x = 500
        self.y = 500
        self.ship_image = pygame.image.load('img/ship.png')
        self.rect = self.ship_image.get_rect()
        self.angle = 0
        self.hp = GameObjects.hp

        self.direction = Vector2D(0, -1)
        self.velocity = Vector2D(0, 0)
        self.delay = Ship.delay
        self.can_shoot = True
        self.alive = True

    def update(self):
        self.move()
        self.fire()
        self.detect_collision()
        self.check_inbounds()
        if self.velocity.length > self.MAX_VELOCITY:
            self.velocity /= self.velocity.length
            self.velocity *= self.MAX_VELOCITY

        self.x += self.velocity.x
        self.y += self.velocity.y

        self.rotate()
        self.check_dead()

    def detect_collision(self):
        collided_bullet = detect_collision(self, ObjectType.BULLET)
        if collided_bullet is not None:
            collided_bullet.kill()
            del GameObjects.bullets[collided_bullet]
            self.hp -= 1
            GameObjects.hp -= 1

        collided_asteroid = detect_collision(self, ObjectType.ASTEROID)
        if collided_asteroid is not None:
            del GameObjects.asteroids[collided_asteroid]
            collided_asteroid.kill()
            self.hp -= 1
            GameObjects.killed_asteroids += 1
            GameObjects.hp -= 1

        return collided_bullet, collided_asteroid

    def check_dead(self):
        if self.hp == 0:
            self.kill()
            self.alive = False

    def fire(self):
        keys = pygame.key.get_pressed()

        if not self.can_shoot:
            self.delay -= 1

        if self.delay <= 0:
            self.can_shoot = True

        if keys[pygame.K_SPACE] and self.can_shoot:
            Bullet(self.x + self.direction.x * 45,
                   self.y + self.direction.y * 45, self.direction)
            self.can_shoot = False
            self.delay = Ship.delay

    def rotate(self):
        rotated = self.rot_center(self.angle)
        GameObjects.window.blit(rotated[0], (rotated[1].x, rotated[1].y))

    def rot_center(self, angle):
        rotated_image = pygame.transform.rotate(self.ship_image, angle)
        image_center = self.ship_image.get_rect(center=(self.x, self.y)).center
        new_rect = rotated_image.get_rect(center=image_center)

        return rotated_image, new_rect

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.direction = self.direction.rotate(angle=-self.ROTATION_ANGLE)
            self.angle += 10

        if keys[pygame.K_d]:
            self.direction = self.direction.rotate(angle=self.ROTATION_ANGLE)
            self.angle -= 10

        if keys[pygame.K_s] and self.y <= GameObjects.HEIGHT:
            self.velocity -= self.direction * self.ACCELERATION

        if keys[pygame.K_w] and self.y >= 0:
            self.velocity += self.direction * self.ACCELERATION

    def check_inbounds(self):
        if self.y >= GameObjects.HEIGHT + 66:
            self.y = -33
        if self.y < -66:
            self.y = GameObjects.HEIGHT + 33
        if self.x >= GameObjects.WIDTH + 66:
            self.x = -33
        if self.x < -66:
            self.x = GameObjects.WIDTH + 33

    @property
    def offset_rect(self):
        size = self.ship_image.get_size()
        self.rect.center = (self.x + size[0] / 2, self.y + size[1] / 2)
        return self.rect
