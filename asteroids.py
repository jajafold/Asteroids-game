import pygame

import game_objects
from game_objects import GameObjects, update_text, change_level, update_all, kill_all, display_final
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

    level_asteroids = GameObjects.LEVEL_ASTEROIDS

    pygame.init()
    pygame.mixer.music.load("snd/menu.mp3")
    pygame.mixer.music.play()
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
                pygame.mixer.music.load("snd/gameplay.mp3")
                pygame.mixer.music.play()
                started = True

        if not started:
            main_menu.update()
        else:
            if GameObjects.alive_asteroids <\
                    level_asteroids[GameObjects.current_level - 1]:
                if GameObjects.killed_asteroids >= level_asteroids[
                        GameObjects.current_level - 1]:
                    end = change_level(GameObjects.current_level + 1)
                    if end:
                        run = False
                    GameObjects.killed_asteroids = 0
                    continue
                spawn_asteroid()

            if GameObjects.killed_asteroids % 5 == 0\
                    and len(GameObjects.ufos) == 0 \
                    and GameObjects.killed_asteroids != 0:
                spawn_ufo()

            if not ship.alive:
                kill_all()
                display_final()
                return 0
            else:
                update_text()
                update_all()

        pygame.display.update()
        GameObjects.window.blit(GameObjects.bg, (0, 0))


if __name__ == '__main__':
    main()
