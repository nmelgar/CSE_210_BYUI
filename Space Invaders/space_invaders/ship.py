import pygame

class Ship:
    """Class to manage the player's ship"""
    def __init__(self, si_game):
        """Initialize the ship and set its starting position"""
        self.screen = si_game.screen
        self.screen_rect = si_game.screen.get_rect()

        # load the ship image and get its rect
        self.image = pygame.image.load('space_invaders/images/player_ship.png')
        self.rect = self.image.get_rect()

        # new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom
    
    def blitme(self):
        """Draw image at its location"""
        self.screen.blit(self.image, self.rect)