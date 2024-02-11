import pygame
import math
from params import Params
from circle import Circle

class Player(Circle):
    def __init__(self, x, y):
        super().__init__(x, y, Params.PLAYER_RADIUS, Params.PLAYER_COLOR)
        self.speed = Params.PLAYER_SPEED
        self.radius = Params.PLAYER_RADIUS
        self.movement_mode = "keyboard"
        self.score = 0
    def set_movement_mode(self, mode):
        self.movement_mode = mode
    def eat(self):
        self.increase_speed()
        self.increase_size()
        self.score += 1

    def increase_speed(self):
        if self.speed < Params.MAX_PLAYER_SPEED:
            self.speed += Params.PLAYER_SPEED_INCREMENT

    def increase_size(self):
        if self.radius < Params.MAX_PLAYER_SIZE:
            self.radius += Params.PLAYER_SIZE_INCREMENT

    def move(self, game):
        if self.movement_mode == "keyboard":
            self.move_keyboard()
        elif self.movement_mode == "mouse":
            mouse_pos = pygame.mouse.get_pos()
            self.move_mouse(mouse_pos, Params.FPS)
        self.teleport()
        for trap in game.trap_list:
            if self.is_colliding(trap):
                if self.radius > trap.radius:
                    self.radius -= Params.DIFFICULTY_SETTINGS[game.menu.selected_difficulty]["DecrementAmount"]
                    self.speed -= Params.DIFFICULTY_SETTINGS[game.menu.selected_difficulty]["DecrementAmount"]
                    game.trap_list.remove(trap)
        for food in game.food_list:
            if self.is_colliding(food):
                self.eat()
                game.food_list.remove(food)
                
    def reset_position(self, x, y):
        self.x = x
        self.y = y
        
    def teleport(self):
        if self.x > Params.SCREEN_WIDTH:
            self.x = 0
        if self.x < 0:
            self.x = Params.SCREEN_WIDTH
        if self.y > Params.SCREEN_HEIGHT:
            self.y = 0
        if self.y < 0:
            self.y = Params.SCREEN_HEIGHT

    def move_keyboard(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= self.speed / Params.FPS
        if keys[pygame.K_RIGHT]:
            self.x += self.speed / Params.FPS
        if keys[pygame.K_UP]:
            self.y -= self.speed / Params.FPS
        if keys[pygame.K_DOWN]:
            self.y += self.speed / Params.FPS

        
    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), int(self.radius))
