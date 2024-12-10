import pygame
import constants
import states

# initialising
window = pygame.display.set_mode((constants.WIDTH,constants.HEIGHT))
running = True
current_state = states.Menu()
clock = pygame.time.Clock()


# game loop
while running:

    # handling events
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        else:
            current_state.input(event)

    #updates
    current_state.update()

    #drawing
    current_state.render(window)
    pygame.display.flip()

    #clock tick
    clock.tick(constants.FPS)

    if current_state.next_state:
        if current_state.next_state == "quit":
            running = False
        elif current_state.next_state =="play":
            current_state = states.Game()