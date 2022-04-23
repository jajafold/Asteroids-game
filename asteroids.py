import pygame

import game_objects
from ship import Ship
from game_objects import GameObjects
from asteroid import Asteroid
from Vector2D import get_random_vector


def main():
    pygame.init()
    clock = pygame.time.Clock()
    GameObjects.units.append(Ship())

    run = True

    while run:
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        if GameObjects.alive_asteroids < GameObjects.MAX_ASTEROIDS:
            GameObjects.alive_asteroids += 1
            rand_point = game_objects.get_random_corner()
            GameObjects.units.append(Asteroid(rand_point[0], rand_point[1], get_random_vector()))

        for el in GameObjects.units:
            el.update()
        
        pygame.display.update()
        GameObjects.window.blit(GameObjects.bg, (0, 0))


if __name__ == '__main__':
    main()
