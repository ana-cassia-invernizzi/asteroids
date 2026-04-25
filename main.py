import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state

def main():
    # Iniciando o pygame
    pygame.init()

    # Variáveis criadas para a limitação do FPS
    clock = pygame.time.Clock()
    dt = 0

    # Variável criada para configurar a tela do jogo
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # While Loop infinito que faz com que o jogo rode
    while True:
        # Chamando o logger para salvar o que é feito em um arquivo jsonl
        log_state()

        # For loop para criar os eventos do jogo
        for event in pygame.event.get():
            # Esse evento faz com que o X na janela do jogo seja funcional
            if event.type == pygame.QUIT:
                return

        # A tela é preenchida com a cor preta
        screen.fill("black")
        pygame.display.flip()

        # Chamando o método que limita o FPS para 60
        dt = clock.tick(60) / 1000

    print("Starting Asteroids with pygame version: VERSION")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
