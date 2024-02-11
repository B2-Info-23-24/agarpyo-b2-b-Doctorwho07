import pygame

class Circle:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

    def is_colliding(self, other):
        distance_squared = (self.x - other.x)**2 + (self.y - other.y)**2
        combined_radius = (self.radius + other.radius)**2
        return distance_squared < combined_radius
