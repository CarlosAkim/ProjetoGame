import pygame

print("Setup Start")
pygame.init()

window = pygame.display.set_mode(size=(600,480))
print("Setup end")

print("Loop Start")
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            print("Fim do loop")
