import pygame

from game_objects import GameObjects
from src.button import Button


class Start_Button(Button):

    def __init__(self, x, y, label: str, font: pygame.font.Font):
        super().__init__(x, y, label, font)

    def on_click(self):
        pygame.event.post(pygame.event.Event(GameObjects.EVENT_START))


class Exit_Button(Button):

    def __init__(self, x, y, label: str, font: pygame.font.Font):
        super().__init__(x, y, label, font)

    def on_click(self):
        pygame.event.post(pygame.event.Event(pygame.QUIT))


class Menu:
    UNSELECTED_SIZE = 50
    SELECTED_SIZE = 64

    def __init__(self, show):
        self.show = show
        self.buttons = []
        pygame.font.init()

        self.font_btn_unselected = pygame.font.SysFont(
            "Impact", Menu.UNSELECTED_SIZE)
        self.font_btn_selected = pygame.font.SysFont(
            "Impact", Menu.SELECTED_SIZE)
        self.font_game_name = pygame.font.SysFont("Courier New", 142)

        # region Buttons
        self.start_btn = Start_Button(
            GameObjects.WIDTH / 2 - 50,
            350,
            "Start",
            self.font_btn_unselected)
        self.buttons.append(self.start_btn)

        self.exit_btn = Exit_Button(
            GameObjects.WIDTH / 2 - 50,
            450,
            "Exit",
            self.font_btn_unselected)
        self.buttons.append(self.exit_btn)
        # endregion

        # self.renderer = [self.font_unselected.render(button) for button in self.buttons]

    def update(self):
        if not self.show:
            return

        render = self.font_game_name.render(
            "Asteroids", False, (255, 255, 255))
        GameObjects.window.blit(render, (220, 100))

        for btn in self.buttons:
            render = self.font_btn_unselected.render(
                btn.label, False, (255, 255, 255))
            GameObjects.window.blit(render, (btn.x, btn.y))
            # pygame.draw.rect(GameObjects.window, (255, 255, 255), btn.offset_rect, 1)
            btn.update()
