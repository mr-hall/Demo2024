import pygame
import constants

window = pygame.display.set_mode((constants.WIDTH,constants.HEIGHT))

window.fill(constants.MENU_BACKGROUND)
running = True
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()