import pygame


class Background:
    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings

        # Sky and Ground background
        self.surface = pygame.image.load('Images/sky.jpg').convert()
        self.sky_surface = pygame.transform.scale(self.surface, (settings.screen_width, settings.screen_height))
        self.surface2 = pygame.image.load('Images/images.png').convert()
        self.ground_surface = pygame.transform.scale(self.surface2, (settings.screen_width, settings.screen_height))

        # Game title
        self.font_size = 54
        self.text_color = (64, 64, 64)
        self.text_font = pygame.font.Font(None, self.font_size)
        self.text_surface = self.text_font.render('Chef adventure', False, self.text_color)
        self.text_rect = self.text_surface.get_rect(center=(settings.screen_width // 2, settings.screen_height // 6))

        # Game over title
        self.go_font_size = 54
        self.go_text_color = (64, 64, 64)
        self.go_text_font = pygame.font.Font(None, self.go_font_size)
        self.go_text_surface = self.go_text_font.render('Game over', False, self.go_text_color)
        self.go_text_rect = self.go_text_surface.get_rect(center=(settings.screen_width // 2, settings.screen_height // 4))
        self.go_text_surf_1 = self.go_text_font.render('Press Space to play again', False, self.go_text_color)
        self.go_text_rect_1 = self.go_text_surf_1.get_rect(center=(settings.screen_width // 2, settings.screen_height / 1.2))

