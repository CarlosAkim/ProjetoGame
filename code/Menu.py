import pygame.image


class Menu:
    def __init__(self, window):
        self.window = window # Nossa Janela
        self.surf = pygame.image.load("Asset/Battleground1.png") # Nosso background
        self.rect = self.surf.get_rect(left=0, top=0) # Desenhamos um retangulo

    def run(self):
        self.window.blit(source=self.surf, dest=self.rect) # Vai ficar atualizando a imagem dentro do retangulo
        pygame.display.flip() #Atualiza nosso Display
        pass