import pygame
from constants import BUTTON_HOVER, BUTTON_NORMAL

class Button:

    def __init__(self, x, y, dest):
        self.rect = pygame.Rect(x, y, 100, 20)
        self.colour = BUTTON_NORMAL
        self.dest = dest

    def check_hover(self, pos):
        if self.check_if_inside(pos):
            self.colour = BUTTON_HOVER
        else:
            self.colour = BUTTON_NORMAL

    def check_if_inside(self, pos):
        if self.rect.collidepoint(pos[0], pos[1]):
            return True
        else:
            return False

    def click(self, pos):
        if self.check_if_inside(pos):
            return self.dest
