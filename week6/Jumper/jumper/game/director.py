from game.terminal_service import TerminalService
from game.puzzle import Puzzle
from game.parachute import Parachute


class Director:
    """A person who is responsible of controlling the game.
    He/she will control the sequence of the game.
    Attributes:
        terminal_service: For getting and displaying information on the terminal.
        puzzle: an instance the Puzzle class to generate a random word.
        parachute: an instance of Parachute class, it will print the parachute of the game.

    """

    def __init__(self):
        """This will construct a new director.

        Args:
            self (Director): an instance of Director.

        """
        self._run_game = True
        self._player_points = 4
        self._terminal_service = TerminalService()
        self._puzzle = Puzzle()
        self.parachute = Parachute()

    def start_game(self):
        """This method will run the game by calling the game interface
        method.    
        Args:
            self (Director): an instance of Director.
        """
        #The game will start here ->
        print("\nLet's play!")
        print("")
        self._game_interface()

    def _get_inputs(self):
        """This method will get the input to guess the random word
        previously generated.
        Args:
            self (Director): an instance of Director.
        """
        letter = self._terminal_service.read_letter("\nGuess a letter[a-z]: ")
        return letter

    def _game_interface(self):
        """This method will display the interface of the game by showing the parachute
        the list of the game based on the random word generated, and the input.
        Args:
            self (Director): an instance of Director.
        """
        puzzle = Puzzle()
        parachute = Parachute()
        word = puzzle.generate_word()
        player_points = self._player_points

        # create the list of underscores based on the puzzle
        new_list = []
        for x in word:
            new_list.append("_")

        # loop of the interface of the game
        while self._run_game:

            # print the list with underscores for the puzzle
            for under in new_list:
                print(under, end=" ")
            print(" ")

            # print the parachute
            parachute.print_parachute(player_points)
            if player_points == 0:
                word_final = str(word)
                print(f"\nThe word was {word_final}")
                self._run_game = False
                return self._run_game

            print(" ")
            # get user input of letter
            letter = self._get_inputs()
            print(" ")

            # check if input letter is part of the word
            for i in range(len(word)):
                individual_letter = word[i]
                if letter == individual_letter:
                    new_list.pop(i)
                    new_list.insert(i, letter)

            # if letter not in word, subtract 1 point of user points
            if letter not in word:
                player_points -= 1

            # if no underscores in the list, cause word was guessed
            under = "_"
            if under not in new_list:
                word_final = str(word)
                print(f"\n{word_final}")
                print(f"\nYou guessed the word!\nThanks for playing!")
                self._run_game = False
                return self._run_game
