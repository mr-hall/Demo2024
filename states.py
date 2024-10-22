import pygame
import constants
import extra


class State():
    #parent class for states default behaviour
    def __init__(self):
        pass
        self.next_state = None

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
        self.buttons = []
        button1 = extra.Button(10,10, "play", "play")
        self.buttons.append(button1)
        button2 = extra.Button(10,40, "quit", "quit")
        self.buttons.append(button2)
    def input(self, event):
        #handles key presses
        if event.type == pygame.KEYDOWN:
            pass
        if event.type == pygame.MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            for button in self.buttons:
                button.check_hover(pos)
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            for button in self.buttons:
                dest = button.click(pos)
                if dest:
                    self.next_state = dest


    def render(self, window):
        #draw frame
        window.fill(constants.MENU_BACKGROUND)
        for button in self.buttons:
            pygame.draw.rect(window,button.colour, [button.rect.x, button.rect.y, button.rect.width, button.rect.height])
            window.blit(button.text_image, (button.rect.x, button.rect.y))

class Game(State):
    def __init__(self):
        super().__init__()
        self.player = extra.Player()
        self.enemies = pygame.sprite.Group()
        for i in range(10):
            enemy = extra.Enemy()
            self.enemies.add(enemy)

    def render(self, window):
        # draw frame
        window.fill((255,255,255))
        window.blit(self.player.image, self.player.rect)
        self.enemies.draw(window)

    def update(self):
        self.enemies.update()
        pygame.sprite.spritecollide(self.player, self.enemies, True)
