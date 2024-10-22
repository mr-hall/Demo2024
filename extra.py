import random

import pygame

import constants
from constants import BUTTON_HOVER, BUTTON_NORMAL, FONT, BLACK

class Button:

    def __init__(self, x, y, dest, text):
        self.text_image = FONT.render(text, True, BLACK)
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


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/enemyGreen3.png").convert()
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0,constants.WIDTH)
        self.rect.y = random.randint(0,constants.HEIGHT)

    def update(self):
        self.rect.y = self.rect.y - 1

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/playerShip1_blue.png").convert()
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x =250
        self.rect.y =250




