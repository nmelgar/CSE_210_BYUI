word = "hello"
word = list(word)

print("")
guessed = True
new_list = []

for x in word:
    new_list.append("_")

while guessed:
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

    under = "_"
    if under not in new_list:
        word_final = str(word)
        print(f"\nYou guessed the word! {word_final}")
        guessed = False

# def main():


# if __name__ == "__main__":
#     main()
