import pygame
import constants

class State():
    #parent class for states default behaviour
    def __init__(self):
        pass

    def input(self, event):
        pass

    def update(self):
        pass

    def render(self, window):
        pass
class Menu(State):
    #main menu state
    def __init__(self):
        super().__init__()

    def input(self, event):
        #handles key presses
        if event.type == pygame.KEYDOWN:
            pass

    def render(self, window):
        #draw frame
        window.fill(constants.MENU_BACKGROUND)

