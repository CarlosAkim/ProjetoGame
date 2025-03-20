import pygame.image


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
            pygame.display.flip()  # Atualiza nosso Display


            #Check for all events
            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    pygame.quit()
                    quit()