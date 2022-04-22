import pygame
from ship import Ship


class Game:
    HEIGHT = 700
    WIDTH = 1200

    def __init__(self):
        self.window = pygame.display.set_mode((Game.WIDTH, Game.HEIGHT))
        pygame.display.set_caption("noname_game")
        self.bg = pygame.image.load('bg.png')
        self.units = []

    def play(self):
        pygame.init()
        clock = pygame.time.Clock()
        self.units.append(Ship(self))

        run = True

        while run:
            clock.tick(30)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            for el in self.units:
                el.update()
        
            pygame.display.update()
            self.window.blit(self.bg, (0, 0))