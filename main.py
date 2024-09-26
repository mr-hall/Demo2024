import pygame
import constants
import states

window = pygame.display.set_mode((constants.WIDTH,constants.HEIGHT))
running = True
current_state = states.Menu()
clock = pygame.time.Clock()
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        else:
            current_state.input(event)
    current_state.update()
    current_state.render(window)
    pygame.display.flip()
    clock.tick(constants.FPS)