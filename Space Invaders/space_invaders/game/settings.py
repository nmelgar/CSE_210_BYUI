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
            "space_invaders/game/images/in_game_bg_alt_3.png")

        # Ship settings
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (0, 128, 255)
        self.bullets_allowed = 1000000

        # Alien settings
        self.fleet_drop_speed = 10
        # How quickly the game speeds up
        self.speedup_scale = 1.1
        # alient point values increases at this speed
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initializes settings that change throughout the game."""
        self.ship_speed = 1.5
        self.bullet_speed = 2.5
        self.alien_speed = 1.0
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # score settings
        self.alien_points = 50

    def increase_speed(self):
        """Increases speed settings"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)
