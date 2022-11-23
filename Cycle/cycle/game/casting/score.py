import constants

from game.casting.actor import Actor


class Score(Actor):
    """
    A record of points made or lost. 

    The responsibility of Score is to keep track of the points the player has earned by eating food.
    It contains methods for adding and getting points. Client should use get_text() to get a string 
    representation of the points earned.

    Attributes:
        _points (int): The points earned in the game.
    """

    def __init__(self):
        super().__init__()
        self._points = 0
        # self._player_name = ""

    # def add_points(self, points):
    #     """Adds the given points to the score's total points.

    #     Args:
    #         points (int): The points to add.
    #     """
    #     self._points += points
    #     # modify following line to show usernme and points
    #     self.set_text(f"{self._player_name}: {self._points}")

    # def set_player_name(self, name):

    #     self._player_name = name
    #     self.set_text(f"{self._player_name}: {self._points}")

    # def get_player_points(self):
    #     """Gets the points of the player
    #     """
    #     return self._points
