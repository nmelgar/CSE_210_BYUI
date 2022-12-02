import pygame


class Settings:
    """a class to store the settings of the game"""

    def __init__(self):
        """Initialize the game's settings"""

        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.background_image = pygame.image.load(
            "space_invaders/images/in_game_bg_alt_3.png")
