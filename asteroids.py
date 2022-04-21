import pygame
from Vector2D import *
from ship import *

WIDTH = 1200
HEIGHT = 700

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("noname_game")
bg = pygame.image.load('bg.png')
units = []

def main():
    global window
    global units

    pygame.init()
    clock = pygame.time.Clock()
    units.append(Ship())

    run = True

    while run:
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for el in units:
            el.update()
        
        pygame.display.update()
        window.blit(bg, (0, 0))

if __name__ == '__main__':
    main()