import pygame
from ship import Ship
from game_objects import GameConsts

def main():
    pygame.init()
    clock = pygame.time.Clock()
    GameConsts.units.append(Ship())

    run = True

    while run:
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for el in GameConsts.units:
            el.update()
        
        pygame.display.update()
        GameConsts.window.blit(GameConsts.bg, (0, 0))


if __name__ == '__main__':
    main()