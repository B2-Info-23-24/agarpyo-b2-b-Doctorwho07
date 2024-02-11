import pygame
import math
from params import Params
from circle import Circle

class Player(Circle):
    def __init__(self, x, y):
        super().__init__(x, y, Params.PLAYER_RADIUS, Params.PLAYER_COLOR)
        self.speed = Params.PLAYER_SPEED
        self.size = Params.PLAYER_RADIUS
        self.score = 0

    def update(self, follow_mouse=False):
        self.move(follow_mouse)


    def eat(self):
        self.increase_speed()
        self.increase_size()

    def increase_speed(self):
        if self.speed < Params.MAX_PLAYER_SPEED:
            self.speed += Params.PLAYER_SPEED_INCREMENT

    def increase_size(self):
        if self.size < Params.MAX_PLAYER_SIZE:
            self.size += Params.PLAYER_SIZE_INCREMENT

    def move(self, follow_mouse=False):
        if follow_mouse:
            self.move_mouse()
        else:
            self.move_keyboard()


    def move_keyboard(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.x > self.radius:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x < Params.SCREEN_WIDTH - self.radius:
            self.x += self.speed
        if keys[pygame.K_UP] and self.y > self.radius:
            self.y -= self.speed
        if keys[pygame.K_DOWN] and self.y < Params.SCREEN_HEIGHT - self.radius:
            self.y += self.speed
            
    def move_mouse(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        angle = math.atan2(mouse_y - self.y, mouse_x - self.x)
        self.x += self.speed * math.cos(angle)
        self.y += self.speed * math.sin(angle)

