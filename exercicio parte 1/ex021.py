import pygame

pygame.init()

# Inicializa o mixer de áudio
pygame.mixer.init()

# Carrega o arquivo de áudio
pygame.mixer.music.load('ex021.mp3')

# Reproduz o arquivo de áudio
pygame.mixer.music.play()

# Mantém o programa em execução até a música terminar
while pygame.mixer.music.get_busy():
    pass

pygame.quit()
