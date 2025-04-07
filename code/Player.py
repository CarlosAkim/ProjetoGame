import pygame
from code.Const import SPEED_PLAYER, WIN_WIDTH, WIN_HEIGHT, PLAYER_KEY_CUT, ENTITY_SHOT_DELAY
from code.Entity import Entity
from code.PlayerCut import PlayerCut


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

        self.cutDelay = ENTITY_SHOT_DELAY[self.name]

        # Lista de sprites do personagem
        self.sprites = [
            pygame.image.load("Asset/PlayerRunning0.png"),
            pygame.image.load("Asset/PlayerRunning1.png"),
            pygame.image.load("Asset/PlayerRunning2.png"),
            pygame.image.load("Asset/PlayerRunning3.png"),
            pygame.image.load("Asset/PlayerRunning4.png"),

        ]

        self.current_sprite = 0  # Índice do sprite atual
        self.image = self.sprites[self.current_sprite]
        self.last_update = pygame.time.get_ticks()  # Tempo da última troca de sprite
        self.animation_delay = 40  # Tempo de troca de sprite (1 segundo)

    def update(self):
        self.move()
        self.animate()

    def move(self):
        pressed_key = pygame.key.get_pressed()
        moved = False  # Flag para verificar se o personagem se moveu

        if pressed_key[pygame.K_UP] and self.rect.top > 125:
            self.rect.centery -= SPEED_PLAYER[self.name]
            moved = True
        if pressed_key[pygame.K_DOWN] and self.rect.bottom < WIN_WIDTH:
            self.rect.centery += SPEED_PLAYER[self.name]
            moved = True
        if pressed_key[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.centerx -= SPEED_PLAYER[self.name]
            moved = True
        if pressed_key[pygame.K_RIGHT] and self.rect.right < WIN_HEIGHT:
            self.rect.centerx += SPEED_PLAYER[self.name]
            moved = True

        if moved:
            self.animate()

    def animate(self):
        """Troca o sprite a cada 1 segundo"""
        now = pygame.time.get_ticks()
        if now - self.last_update > self.animation_delay:
            self.last_update = now
            self.current_sprite = (self.current_sprite + 1) % len(self.sprites)
            self.image = self.sprites[self.current_sprite]
            self.surf = self.image

    def cut(self):
        self.cutDelay -= 1
        if self.cutDelay == 0:
            self.cutDelay = ENTITY_SHOT_DELAY[self.name]
            pressed_key = pygame.key.get_pressed()
            if pressed_key[PLAYER_KEY_CUT[self.name]]:
                return PlayerCut(name=f'{self.name}Attack', position=(self.rect.centerx, self.rect.centery))