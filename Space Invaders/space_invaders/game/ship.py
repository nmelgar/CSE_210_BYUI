import pygame


class Ship:
    """Class to manage the player's ship"""

    def __init__(self, si_game):
        """Initialize the ship and set its starting position"""
        self.screen = si_game.screen
        self.screen_rect = si_game.screen.get_rect()
        self.settings = si_game.settings

        # load the ship image and get its rect
        self.image = pygame.image.load('space_invaders/game/images/player_ship.png')
        self.rect = self.image.get_rect()

        # new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # float for the ship's exact horizontal position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # movement flag; start with a ship that's not moving.
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update ship's position based on the movement flag."""

        # updates ship's positions not just the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        # Update rect object from self.x
        self.rect.x = self.x
        self.rect.y = self.y

    def center_ship(self):
        """centers the ship on the screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw image at its location"""
        self.screen.blit(self.image, self.rect)
