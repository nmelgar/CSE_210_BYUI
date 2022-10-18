import random


class Card:
    """An squared object with printed numbers on it. 
    The purpose of a card is to show a number and then 
    compare this card with another one.
    A decision will be taken when comparing cards correctly or not.
    A card can have a value from 1 to 13.

    Attributes:
        value(int): The number of possible values (1 - 13)
    """

    def __init__(self):
        self.value = 0

    def random_card(self):
        """Args:
            self (Card): An instance of Card.
        """
        value = self.individual_value = random.randint(1, 13)
        return value
