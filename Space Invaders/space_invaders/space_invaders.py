import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from time import sleep
from game_stats import GameStats
from button import Button


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
        # instance to store game statistics
        self.stats = GameStats(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

        # Start the game in an active state.
        self.game_active = False

        # create the Play button
        self.play_button = Button(self, "Play")

    def run_game(self):
        """Main loop for the game"""
        while True:
            self._check_events()
            self._update_screen()
            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            # The tick() method takes one argument: the frame rate for the game
            self.clock.tick(60)
            pygame.display.flip()

    def _check_events(self):
        """Watch for the keyboard and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_play_button(self, mouse_pos):
        """Starts a new game when the player clicks Play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            # Reset the game settings
            self.settings.initialize_dynamic_settings()
            # Resets the game statistics
            self.stats.reset_stats()
            self.game_active = True

            # Get rid of any remaining bullets and alienss
            self.bullets.empty()
            self.aliens.empty()

            # Create a new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()

            # Hides the mouse cursor
            pygame.mouse.set_visible(False)

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

    def _ship_hit(self):
        """responds to ship being hit by an alien"""
        if self.stats.ships_left > 0:
            # decrement ships_left.
            self.stats.ships_left -= 1

            # get rid of any remaining bullets and aliens
            self.bullets.empty()
            self.aliens.empty()

            # create a new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()

            # Pause
            sleep(0.5)
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)

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

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Responds to bullet collision with aliens"""
        # Remove any bullets and aliens that have collided
        # Checks for any bullets that have hit aliens
        # If so, get rid of the bullet and the alien
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)

        if not self.aliens:
            # destroys existing bullets and creates new fleet
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

    def _check_aliens_bottom(self):
        """Checks if any aliens have reached the bottom of the screen"""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                # this is the same as if the ship got hit
                self._ship_hit()
                break

    def _update_aliens(self):
        """Check if the fleet is at an edge, then update positions."""
        self._check_fleet_edges()
        self.aliens.update()

        # look for collision of alients with ship
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # look for aliens hitting the bottom of the screen
        self._check_aliens_bottom()

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        # draw again the screen during each pass of the loop
        # self.screen.fill(self.settings.bg_color)
        self.screen.blit(self.settings.background_image, (0, 0))
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)

        # Draws the play button if the game is inactive
        if not self.game_active:
            self.play_button.draw_button()

        # make recent drawn screen visible
        pygame.display.flip()

    def _create_fleet(self):
        """Create the fleet or group of aliens"""
        # make an alien
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width

            # Finished a row; reset x value, and increment y value.
            current_x = alien_width
            current_y += 2 * alien_height

    def _create_alien(self, x_position, y_position):
        """Creates new alient and add it to the row"""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _check_fleet_edges(self):
        """responds if any aliens have reached an edge"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """drops the entire fleet and change the fleet's direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1


if __name__ == '__main__':
    # make a game instance and run the game
    si_game = SpaceInvaders()
    si_game.run_game()
