import random


def main():
    guessed = False
    words = list(list_of_words())
    number = random_number()
    word = words[number]

    while guessed == False:
        print_word(word, letter="x")
        print(" ")
        letter = input("\nTry a letter: ")
        word_comparison(word, letter)


def list_of_words():
    with open("/home/nmelgar/Projects/CSE_210_BYUI/cse210-01/week6/Jumper/jumper/game/words.txt", "r") as words:
        # use this line when not working at my local machine
        # with open("words.txt", "r") as words:
        list_of_words = []

        for line in words:
            stripped_line = line.strip()
            list_of_words.append(stripped_line)

        return list_of_words


def random_number():
    words = list_of_words()
    length = len(words)
    number = random.randint(0, length)

    return number


# check for optional arguments in this function
def print_word(word, letter):
    # strings are arrays so you can loop through them
    print(word)
    for x in word:
        if letter in word:
            print(x)
        else:
            print("_", end=" ")


def word_comparison(word, letter="x"):
    if letter in word:
        print("\nYes it is here")
    else:
        print("Letter is not here")


if __name__ == "__main__":
    main()
