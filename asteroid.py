import pygame
import random
from circleshape import CircleShape 
from constants import ASTEROID_MIN_RADIUS
from constants import ASTEROID_MIN_RADIUS_TO_SPLIT

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

    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS_TO_SPLIT:
            return
        else:
            random_angle = random.uniform(20,50)
            new_radius = self.radius / 2
            v1 = self.velocity.rotate(random_angle) * 1.2
            v2 = self.velocity.rotate(-random_angle) * 1.2

            a1 = Asteroid(self.position.x, self.position.y, new_radius)
            a2 = Asteroid(self.position.x, self.position.y, new_radius)

            a1.velocity = v1
            a2.velocity = v2


