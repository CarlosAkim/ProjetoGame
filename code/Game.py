import pygame

from code.Const import WIN_HEIGHT, WIN_WIDTH
from code.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_HEIGHT, WIN_WIDTH))

    def run(self):

        while True:
            menu = Menu(self.window)
            menu.run()

