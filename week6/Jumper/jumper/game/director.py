from game.terminal_service import TerminalService
from game.puzzle import Puzzle


class Director:
    """A person who is responsible of controlling the game.
    He/she will control the sequence of the game.
    Attributes:
        terminal_service: For getting and displaying information on the terminal.
    """

    def __init__(self):
        """This will construct a new director.

        Args:
            self (Director): an instance of Director.

        """
        self._run_game = True
        self._terminal_service = TerminalService()

    def start_game(self):
        """

        Args:
            self (Director): an instance of Director.
        """
        print("\nLet's play!")
        print("")
        while self._run_game:
            self._game_interface()
            self._get_inputs()

    def _get_inputs(self):
        letter = self._terminal_service.read_letter("\nLetter to guess: ")

    def _game_interface(self):
        puzzle = Puzzle()
        list_of_words = puzzle.list_of_words()
        random_number = puzzle.random_number()
        word = puzzle.generate_word(list_of_words, random_number)
        print(word)
