
import math
import pygame
from Vector2D import Vector2D
from bullet import Bullet
from game_objects import GameConsts

class Ship:
    shoot_delay = 10
    acceleration = 1
    reverse_acceleration = -0.05
    maxVelocity = 15
    angle = 0
    
    ROTATION_ANGLE = math.pi/18

    def __init__(self):
        self.x = 500
        self.y = 500
        self.ship_image = pygame.image.load('ship.png')
        self.direction = Vector2D(0, -1)
        self.velocity = Vector2D(0, 0)
        self.shoot_delay = Ship.shoot_delay
        self.can_shoot = True

    def update(self): 
        self.move()
        self.fire()
        self.check_inbounds()
        if self.velocity.length > self.maxVelocity:
            self.velocity /= self.velocity.length
            self.velocity *= self.maxVelocity

        self.x += self.velocity.x
        self.y += self.velocity.y

        self.rotate()
    
    def fire(self):
        keys = pygame.key.get_pressed()

        if not self.can_shoot:
            self.shoot_delay -= 1
        
        if self.shoot_delay <= 0:
            self.can_shoot = True
            
        if keys[pygame.K_SPACE] and self.can_shoot:
            GameConsts.units.append(Bullet(self.x + self.direction.x, self.y + self.direction.y, self.direction))
            self.can_shoot = False
            self.shoot_delay = Ship.shoot_delay

    def rotate(self):
        self.rotated = self.rot_center(self.angle)
        GameConsts.window.blit(self.rotated[0], (self.rotated[1].x, self.rotated[1].y))

    def rot_center(self, angle):
        rotated_image = pygame.transform.rotate(self.ship_image, angle)
        new_rect = rotated_image.get_rect(center=self.ship_image.get_rect(center=(self.x, self.y)).center)

        return rotated_image, new_rect

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.direction = self.direction.rotate(angle = -self.ROTATION_ANGLE)
            self.angle += 10

        if keys[pygame.K_d]:
            self.direction = self.direction.rotate(angle = self.ROTATION_ANGLE)
            self.angle -= 10

        if keys[pygame.K_s] and self.y <= GameConsts.HEIGHT:
            self.velocity -= self.direction * self.acceleration

        if keys[pygame.K_w] and self.y >= 0:
            self.velocity += self.direction * self.acceleration
    
    def check_inbounds(self):
        if self.y >= GameConsts.HEIGHT + 66:
            self.y = -33
        if self.y < -66:
            self.y = GameConsts.HEIGHT + 33
        if self.x >= GameConsts.WIDTH + 66:
            self.x = -33
        if self.x < -66:
            self.x = GameConsts.WIDTH + 33
