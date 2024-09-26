import pygame
import constants

class State():
    def __init__(self):
        pass

    def input(self, event):
        pass

    def update(self):
        pass

    def render(self, window):
        pass
class Menu(State):
    def __init__(self):
        super().__init__()

    def input(self, event):
        if event.type == pygame.KEYDOWN:
            pass

    def render(self, window):
        window.fill(constants.MENU_BACKGROUND)

