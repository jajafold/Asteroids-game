import pygame

class GameConsts:
    WIDTH = 1200
    HEIGHT = 700
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Asteroids")
    bg = pygame.image.load('bg.png')
    units = []