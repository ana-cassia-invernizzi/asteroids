import random
import pygame
import os

from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.image = None
        self.load_asteroid_image()

    def load_asteroid_image(self):
        try:
            image_path = os.path.join("asset", "img", "asteroid.png")

            image = pygame.image.load(image_path).convert_alpha()

            size = (self.radius * 2, self.radius * 2)
            self.image = pygame.transform.scale(image, size)
        except:
            print("Imagem do asteroide não encontrada")
            self.image = None

    def draw(self, screen):
        if self.image:
            rect = self.image.get_rect(center=self.position)
            screen.blit(self.image, rect)
        else:
            pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        angle = random.uniform(20, 50)
        new_velocity_1 = self.velocity.rotate(angle)
        new_velocity_2 = self.velocity.rotate(-angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        first_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        second_asteroid = Asteroid(self.position.x, self.position.y, new_radius)

        first_asteroid.velocity = new_velocity_1 * 1.2
        second_asteroid.velocity = new_velocity_2 * 1.2
