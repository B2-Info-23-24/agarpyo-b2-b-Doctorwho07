import pygame
import random
from player import Player
from circle import Circle
from food import Food
from trap import Trap
from params import Params
from menu import Menu

pygame.init()

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((Params.SCREEN_WIDTH, Params.SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.time = Params.CHRONO_START_TIME
        self.game_started = True
        self.menu_active = True
        self.menu = Menu()
        self.player = Player(Params.PLAYER_START_X, Params.PLAYER_START_Y)
        self.food_list = []
        self.trap_list = []
        self.trap_count = 0
        self.food_count = 0
        self.mouse = False
        self.run()
        
        
    def difficulty_setting(self):
        difficulty_settings = Params.DIFFICULTY_SETTINGS.get(self.menu.selected_difficulty, {})
        self.trap_count = difficulty_settings.get("TrapCount", 0)
        self.food_count = difficulty_settings.get("FoodCount", 0)
    
    def generate_food(self):
        while len(self.food_list) < self.food_count :
            self.food_list.append(Food())

    def generate_trap(self):
        while len(self.trap_list) < self.trap_count :
            self.trap_list.append(Trap())
    
    def draw_elements(self):
        for food in self.food_list:
            food.draw(self.screen)
        self.player.draw(self.screen)
        for trap in self.trap_list:
            trap.draw(self.screen)

    def draw_stats(self):
            font = pygame.font.Font(None, 36)
            time_text = font.render(f"Time: {int(self.time)}", True, Params.WHITE)
            speed_text = font.render(f"Speed: {int(self.player.speed)}", True, Params.WHITE)
            score_text = font.render(f"Score: {self.player.score}", True, Params.WHITE)
            difficulty_text = font.render(f"Difficulty: {self.menu.selected_difficulty}", True, Params.WHITE)
            trap_text = font.render(f"Traps: {len(self.trap_list)}", True, Params.WHITE)
            food_text = font.render(f"Food: {len(self.food_list)}", True, Params.WHITE)
            size_text = font.render(f"Player Size: {int(self.player.radius)}", True, Params.WHITE)
            self.screen.blit(time_text, (10, 10))
            self.screen.blit(speed_text, (10, 50))
            self.screen.blit(score_text, (10, 90))
            self.screen.blit(difficulty_text, (10, 130))
            self.screen.blit(trap_text, (10, 170))
            self.screen.blit(food_text, (10, 210))
            self.screen.blit(size_text, (10, 250))
            
    def run(self):
        while self.game_started:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_started = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.menu_active = not self.menu_active
                    elif event.key == pygame.K_q:  # Ajout de la vérification pour la touche 'Q'
                        self.game_started = False
                if self.menu_active:
                    clicked_checkbox = self.menu.display_menu()
                    if clicked_checkbox:
                        self.difficulty_setting()
                        self.menu_active = False

            self.screen.fill((0, 0, 0))

            if self.menu_active:
                self.menu.display_menu()
            else:
                self.generate_food()
                self.generate_trap()
                self.player.move(self)
                self.draw_elements()
                self.draw_stats()
                self.time -= 1 / Params.FPS
                if self.time <= 0:
                    self.game_started = False
            pygame.display.flip()
            self.clock.tick(Params.FPS)

        pygame.quit()