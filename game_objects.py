import random
import pygame


class GameObjects:
    WIDTH = 1200
    HEIGHT = 700
    MAX_ASTEROIDS = 10
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Asteroids")
    bg = pygame.image.load('bg.png')
    unit_group = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()
    bullets_group = pygame.sprite.Group()
    bullets = {}
    asteroids = {}
    alive_asteroids = 0


def get_random_corner():
    a = random.randint(0, 3)
    if a == 0:
        return 0, random.randint(0, GameObjects.HEIGHT)
    if a == 1:
        return GameObjects.WIDTH, random.randint(0, GameObjects.HEIGHT)
    if a == 2:
        return random.randint(0, GameObjects.WIDTH), 0
    return random.randint(0, GameObjects.WIDTH), GameObjects.HEIGHT
