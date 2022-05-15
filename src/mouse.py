import pygame


class Mouse:

    @property
    def offset_rect(self):
        pos = pygame.mouse.get_pos()
        x, y = pos[0], pos[1]
        rect = pygame.Rect(x - 5, y - 5, 15, 15)

        return rect

    @property
    def pressed(self):
        pressed = pygame.mouse.get_pressed()
        if pressed[0]:
            return True
