import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet


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
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """Main loop for the game"""
        while True:
            self._check_events()
            self._update_screen()
            self.ship.update()
            self._update_bullets()
            # The tick() method takes one argument: the frame rate for the game
            self.clock.tick(60)
            pygame.display.flip()

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
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """for key releases events"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        self.bullets.update()

        # delete bullets that have disappeared from the screen
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        # draw again the screen during each pass of the loop
        # self.screen.fill(self.settings.bg_color)
        self.screen.blit(self.settings.background_image, (0, 0))
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()

        # make recent drawn screen visible
        pygame.display.flip()


if __name__ == '__main__':
    # make a game instance and run the game
    si_game = SpaceInvaders()
    si_game.run_game()
