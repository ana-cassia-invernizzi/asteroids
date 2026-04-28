import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    # Iniciando o pygame
    pygame.init()

    # Variáveis criadas para a limitação do FPS
    clock = pygame.time.Clock()
    dt = 0

    # Criando os grupos utilizando um método do próprio pygame
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Adicionando cada instância criada desses objetos nos grupos
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    # Criando os objetos
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

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

        updatable.update(dt)
        for obj in drawable:
            obj.draw(screen)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        pygame.display.flip()

        # Chamando o método que limita o FPS para 60
        dt = clock.tick(60) / 1000

    print("Starting Asteroids with pygame version: VERSION")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
