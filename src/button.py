import pygame
from game_objects import GameObjects


class Button(pygame.sprite.Sprite):

    def __init__(self, x, y, label: str, font: pygame.font.Font):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.label = label
        self.size = font.size(label)
        self.rect = pygame.rect.Rect((0, 0), (self.size[0], self.size[1]))

    def update(self):
        if pygame.Rect.colliderect(self.offset_rect, GameObjects.mouse.offset_rect) \
                and GameObjects.mouse.pressed:
            self.on_click()

    def on_click(self):
        raise Exception('Pure virtual method called!')

    def on_selected(self):
        pass

    @property
    def offset_rect(self):
        self.rect.center = (self.x + self.size[0] / 2, self.y + self.size[1] / 2)
        return self.rect
