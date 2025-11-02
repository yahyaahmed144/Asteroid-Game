import pygame
from circleshape import CircleShape  # or from circle_shape import CircleShape, depending on your filename

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        # Call parent constructor
        super().__init__(x, y, radius)

        # Optionally give it some initial velocity (example: moving diagonally)
        self.velocity = pygame.Vector2(100, 60)  # pixels per second, change as you like

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
