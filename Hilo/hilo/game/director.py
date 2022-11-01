from game.card import Card


class Director:
    """A person who is responsible of controlling the game.
    He/she will control the sequence of the game.
    Attributes:
        score (int): the available score, starting at 300.
        guess_score (int): if the next card is guessed, 100 added to score.
        failed_score (int): if the next card is not guessed, 75 is subtracted to score.
        run_game (bol): it is to run the game, starts on True to run.

    """

    def __init__(self):
        """This will construct a new director.

        Args:
            self (Director): an instance of Director.

        """
        self.score = 300
        self.guess_score = 100
        self.failed_Score = 75
        self.run_game = True

    def start_game(self):
        """This method will be to start or stop the game.
        It will run the loop to play and stop at different situations.

        Args:
            self (Director): an instance of Director.
        """
        print("\nLet's play!")
        print("")
        while self.run_game:
            self.game_interface()
            if self.score == 0:
                print("\nSee you next time!")
                self.run_game = False
            else:
                keep_playing = self.play_again()
                if keep_playing == True:
                    self.run_game = True
                elif keep_playing == False:
                    self.run_game = False

    def game_interface(self):
        """This method will show the interface and information of the game.
        card_value: a integer value of randomly selected card.
        guess: coming for higher_or_lower function.
        next_card_value: a integer value of randomly selected card.
        self.score: integer that will be added or subtracted.

        Args:
            self (Director): an instance of Director.
        """
        card = Card()
        card_value = card.random_card()
        print(f"\nThe card is: {card_value}")

        # the user will guess if higher or lower for the next card
        guess = self.higher_or_lower()
        if guess == "h" or guess == "l":
            # next card will be created
            next_card_value = card.random_card()
            print(f"Next card was: {next_card_value}")

            # sum or subtract points if guessed or not
            if next_card_value > card_value and guess == "h":
                total_score = self.score + self.guess_score
            elif next_card_value > card_value and guess == "l":
                total_score = self.score - self.failed_Score
            elif next_card_value < card_value and guess == "l":
                total_score = self.score + self.guess_score
            elif next_card_value < card_value and guess == "h":
                total_score = self.score - self.failed_Score
            elif next_card_value == card_value and guess == "h":
                total_score = self.score + 0
            elif next_card_value == card_value and guess == "l":
                total_score = self.score + 0
            self.score = total_score

            print(f"Your score is: {self.score}")
        else:
            print("\nPlease enter a valid option.")

    def higher_or_lower(self):
        """This method will be to allow the user to guess if next card
        will be higher or lower that the randomly selected.
        Input: user input string of and h or l.
        Args:
            self (Director): an instance of Director.

        """
        guess = input("Higher or lower? [h/l] ")
        return guess

    def play_again(self):
        """This method will ask the player to play again or quit.
        Just can choose between y or n, anything else will end
        the game.
        Input: user input string  of y or n.
        Args:
            self (Director): an instance of Director.
        """
        play_again = input("Play again? [y/n] ")
        if play_again.lower() == "y":
            return True
        elif play_again.lower() == "n":
            return False
        else:
            print("\nInvalid input. Bye!")
            return False
