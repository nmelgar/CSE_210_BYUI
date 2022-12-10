class GameStats:
    """A game tracking for statistics of the game"""

    def __init__(self, si_game):
        """Initializes the statistics"""
        self.settings = si_game.settings
        self.reset_stats()

    def reset_stats(self):
        """Initializes statistics that can change during the game"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
