import pygame

import game_objects
from src.ship import Ship
from game_objects import GameObjects, update_text
from src.asteroid import Asteroid
from src.utils.Vector2D import get_random_vector

 
def main():
    pygame.init()
    clock = pygame.time.Clock()
    ship = Ship()
    GameObjects.unit_group.add(ship)

    run = True

    while run:
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        if GameObjects.alive_asteroids < GameObjects.MAX_ASTEROIDS:
            GameObjects.alive_asteroids += 1
            rand_point = game_objects.get_random_corner()
            asteroid = Asteroid(rand_point[0],
                                rand_point[1],
                                get_random_vector())
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
