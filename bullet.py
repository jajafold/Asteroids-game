import pygame

class Bullet:
    VELOCITY_CONST = 5
    def __init__(self, x, y, velocity, game):
        self.x = x
        self.y = y
        self.bullet_image = pygame.image.load("bullet.png")
        self.velocity = velocity * Bullet.VELOCITY_CONST
        self.game = game
        game.units.append(self)

    def update(self):
        print("here")
        self.x += self.velocity.x
        self.y += self.velocity.y