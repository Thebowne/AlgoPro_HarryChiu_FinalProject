import pygame


class Settings:
    def __init__(self):
        # Screen size
        self.screen_width = 1200
        self.screen_height = 720

        # Game Icon Image
        self.icon = pygame.image.load('Images/drumstick.png')
