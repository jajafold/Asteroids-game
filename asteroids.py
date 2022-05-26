import pygame

import game_objects
from game_objects import GameObjects, update_text, change_level, update_all
from src.asteroid import Asteroid
from src.menu import Menu
from src.ship import Ship
from src.ufo import Ufo
from src.utils.Vector2D import get_random_vector, Vector2D


def main():
    def spawn_ufo():
        point = game_objects.get_random_corner()
        dot_vec = Vector2D(point[0], point[1])
        summa = center - dot_vec
        result = dot_vec + (summa / summa.length) * 100

        GameObjects.ufo_group.add(Ufo(result.x,
                                      result.y,
                                      ship))

    def spawn_asteroid():
        GameObjects.alive_asteroids += 1
        rand_point = game_objects.get_random_corner()
        asteroid = Asteroid(rand_point[0],
                            rand_point[1],
                            get_random_vector() * GameObjects.current_level)
        GameObjects.asteroid_group.add(asteroid)

    level_asteroids = [GameObjects.LEVEL_ONE_ASTEROIDS,
                       GameObjects.LEVEL_TWO_ASTEROIDS, GameObjects.LEVEL_THREE_ASTEROIDS]

    pygame.init()
    clock = pygame.time.Clock()
    ship = Ship()
    main_menu = Menu(True)
    center = Vector2D(GameObjects.WIDTH / 2, GameObjects.HEIGHT / 2)

    GameObjects.unit_group.add(ship)

    run = True
    started = False

    while run:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == GameObjects.EVENT_START:
                started = True

        if not started:
            main_menu.update()
            # pygame.draw.rect(GameObjects.window, (255, 255, 255), GameObjects.mouse.offset_rect, 1)
        else:
            if GameObjects.alive_asteroids < level_asteroids[GameObjects.current_level - 1]:
                if GameObjects.killed_asteroids_on_level == level_asteroids[GameObjects.current_level - 1]:
                    end = change_level(GameObjects.current_level + 1)
                    if end:
                        run = False
                    GameObjects.killed_asteroids_on_level = 0
                    continue
                spawn_asteroid()

            if GameObjects.killed_asteroids_on_level % 5 == 0 and len(GameObjects.ufos) == 0 \
                    and GameObjects.killed_asteroids_on_level != 0:
                spawn_ufo()

            update_text()
            update_all()

            if not ship.alive:
                run = False

        pygame.display.update()
        GameObjects.window.blit(GameObjects.bg, (0, 0))


if __name__ == '__main__':
    main()
