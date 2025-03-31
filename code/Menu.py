import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, WIN_HEIGHT, COLOR_GREEN, MENU_OPTION, COLOR_WHITE, COLOR_RED


class Menu:
    def __init__(self, window):
        self.window = window # Nossa Janela
        self.surf = pygame.image.load("Asset/Battleground1.png").convert_alpha() # Nosso background
        self.rect = self.surf.get_rect(left=0, top=0) # Desenhamos um retangulo

    def run(self):
        menu_option = 0;
        pygame.mixer_music.load('Asset/Menu.wav')  # adicionando musica ao Menu
        pygame.mixer_music.play(-1)  # A musica vai ficar tocando eternamente


        while True:
            self.window.blit(source=self.surf, dest=self.rect)  # Vai ficar atualizando a imagem dentro do retangulo
            self.menu_text(70, "Zombie", COLOR_GREEN, ((WIN_HEIGHT / 2), 70)) # Adicinando o text no menu
            self.menu_text(70, "Boy", COLOR_GREEN, ((WIN_HEIGHT / 2), 120)) # Adicinando o text no menu

            # Opções do menu
            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(30, MENU_OPTION[i], COLOR_RED, ((WIN_HEIGHT / 2), 300 + 30 * i))  # Adicinando o text no menu

                else:
                    self.menu_text(30, MENU_OPTION[i], COLOR_WHITE, ((WIN_HEIGHT / 2), 300 + 30 * i))  # Adicinando o text no menu

            #Check for all events
            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    pygame.quit() # fecha a janela
                    quit() # sai do jogo

                if events.type == pygame.KEYDOWN: # Quando o botão de seta for apertado
                    if events.key == pygame.K_DOWN:
                        if menu_option < len(MENU_OPTION) - 1: # Botão para baixo
                            menu_option += 1
                        else:
                            menu_option = 0

                    if events.key == pygame.K_UP:
                        if menu_option > 0: # Botão para Cima
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1

                    if events.key == pygame.K_RETURN: # Botão de enter
                        return MENU_OPTION[menu_option]

            pygame.display.flip()  # Atualiza nosso Display



    def menu_text(self, text_size: int,
                  text: str,
                  text_color: tuple,
                  text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)