import random


class Puzzle:
    """A magic and secret word generated. 
    The purpose is to generate a random word so the user
    can guess it.

    Attributes:
        word(str): A random word
    """

    def __init__(self):
        self.word = 0

    def list_of_words(self):
        """This function will be to generate the list of words.
        It will return the list of words so a random word can be chosen later.

        Args:
            self (word): An instance of puzzle
        """
        # use this line when not working at my local machine
        # with open("words.txt", "r") as words:
        with open("/home/nmelgar/Projects/CSE_210_BYUI/cse210-01/week6/Jumper/jumper/trying/words.txt", "r") as words:
            list_of_words = []

            for line in words:
                stripped_line = line.strip()
                list_of_words.append(stripped_line)

            return list_of_words

    def random_number(self):
        """This function will be to generate a random number.
        This number will be used when generating the random word.

        Args:
            self (word): An instance of puzzle
        """
        words = self.list_of_words()
        length = len(words)
        number = random.randint(0, length)

        return number

    def generate_word(self):
        """This function will be to generate a random word. 
        It will be taking the list_of_words() and random_number() functions,
        not as parameters.

        Args:
            self (word): An instance of puzzle
        """
        list_of_words = self.list_of_words()
        words = list(list_of_words)
        random_number = self.random_number()

        word = words[random_number]

        return word
