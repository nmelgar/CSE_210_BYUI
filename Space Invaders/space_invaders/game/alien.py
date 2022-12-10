import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """An alien, a space ship coming from another planet to invade
    the earth. Single alien of a fleet"""

    def __init__(self, si_game):
        """Initializes the alien and sets its position"""
        super().__init__()
        self.screen = si_game.screen
        self.settings = si_game.settings

        # load the alien image and sets its attributes
        self.image = pygame.image.load('space_invaders/game/images/enemy_ship.png')
        self.rect = self.image.get_rect()

        # start each new alien near t the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # stores the alien's horizontal position.
        self.x = float(self.rect.x)

    def check_edges(self):
        """Returns True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)

    def update(self):
        """Move the alien to the right or left"""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x
