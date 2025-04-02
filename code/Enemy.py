from code.Const import SPEED_ENEMY, WIN_HEIGHT
from code.Entity import Entity

class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        pass

    def move(self):
        self.rect.centerx -= SPEED_ENEMY[self.name]
        if self.rect.right <= 0:
            self.rect.left = WIN_HEIGHT