import pygame
from params import Params
from player import Player

class Menu:
    def __init__(self):
        pygame.font.init()
        self.screen = pygame.display.set_mode((Params.SCREEN_WIDTH, Params.SCREEN_HEIGHT))
        self.menu_active = True
        self.selected_difficulty = "EASY"
        self.difficulty_checked = False
        self.selected_control = "StartKeyboard"

    def draw_checkbox(self, checkbox_rect, checked, text):
        pygame.draw.rect(self.screen, Params.WHITE, checkbox_rect, 2)
        if checked:
            pygame.draw.line(self.screen, Params.WHITE, (checkbox_rect.x - 5, checkbox_rect.centery),(checkbox_rect.x + checkbox_rect.width + 5, checkbox_rect.centery), 2)
        font = pygame.font.SysFont(None, 25)
        text_surface = font.render(text, True, Params.WHITE)
        text_rect = text_surface.get_rect(center=checkbox_rect.center)
        self.screen.blit(text_surface, text_rect)

    def handle_checkbox_click(self, checkbox_rect, difficulty):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if checkbox_rect.collidepoint(mouse) and click[0] == 1:
            self.selected_difficulty = difficulty
            self.difficulty_checked = True

    def draw_difficulty_options(self):
        font = pygame.font.SysFont(None, 30)
        text = font.render(f"Difficulty: {self.selected_difficulty}", True, Params.WHITE)
        self.screen.blit(text, (50, 400))
        self.draw_checkbox(pygame.Rect(50, 450, 40, 40), self.selected_difficulty == "EASY", "EASY")
        self.draw_checkbox(pygame.Rect(50, 500, 40, 40), self.selected_difficulty == "NORMAL", "NORMAL")
        self.draw_checkbox(pygame.Rect(50, 550, 40, 40), self.selected_difficulty == "HARD", "HARD")

    def draw_button(self, button_rect, text, action):
        pygame.draw.rect(self.screen, Params.WHITE, button_rect, 2)
        font = pygame.font.SysFont(None, 25)
        text_surface = font.render(text, True, Params.WHITE)
        text_rect = text_surface.get_rect(center=button_rect.center)
        self.screen.blit(text_surface, text_rect)

    def handle_button_click(self, button_rect, action):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if button_rect.collidepoint(mouse) and click[0] == 1:
            if action == "Exit":
                pygame.quit()
                quit()
            if action in ["StartKeyboard", "StartMouse"]:
                self.selected_control = action
                self.menu_active = False
            return action
        return None


    def draw_menu_buttons(self):
        self.draw_button(pygame.Rect(250, 450, 200, 50), "Start with Keyboard", "StartKeyboard")
        self.draw_button(pygame.Rect(250, 500, 200, 50), "Start with Mouse", "StartMouse")
        self.draw_button(pygame.Rect(250, 550, 200, 50), "Exit", "Exit")

    def display_menu(self):
        clicked_button = None
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_checkbox_click(pygame.Rect(50, 450, 40, 40), "EASY")
                    self.handle_checkbox_click(pygame.Rect(50, 500, 40, 40), "NORMAL")
                    self.handle_checkbox_click(pygame.Rect(50, 550, 40, 40), "HARD")
                    clicked_button = self.handle_button_click(pygame.Rect(250, 450, 200, 50), "StartKeyboard")
                    if clicked_button:
                        Player.set_movement_mode(self, "keyboard")
                        return self.selected_difficulty

            keys = pygame.key.get_pressed()
            if keys[pygame.K_q]:
                pygame.quit()
                quit()

            if keys[pygame.K_p] and self.selected_control == "StartKeyboard" and self.difficulty_checked:
                return self.selected_difficulty

            if self.difficulty_checked:
                if keys[pygame.K_p]:
                    return self.selected_difficulty

            self.screen.fill((0, 0, 0))

            self.draw_difficulty_options()
            self.draw_menu_buttons()

            pygame.display.flip()

            clicked_button = self.handle_button_click(pygame.Rect(250, 500, 200, 50), "StartMouse")
            if clicked_button:
                Player.set_movement_mode(self, "mouse")
                if clicked_button == "Exit":
                    pygame.quit()
                    quit()
                return self.selected_difficulty
