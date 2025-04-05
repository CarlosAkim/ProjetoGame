import pygame

from code.Const import SPEED_ENEMY, WIN_HEIGHT
from code.Entity import Entity

class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        # Lista de sprites do personagem
        self.sprites = [
            pygame.image.load(f"Asset/Enemy{i}.png") for i in range(12)

        ]

    def move(self):
        self.rect.centerx -= SPEED_ENEMY[self.name]
