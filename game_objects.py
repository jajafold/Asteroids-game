import random
import pygame
from src.mouse import Mouse
from src.utils.obj_type import ObjectType


class GameObjects:
    WIDTH = 1200
    HEIGHT = 700
    EVENT_START = 3393
    LEVEL_ONE_ASTEROIDS = 15
    LEVEL_TWO_ASTEROIDS = 20
    LEVEL_THREE_ASTEROIDS = 25

    current_level = 1
    score = 0
    hp = 3
    alive_asteroids = 0
    killed_asteroids_on_level = 0

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
    GameObjects.window.blit(GameObjects.hp_surface, (GameObjects.WIDTH - 40, 20))
    GameObjects.window.blit(GameObjects.font.render(f"Level {GameObjects.current_level}",
                                                    False, (255, 255, 255)), (550, 20))


def get_random_corner():
    a = random.randint(0, 3)
    if a == 0:
        return -20, random.randint(-20, GameObjects.HEIGHT + 20)
    if a == 1:
        return GameObjects.WIDTH + 20, random.randint(-20, GameObjects.HEIGHT + 20)
    if a == 2:
        return random.randint(-20, GameObjects.WIDTH + 20), -20
    return random.randint(-20, GameObjects.WIDTH + 20), GameObjects.HEIGHT + 20


def change_level(a: int):
    if a < 0 or a > 3:
        return True
    GameObjects.current_level = a


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
