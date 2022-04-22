import math
import pygame
from Vector2D import Vector2D
from bullet import Bullet
from game import Game


class Ship:
    acceleration = 1
    reverse_acceleration = -0.05
    maxVelocity = 15
    angle = 0

    ROTATION_ANGLE = math.pi/18

    position = Vector2D(0, 0)

    def __init__(self, game: Game):
        self.x = 500
        self.y = 500
        self.ship_image = pygame.image.load('ship.png')
        self.direction = Vector2D(0, -1)
        self.velocity = Vector2D(0, 0)
        self.game = game

    def update(self): 
        self.move()
        self.check_inbounds()
        if self.velocity.length > self.maxVelocity:
            self.velocity /= self.velocity.length
            self.velocity *= self.maxVelocity

        self.x += self.velocity.x
        self.y += self.velocity.y

        self.rotate()

    def rotate(self):
        self.rotated = self.rot_center(self.angle)
        self.game.window.blit(self.rotated[0], (self.rotated[1].x, self.rotated[1].y))

    def rot_center(self, angle):
        rotated_image = pygame.transform.rotate(self.ship_image, angle)
        new_rect = rotated_image.get_rect(center=self.ship_image.get_rect(center=(self.x, self.y)).center)

        return rotated_image, new_rect

    def move(self):
        self.keys = pygame.key.get_pressed()

        if self.keys[pygame.K_a]:
            self.direction = self.direction.rotate(angle = -self.ROTATION_ANGLE)
            self.angle += 10

        if self.keys[pygame.K_d]:
            self.direction = self.direction.rotate(angle = self.ROTATION_ANGLE)
            self.angle -= 10

        if self.keys[pygame.K_s] and self.y <= Game.HEIGHT:
            self.velocity -= self.direction * self.acceleration

        if self.keys[pygame.K_w] and self.y >= 0:
            self.velocity += self.direction * self.acceleration
        
        if self.keys[pygame.K_SPACE]:
            self.game.units.append(Bullet(self.x + self.velocity.x * 5, self.y + self.velocity.y * 5, self.velocity))
    
    def check_inbounds(self):
        if self.y >= Game.HEIGHT + 66:
            self.y = -33
        if self.y < -66:
            self.y = Game.HEIGHT + 33
        if self.x >= Game.WIDTH + 66:
            self.x = -33
        if self.x < -66:
            self.x = Game.WIDTH + 33
