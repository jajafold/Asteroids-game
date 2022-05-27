import random

import pygame

from src.mouse import Mouse
from src.utils.obj_type import ObjectType


class GameObjects:
    WIDTH = 1200
    HEIGHT = 700
    EVENT_START = 3393
    LEVEL_ASTEROIDS = [15, 20, 25]

    current_level = 1
    score = 0
    hp = 3
    alive_asteroids = 0
    killed_asteroids = 0

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
    ufo_group = pygame.sprite.Group()
    bullets = {}
    asteroids = {}
    ufos = {}


def update_text():
    GameObjects.score_surface = GameObjects.font.render(str(GameObjects.score),
                                                        False, (255, 255, 255))
    GameObjects.hp_surface = GameObjects.font.render(str(GameObjects.hp),
                                                     False, (255, 255, 255))
    GameObjects.window.blit(GameObjects.score_surface, (20, 20))
    GameObjects.window.blit(GameObjects.hp_surface,
                            (GameObjects.WIDTH - 40, 20))
    GameObjects.window.blit(GameObjects.font.render
                            (f"Level {GameObjects.current_level}",
                             False, (255, 255, 255)), (550, 20))
    current_level_asteroids \
        = GameObjects.LEVEL_ASTEROIDS[GameObjects.current_level - 1]
    to_complete = current_level_asteroids - GameObjects.killed_asteroids
    need = f"Need to kill {to_complete}"
    GameObjects.window.blit(GameObjects.
                            font.render(need,
                                        False, (255, 255, 255)), (510, 50))


def get_random_corner():
    a = random.randint(0, 3)
    if a == 0:
        return -20, random.randint(-20, GameObjects.HEIGHT + 20)
    if a == 1:
        return GameObjects.WIDTH + \
               20, random.randint(-20, GameObjects.HEIGHT + 20)
    if a == 2:
        return random.randint(-20, GameObjects.WIDTH + 20), -20
    return random.randint(-20, GameObjects.WIDTH + 20), GameObjects.HEIGHT + 20


def change_level(a: int):
    if a < 0 or a > 3:
        return True
    GameObjects.current_level = a


def display_final():
    text_surface = GameObjects.font.render(f"You died!",
                                           False, (255, 255, 255))
    score_surface = GameObjects.font.render(f"Your score is {GameObjects.score}",
                                            False, (255, 255, 255))
    GameObjects.window.blit(text_surface, (530, 320))
    GameObjects.window.blit(score_surface, (500, 360))


def update_all():
    GameObjects.unit_group.update()
    GameObjects.bullets_group.update()
    GameObjects.asteroid_group.update()
    GameObjects.ufo_group.update()

    for el in GameObjects.bullets:
        GameObjects.bullets[el] = el.offset_rect

    for el in GameObjects.asteroids:
        GameObjects.asteroids[el] = el.offset_rect


def detect_collision(obj: pygame.sprite, col_type: ObjectType):
    if col_type == ObjectType.ASTEROID:
        obj_dict = GameObjects.asteroids
    elif col_type == ObjectType.BULLET:
        obj_dict = GameObjects.bullets
    else:
        obj_dict = GameObjects.ufos

    obj_to_delete = None
    for element in obj_dict.keys():
        if pygame.Rect.colliderect(obj.offset_rect,
                                   obj_dict[element]):
            obj_to_delete = element
            break
    return obj_to_delete


def kill_all():
    GameObjects.unit_group.empty()
    GameObjects.ufo_group.empty()
    GameObjects.asteroid_group.empty()
    GameObjects.bullets_group.empty()
    GameObjects.ufos = {}
    GameObjects.asteroids = {}
    GameObjects.bullets = {}
