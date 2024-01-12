import pygame


class Player:
    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings

        # Player x and y positions
        self.player_x = 80
        self.player_y = 570

        # Player size
        self.player_w = 100
        self.player_h = 100

        # Gravity
        self.player_gravity = 0

        # Load player image and create player rectangle
        self.player_image = pygame.image.load('Images/chef0.png').convert_alpha()
        self.player_surface = pygame.transform.scale(self.player_image, (self.player_w, self.player_h))
        self.player_rect = self.player_surface.get_rect(midbottom=(self.player_x, self.player_y))
        self.player_surface_1 = pygame.transform.scale(self.player_image, (200, 200))
        self.player_rect_1 = self.player_surface.get_rect(center=(settings.screen_width // 2, settings.screen_height // 2))

    # Increasing the variable to make it seem exponential and hence feels like gravity
    def gravity(self):
        self.player_gravity += 0.6
        self.player_rect.y += self.player_gravity
        if self.player_rect.bottom > 570:
            self.player_rect.bottom = 570
