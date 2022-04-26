import pygame
from game_objects import GameObjects


class Bullet(pygame.sprite.Sprite):
    VELOCITY_CONST = 20

    def __init__(self, x, y, velocity):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.bullet_image = pygame.image.load("img/bullet.png")
        self.velocity = velocity * Bullet.VELOCITY_CONST
        self.rect = self.bullet_image.get_rect()

        GameObjects.bullets_group.add(self)
        GameObjects.bullets[self] = self.offset_rect

    def update(self):
        self.x += self.velocity.x
        self.y += self.velocity.y

        GameObjects.window.blit(self.bullet_image, (self.x, self.y))
    
    def check_inbounds(self):
        if not self.is_inbounds:
            self.kill()
    
    @property
    def is_inbounds(self):
        return self.y >= GameObjects.HEIGHT + 66 or self.y < -66 or self.x >= GameObjects.WIDTH + 66 or self.x < -66

    @property
    def offset_rect(self):
        size = self.bullet_image.get_size()
        self.rect.center = (self.x + size[0] / 2, self.y + size[1] / 2)
        return self.rect
