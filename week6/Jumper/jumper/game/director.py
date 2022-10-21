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
        self._puzzle = Puzzle()

    def start_game(self):
        """

        Args:
            self (Director): an instance of Director.
        """
        print("\nLet's play!")
        print("")
        self._game_interface()

    def _get_inputs(self):
        letter = self._terminal_service.read_letter("\nLetter to guess: ")
        return letter

    def _game_interface(self):
        puzzle = Puzzle()
        word = puzzle.generate_word()
        print(word)
        new_list = []

        for x in word:
            new_list.append("_")

        while self._run_game:
            for under in new_list:
                print(under, end=" ")

            print("\n")
            letter = self._get_inputs()

            for i in range(len(word)):
                individual_letter = word[i]
                if letter == individual_letter:
                    new_list.pop(i)
                    new_list.insert(i, letter)

            under = "_"
            if under not in new_list:
                word_final = str(word)
                print(f"\nYou guessed the word! {word_final}")
                self._run_game = False
                return self._run_game
