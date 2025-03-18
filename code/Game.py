import pygame

from code.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(848, 477))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu.run()

