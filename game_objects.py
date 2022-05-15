import random
import pygame
from src.mouse import Mouse


class GameObjects:
    WIDTH = 1200
    HEIGHT = 700
    MAX_ASTEROIDS = 15
    EVENT_START = 3393

    score = 0
    hp = 3
    alive_asteroids = 0

    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.font.init()
    font = pygame.font.SysFont("Impact", 30)
    score_surface = font.render(str(score), False, (255, 255, 255))
    hp_surface = font.render(str(hp), False, (255, 255, 255))
    pygame.display.set_caption("Asteroids")
    bg = pygame.image.load('img/bg.png')
    mouse = Mouse()

    unit_group = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()
    bullets_group = pygame.sprite.Group()
    bullets = {}
    asteroids = {}


def update_text():
    GameObjects.score_surface = GameObjects.font.render(str(GameObjects.score),
                                                        False, (255, 255, 255))
    GameObjects.hp_surface = GameObjects.font.render(str(GameObjects.hp),
                                                     False, (255, 255, 255))
    GameObjects.window.blit(GameObjects.score_surface, (20, 20))
    GameObjects.window.blit(GameObjects.hp_surface, (GameObjects.WIDTH-40, 20))


def get_random_corner():
    a = random.randint(0, 3)
    if a == 0:
        return -20, random.randint(-20, GameObjects.HEIGHT + 20)
    if a == 1:
        return GameObjects.WIDTH + 20, random.randint(-20, GameObjects.HEIGHT + 20)
    if a == 2:
        return random.randint(-20, GameObjects.WIDTH + 20), -20
    return random.randint(-20, GameObjects.WIDTH + 20), GameObjects.HEIGHT + 20
