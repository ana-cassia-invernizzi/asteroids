import pygame
import sys
import os
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from menu import Menu

def main():
    # Iniciando o pygame
    pygame.init()

    try:
        music_path = os.path.join("asset", "sound", "bg_music.wav")

        if os.path.exists(music_path):
            pygame.mixer.music.load(music_path)
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.3)
        else:
            print("Arquivo de música não encontrado")
    except Exception as e:
        print(f"Erro ao carregar música: {e}")

    # Variáveis criadas para a limitação do FPS
    clock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")

    background_image = None
    try:
        bg_path = os.path.join("asset", "img", "background.png")
        if not os.path.exists(bg_path):
            bg_path = os.path.join("asset", "img", "bg.png")

        if os.path.exists(bg_path):
            background_image = pygame.image.load(bg_path).convert()
            background_image = pygame.transform.smoothscale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        else:
            print("Imagem de fundo não encontrada")
    except Exception as e:
        print(f"Erro ao carregar imagem de fundo: {e}")

    menu = Menu(screen)
    in_menu = True
    while in_menu:
        action = menu.handle_events()
        menu.draw()
        if action == "start":
            in_menu = False
        clock.tick(60)

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
        # For loop para criar os eventos do jogo
        for event in pygame.event.get():
            # Esse evento faz com que o X na janela do jogo seja funcional
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if background_image is not None:
            screen.blit(background_image, (0, 0))
        else:
            screen.fill("black")

        updatable.update(dt)
        for obj in drawable:
            obj.draw(screen)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                pygame.mixer.music.stop()
                sys.exit()

        for asteroid in asteroids:
            for shot in shots:
                if shot.collides_with(asteroid):
                    asteroid.split()
                    shot.kill()

        pygame.display.flip()

        # Chamando o método que limita o FPS para 60
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
