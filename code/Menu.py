import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, WIN_HEIGHT, COLOR_GREEN, MENU_OPTION, COLOR_WHITE


class Menu:
    def __init__(self, window):
        self.window = window # Nossa Janela
        self.surf = pygame.image.load("Asset/Battleground1.png") # Nosso background
        self.rect = self.surf.get_rect(left=0, top=0) # Desenhamos um retangulo

    def run(self):
        pygame.mixer_music.load('Asset/Menu.wav')  # adicionando musica ao Menu
        pygame.mixer_music.play(-1)  # A musica vai ficar tocando eternamente


        while True:
            self.window.blit(source=self.surf, dest=self.rect)  # Vai ficar atualizando a imagem dentro do retangulo
            self.menu_text(70, "Zombie", COLOR_GREEN, ((WIN_HEIGHT / 2), 70)) # Adicinando o text no menu
            self.menu_text(70, "Boy", COLOR_GREEN, ((WIN_HEIGHT / 2), 120)) # Adicinando o text no menu

            # Opções do menu
            for i in range(len(MENU_OPTION)):
                self.menu_text(30, MENU_OPTION[i], COLOR_WHITE, ((WIN_HEIGHT / 2), 300 + 30 * i))  # Adicinando o text no menu

            pygame.display.flip()  # Atualiza nosso Display


            #Check for all events
            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    pygame.quit() # fecha a janela
                    quit() # sai do jogo

    def menu_text(self, text_size: int,
                  text: str,
                  text_color: tuple,
                  text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)