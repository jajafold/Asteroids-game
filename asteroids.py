import pygame

import game_objects
from src.ship import Ship
from game_objects import GameObjects, update_text, change_level
from src.asteroid import Asteroid
from src.utils.Vector2D import get_random_vector
from src.menu import Menu


def main():
    level_asteroids = [GameObjects.LEVEL_ONE_ASTEROIDS,
                       GameObjects.LEVEL_TWO_ASTEROIDS, GameObjects.LEVEL_THREE_ASTEROIDS]

    pygame.init()
    clock = pygame.time.Clock()
    ship = Ship()
    main_menu = Menu(True)

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
                    change_level(GameObjects.current_level + 1)
                    GameObjects.killed_asteroids_on_level = 0
                    continue
                GameObjects.alive_asteroids += 1
                rand_point = game_objects.get_random_corner()
                asteroid = Asteroid(rand_point[0],
                                    rand_point[1],
                                    get_random_vector() * GameObjects.current_level)
                GameObjects.asteroid_group.add(asteroid)

            update_text()

            if not ship.alive:
                run = False

            GameObjects.unit_group.update()
            GameObjects.bullets_group.update()
            GameObjects.asteroid_group.update()

            for el in GameObjects.bullets:
                GameObjects.bullets[el] = el.offset_rect

            for el in GameObjects.asteroids:
                GameObjects.asteroids[el] = el.offset_rect

        pygame.display.update()
        GameObjects.window.blit(GameObjects.bg, (0, 0))


if __name__ == '__main__':
    main()
