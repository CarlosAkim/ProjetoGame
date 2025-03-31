import pygame.key

from code.Const import SPEED_PLAYER, WIN_WIDTH, WIN_HEIGHT
from code.Entity import Entity


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        ...

    def update(self):
        ...

    def move(self):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_UP] and self.rect.top > 125:
            self.rect.centery -= SPEED_PLAYER[self.name]
        if pressed_key[pygame.K_DOWN] and self.rect.bottom  < WIN_WIDTH:
            self.rect.centery += SPEED_PLAYER[self.name]
        if pressed_key[pygame.K_LEFT] and self.rect.left  > 0:
            self.rect.centerx -= SPEED_PLAYER[self.name]
        if pressed_key[pygame.K_RIGHT] and self.rect.right  < WIN_HEIGHT:
            self.rect.centerx += SPEED_PLAYER[self.name]