import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point


class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.

    The responsibility of HandleCollisionsAction is to handle the situation when the snake collides
    with the food, or the snake collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_segment_collision(cast)
        self._handle_walls(cast)
        self._handle_game_over(cast)

    def _handle_walls(self, cast):
        """
        Handles the behavior of cycles with walls

        Args:
        ---
            cast(Cast): cast of Actors
        """

        cycle_one = cast.get_first_actor("cycle_one")
        cycle_two = cast.get_first_actor("cycle_two")
        cycle_one.walls(self._is_game_over)
        cycle_two.walls(self._is_game_over)

    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the cycles collides with one of its segments or 
        to the other cycle.

        Args:
            cast (Cast): The cast of Actors in the game.
        """

        cycle_one = cast.get_first_actor("cycle_one")
        cycle_two = cast.get_first_actor("cycle_two")

        cycle_one_head = cycle_one.get_cycle()
        cycle_two_head = cycle_two.get_cycle()

        segments_one = cycle_one.get_segments()[1:]
        segments_two = cycle_two.get_segments()[1:]

        for segment in segments_one:
            if cycle_two_head.get_position().equals(segment.get_position()):
                self._is_game_over = True
        
        for segment in segments_one:
            if cycle_one_head.get_position().equals(segment.get_position()):
                self._is_game_over = True

        for segment in segments_two:
            if cycle_one_head.get_position().equals(segment.get_position()):
                self._is_game_over = True
        
        for segment in segments_two:
            if cycle_two_head.get_position().equals(segment.get_position()):
                self._is_game_over = True
        


    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the cycles white if the game is over.

        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            cycle_one = cast.get_first_actor("cycle_one")
            cycle_two = cast.get_first_actor("cycle_two")

            segments_one = cycle_one.get_segments()
            segments_two = cycle_two.get_segments()

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text("Game Over!")
            message.set_position(position)
            message.set_font_size(80)
            cast.add_actor("messages", message)

            for segment in segments_one:
                segment.set_color(constants.WHITE)

            for segment in segments_two:
                segment.set_color(constants.WHITE)
