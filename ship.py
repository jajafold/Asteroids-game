import math
import pygame
from Vector2D import Vector2D
from bullet import Bullet
from game_objects import GameObjects


class Ship(pygame.sprite.Sprite):
    SHOOT_DELAY = 10
    ACCELERATION = 1
    REVERSE_ACCELERATION = -0.05
    MAX_VELOCITY = 15
    ROTATION_ANGLE = math.pi/18

    angle = 0

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.x = 500
        self.y = 500
        self.ship_image = pygame.image.load('ship.png')
        self.rect = self.ship_image.get_rect()

        self.direction = Vector2D(0, -1)
        self.velocity = Vector2D(0, 0)
        self.SHOOT_DELAY = Ship.SHOOT_DELAY
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

    def detect_collision(self):
        for asteroid in GameObjects.asteroids.keys():
            if pygame.Rect.colliderect(self.offset_rect, GameObjects.asteroids[asteroid]):
                self.kill()
                self.alive = False
    
    def fire(self):
        keys = pygame.key.get_pressed()

        if not self.can_shoot:
            self.SHOOT_DELAY -= 1
        
        if self.SHOOT_DELAY <= 0:
            self.can_shoot = True
            
        if keys[pygame.K_SPACE] and self.can_shoot:
            Bullet(self.x + self.direction.x, self.y + self.direction.y, self.direction)
            self.can_shoot = False
            self.SHOOT_DELAY = Ship.SHOOT_DELAY

    def rotate(self):
        rotated = self.rot_center(self.angle)
        GameObjects.window.blit(rotated[0], (rotated[1].x, rotated[1].y))

    def rot_center(self, angle):
        rotated_image = pygame.transform.rotate(self.ship_image, angle)
        new_rect = rotated_image.get_rect(center=self.ship_image.get_rect(center=(self.x, self.y)).center)

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