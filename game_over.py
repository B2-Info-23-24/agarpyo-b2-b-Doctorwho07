import pygame
from params import Params
from menu import Menu

class GameOver:
    def __init__(self, player_score, player_size):
        pygame.font.init()
        self.screen = pygame.display.set_mode((Params.SCREEN_WIDTH, Params.SCREEN_HEIGHT))
        self.player_score = player_score
        self.player_size = player_size

    def display_game_over(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return  # Retour au menu si la touche Escape est enfoncée
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.play_again_button_rect.collidepoint(event.pos):
                        return "PlayAgain"  # Retour au menu si le bouton "Play Again" est cliqué

            self.screen.fill((0, 0, 0))

            font = pygame.font.SysFont(None, 36)
            score_text = font.render(f"Score: {self.player_score}", True, Params.WHITE)
            size_text = font.render(f"Player Size: {int(self.player_size)}", True, Params.WHITE)

            # Affichage des informations du joueur
            self.screen.blit(score_text, (Params.SCREEN_WIDTH // 2 - 50, Params.SCREEN_HEIGHT // 2 - 20))
            self.screen.blit(size_text, (Params.SCREEN_WIDTH // 2 - 50, Params.SCREEN_HEIGHT // 2 + 20))

            # Affichage du bouton "Play Again"
            self.draw_play_again_button()

            pygame.display.flip()

    def draw_play_again_button(self):
        play_again_button_rect = pygame.Rect(Params.SCREEN_WIDTH // 2 - 100, Params.SCREEN_HEIGHT // 2 + 100, 200, 50)
        pygame.draw.rect(self.screen, Params.WHITE, play_again_button_rect, 2)
        font = pygame.font.SysFont(None, 25)
        text_surface = font.render("Play Again", True, Params.WHITE)
        text_rect = text_surface.get_rect(center=play_again_button_rect.center)
        self.screen.blit(text_surface, text_rect)
        self.play_again_button_rect = play_again_button_rect
