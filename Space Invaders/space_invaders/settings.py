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

        # Ship settings
        self.ship_speed = 1.5

        # Bullet settings
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (0, 128, 255)
        self.bullets_allowed = 1000000

        # Alien settings
        self.alien_speed = 1.0
        # how fast the fleet goes down the screen
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
