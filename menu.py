import pygame
import sys
import os
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.font_title = pygame.font.Font(None, 74)
        self.font_options = pygame.font.Font(None, 36)
        self.selected_option = 0
        self.options = ["Iniciar Jogo", "Sair"]
        self.title = "ASTEROIDS"
        self.controls = [
            "W / Seta Cima - Mover para Frente",
            "A / Seta Esquerda - Rotacionar Esquerda",
            "D / Seta Direita - Rotacionar Direita",
            "Espaço - Atirar"
        ]

        self.background_image = None
        try:
            bg_path = os.path.join("asset", "img", "background.png")
            if not os.path.exists(bg_path):
                bg_path = os.path.join("asset", "img", "bg.png")

            if os.path.exists(bg_path):
                self.background_image = pygame.image.load(bg_path).convert()
                self.background_image = pygame.transform.scale(self.background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        except:
            self.background_image = None

    def draw(self):
        if self.background_image is not None:
            self.screen.blit(self.background_image, (0, 0))
        else:
            self.screen.fill((0, 0, 0))

        title_surf = self.font_title.render(self.title, True, (255, 255, 255))
        title_rect = title_surf.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/4))
        self.screen.blit(title_surf, title_rect)

        for i, option in enumerate(self.options):
            color = (255, 255, 0) if i == self.selected_option else (255, 255, 255)
            option_surf = self.font_options.render(option, True, color)
            option_rect = option_surf.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + i * 50))
            self.screen.blit(option_surf, option_rect)

        y_offset = SCREEN_HEIGHT/2 + len(self.options) * 50 + 50
        for control in self.controls:
            control_surf = self.font_options.render(control, True, (200, 200, 200))
            control_rect = control_surf.get_rect(center=(SCREEN_WIDTH/2, y_offset))
            self.screen.blit(control_surf, control_rect)
            y_offset += 30

        pygame.display.flip()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    self.selected_option = (self.selected_option - 1) % len(self.options)
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    self.selected_option = (self.selected_option + 1) % len(self.options)
                elif event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    if self.selected_option == 0:
                        return "start"
                    elif self.selected_option == 1:
                        pygame.quit()
                        sys.exit()
        return None
