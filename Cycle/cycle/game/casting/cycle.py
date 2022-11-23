import constants
from game.casting.actor import Actor
from game.shared.point import Point
from game.shared.color import Color


class Cycle(Actor):
    """
    A fast vehicle that leaves a trace behind.

    The responsibility of Cycle is to move by itself.

    Attributes:
        _segments: list of actors that will make a cycle
        _color: will contain the values to create a color
        _prepare_cycle: will create the cycle
        _name: will be for user's name if using it to display points
    """

    def __init__(self, position):
        """
        Creates a new cycle

        Args:
            position: the postion and direction for each cycle
        """
        super().__init__()
        self._segments = []
        self._color = Color(255, 255, 255)
        self._prepare_cycle(position)
        # self._name = ""

    def get_segments(self):
        """
        Get segments for the cycle.
        """
        return self._segments

    # def get_players_name(self):
    #     """Gets the players name"""

    #     return self._name

    def move_next(self):
        """
        Moves the actors to the next position.
        """
        # move all segments
        for segment in self._segments:
            segment.move_next()
        # update velocities
        for i in range(len(self._segments) - 1, 0, -1):
            trailing = self._segments[i]
            previous = self._segments[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)

    def get_cycle(self):
        """
        Get the first actors from the segments.
        """
        return self._segments[0]

    def walls(self, game_over):
        """
        Creates walls for the cycle as they move
        """
        tail = self._segments[-1]
        velocity = tail.get_velocity()
        offset = velocity.reverse()
        position = tail.get_position().add(offset)

        segment = Actor()
        segment.set_position(position)
        segment.set_velocity(velocity)
        segment.set_text("#")
        if game_over == False:
            segment.set_color(self._color)
        else:
            segment.set_color(constants.WHITE)
        self._segments.append(segment)

    def turn_cycle(self, velocity):
        """
        Changes the direction for a cycle.

        Args:
        ---
            velocity: velocity for the cycle
        """
        self._segments[0].set_velocity(velocity)

    def _prepare_cycle(self, position):
        """
        Creates a new cycle
        Args:
        ---
            position: a position to locate the cycle
        """

        x = position.get_x()
        y = position.get_y()

        for i in range(constants.CYCLE_LENGTH):
            position = Point(x, y + i * constants.CELL_SIZE)
            velocity = Point(0, 1 * -constants.CELL_SIZE)
            text = "O" if i == 0 else "#"

            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(self._color)
            self._segments.append(segment)

    def set_cycle_color(self, color):
        """
        Sets the color for segments of a cycle

        Args:
        ---
            color: color for the cycle
        """

        self._color = color

        for segment in self._segments:
            segment.set_color(self._color)

    # def set_name(self, name):

    #     self._name = name
