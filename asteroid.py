import pygame
import random
from constants import *
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(random.uniform(-1,1), random.uniform(-1,1))
        self.velocity.scale_to_length(random.uniform(20,50))

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
        self.position.x %= SCREEN_WIDTH
        self.position.y %= SCREEN_HEIGHT

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return []
        
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        random_angle = random.uniform(20,50)

        new_velocity1 = self.velocity.rotate(random_angle)
        new_velocity2 = self.velocity.rotate(-random_angle)

        new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid1.velocity = new_velocity1 * 1.2

        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid2.velocity = new_velocity2 * 1.2

        return [new_asteroid1, new_asteroid2]