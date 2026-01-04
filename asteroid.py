import pygame
import random

from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)


    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)


    def update(self, dt):
        self.position += self.velocity * dt


    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")

        angle_deg = random.uniform(20, 50)
        child_velocity_one = self.velocity.rotate(angle_deg)
        child_velocity_two = self.velocity.rotate(-angle_deg)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        child_one = Asteroid(self.position[0], self.position[1], new_radius)
        child_two = Asteroid(self.position[0], self.position[1], new_radius)

        child_one.velocity = child_velocity_one * 1.2
        child_two.velocity = child_velocity_two * 1.2
