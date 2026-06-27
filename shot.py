import pygame
import os

from circleshape import CircleShape
from constants import LINE_WIDTH, SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.image = None

        try:
            image_path = os.path.join("asset", "img", "shot.png")
            self.image = pygame.image.load(image_path).convert_alpha()
            size = (SHOT_RADIUS * 2, SHOT_RADIUS * 2)
            self.image = pygame.transform.scale(self.image, size)
        except:
            print("Imagem do tiro não encontrada, usando fallback")
            self.image = None

    def draw(self, screen):
        if self.image is not None:
            rect = self.image.get_rect(center=self.position)
            screen.blit(self.image, rect)
        else:
            pygame.draw.circle(screen, "yellow", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt
