import pygame

from code.Const import SPEED_ENEMY, WIN_HEIGHT
from code.Entity import Entity

class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        # Lista de sprites do personagem
        if self.name == 'Enemy1':
            self.sprites = [
                pygame.image.load(f"Asset/Enemy{i}.png") for i in range(12)

            ]
        elif self.name == 'Enemy2':
            self.sprites = [
                pygame.image.load(f"Asset/Enemy2/Enemy{i}.png") for i in range(12)

            ]
        self.current_sprite = 0  # Índice do sprite atual
        self.image = self.sprites[self.current_sprite]
        self.last_update = pygame.time.get_ticks()  # Tempo da última troca de sprite
        self.animation_delay = 40  # Tempo de troca de sprite (1 segundo)

    def update(self):
        self.move()
        self.animate()


    def animate(self):
        """Troca o sprite a cada 1 segundo"""
        now = pygame.time.get_ticks()
        if now - self.last_update > self.animation_delay:
            self.last_update = now
            self.current_sprite = (self.current_sprite + 1) % len(self.sprites)
            self.surf = self.sprites[self.current_sprite]

    def move(self):
        self.rect.centerx -= SPEED_ENEMY[self.name]
        moved = True
        if moved:
            self.animate()
