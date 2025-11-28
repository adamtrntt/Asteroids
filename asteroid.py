import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, surface):
        pygame.draw.circle(surface, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        random_angle = random.uniform(20, 50)
        new_vel1 = self.velocity.rotate(random_angle)
        new_vel2 = self.velocity.rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid1.velocity = new_vel1 * 1.2
        new_asteroid1.add(self.containers)

        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid2.velocity = new_vel2 * 1.2
        new_asteroid2.add(self.containers)


class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, surface):
        pygame.draw.circle(surface, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
