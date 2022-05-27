import pygame


class Item(pygame.sprite.Sprite):
    def use(self):
        raise AttributeError("Shouldn't use this method in this scope")
