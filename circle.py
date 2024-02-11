import pygame

class Circle:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

    def is_colliding(self, object):
        distance = ((self.x - object.x)**2 + (self.y - object.y)**2)**0.5
        return distance < self.radius + object.radius
