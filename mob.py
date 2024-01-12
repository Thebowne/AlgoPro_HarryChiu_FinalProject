import pygame
import random


class Mob:
    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings

        # Cactus X and Y position
        self.cactus_x = 1000
        self.cactus_y = 570

        # Cactus size
        self.cactus_w = 120
        self.cactus_h = 120

        # Loading cactus image
        self.cactus = pygame.image.load('Images/cactus.png').convert_alpha()
        self.cactus_surface = pygame.transform.scale(self.cactus, (self.cactus_w, self.cactus_h))
        self.cactus_rect = self.cactus_surface.get_rect(midbottom=(self.cactus_x, self.cactus_y))

    # Function to spawn enemy
    def enemy_spawn(self, settings):
        self.cactus_rect.x -= 5
        if self.cactus_rect.right < 0:
            self.cactus_rect.x = random.randint(settings.screen_width + 100, settings.screen_width + 500)
