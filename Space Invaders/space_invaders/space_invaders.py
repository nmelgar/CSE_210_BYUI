import sys
import pygame
from settings import Settings
from ship import Ship


class SpaceInvaders:
    """General class to manage game assets and behaviors"""

    def __init__(self):
        """Initialize the game, and create the game resources"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))

        pygame.display.set_caption("Space Invaders")
        self.ship = Ship(self)

    def run_game(self):
        """Main loop for the game"""
        while True:
            self._check_events()
            self._update_screen()
            self.ship.update()

            pygame.display.flip()
            # The tick() method takes one argument: the frame rate for the game
            self.clock.tick(60)

    def _check_events(self):
        """Watch for the keyboard and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """for to keypress events"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """for key releases events"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        # draw again the screen during each pass of the loop
        # self.screen.fill(self.settings.bg_color)
        self.screen.blit(self.settings.background_image, (0, 0))
        self.ship.blitme()

        # make recent drawn screen visible
        pygame.display.flip()


if __name__ == '__main__':
    # make a game instance and run the game
    si_game = SpaceInvaders()
    si_game.run_game()
