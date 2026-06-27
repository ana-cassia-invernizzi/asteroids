import pygame
import os

from constants import (
    PLAYER_RADIUS,
    LINE_WIDTH,
    PLAYER_TURN_SPEED,
    PLAYER_SPEED,
    PLAYER_SHOOT_SPEED,
    PLAYER_SHOOT_COOLDOWN_SECONDS
)
from circleshape import CircleShape
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_cooldown = 0
        self.original_image = None

        try:
            image_path = os.path.join("asset", "img", "player.png")
            self.original_image = pygame.image.load(image_path).convert_alpha()
            size = (PLAYER_RADIUS * 2, PLAYER_RADIUS * 2)
            self.original_image = pygame.transform.scale(self.original_image, size)
        except:
            print("Imagem do player não encontrada, usando fallback")
            self.original_image = None

    def triangle(self):
        forward = pygame.Vector2(0, -1).rotate(self.rotation)
        right = pygame.Vector2(0, -1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        if self.original_image is not None:
            rotated_image = pygame.transform.rotate(self.original_image, -self.rotation)
            rect = rotated_image.get_rect(center=self.position)
            screen.blit(rotated_image, rect)
        else:
            pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        self.shot_cooldown -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rotate(-dt)
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rotate(dt)
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.move(-dt)
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.move(dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

    def move(self, dt):
        unit_vector = pygame.Vector2(0, -1).rotate(self.rotation)
        rotated_with_speed_vector = unit_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector

    def shoot(self):
        if self.shot_cooldown > 0:
            return
        self.shot_cooldown = PLAYER_SHOOT_COOLDOWN_SECONDS

        forward = pygame.Vector2(0, -1).rotate(self.rotation)

        shoot_offset = self.radius + 10

        shoot_position = self.position + forward * shoot_offset

        shot = Shot(shoot_position.x, shoot_position.y)
        shot.velocity = forward * PLAYER_SHOOT_SPEED
