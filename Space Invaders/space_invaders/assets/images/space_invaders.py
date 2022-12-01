import sys
import pygame
from settings import Settings


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

    def run_game(self):
        """Main loop for the game"""
        while True:
            # watch for the keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # draw again the screen during each pass of the loop
            self.screen.fill(self.settings.bg_color)

            # make recent drawn screen visible
            pygame.display.flip()
            # The tick() method takes one argument: the frame rate for the game
            self.clock.tick(60)


if __name__ == '__main__':
    # make a game instance and run the game
    space_invaders_game = SpaceInvaders()
    space_invaders_game.run_game()
