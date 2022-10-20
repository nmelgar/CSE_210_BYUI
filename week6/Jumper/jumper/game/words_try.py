import random


def main():
    guessed = True
    words = list(list_of_words())
    number = random_number()
    word = words[number]
    print_word(word)


def list_of_words():
    # with open("/home/nmelgar/Projects/CSE_210_BYUI/cse210-01/week6/Jumper/jumper/game/words.txt", "r") as words:
    # use this line when not working at my local machine
    with open("words.txt", "r") as words:
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


def print_word(word):
    guessed = True
    new_list = []

    for x in word:
        new_list.append("_")

    while guessed:
        for under in new_list:
            print(under, end=" ")

        print("\n")
        letter = input("\nletter: ")

        for i in range(len(word)):
            individual_letter = word[i]
            if letter == individual_letter:
                new_list.pop(i)
                new_list.insert(i, letter)

        under = "_"
        if under not in new_list:
            word_final = str(word)
            print(f"\nYou guessed the word! {word_final}")
            guessed = False
            return guessed


if __name__ == "__main__":
    main()
