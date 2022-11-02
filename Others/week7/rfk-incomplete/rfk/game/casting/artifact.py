import random
from game.casting.actor import Actor
from game.shared.color import Color
from game.shared.point import Point


# TODO: Implement the Artifact class here. Don't forget to inherit from Actor!


class Artifact(Actor):
    """A visible not moveable things
        
        Attributes:
        _text (string): The text to display
        _font_size (int): The font size to use.
        _color (Color): The color of the text.
        _position (Point): The screen coordinates.
        _message (string): message that will be displayed.
  
    
    """
    def __init__(self):
        """Constructs a new Artifact"""
        self._text = ""
        self._font_size = 15
        self._color = Color(255, 255, 255)
        self._position = Point(0, 0)
    
    def set_message():
        random_number = random.randint(0, 255)
        return random_number
 