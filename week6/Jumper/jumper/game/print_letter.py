def main():
    guessed = False
    word = "hello"

    while guessed == False:
        letter_input = input("Try a letter: ")
        print(word)
        print_word(word, letter_input)
        
def print_word(word, letter):
    word = list(word)
    for x in word:
        if letter in word:
            replace_value = word.index(letter)
            word.insert(replace_value, letter)          
            print(letter, end=" ")
        else:
            print("_", end=" ")
    


if __name__ == "__main__":
    main()
