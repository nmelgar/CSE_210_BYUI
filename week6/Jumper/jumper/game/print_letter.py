word = "hello"
word = list(word)

print("")
run = True
new_list = []

for x in word:
    new_list.append("_")

while run:
    # imprimir la lista con puros underscores
    for under in new_list:
        print(under, end=" ")

    print("\n")
    letter = input("\nletter: ")

    for i in range(len(word)):
        individual_letter = word[i]
        if letter == individual_letter:
            new_list.pop(i)
            new_list.insert(i, letter)

    print(new_list)
    under = "_"
    if under not in new_list:
        run = False
    # # if letter in word:
    # exit = input("Do you want to exit? ")
    # if exit == "s":
    #     run = False


# def main():
#     guessed = False
#     word = "hello"

#     while guessed == False:
#         letter_input = input("Try a letter: ")
#         print(word)
#         print_word(word, letter_input)

# def print_word(word, letter):
#     word = list(word)
#     for x in word:
#         if letter in word:
#             replace_value = word.index(letter)
#             word.insert(replace_value, letter)
#             print(letter, end=" ")
#         else:
#             print("_", end=" ")


# if __name__ == "__main__":
#     main()
