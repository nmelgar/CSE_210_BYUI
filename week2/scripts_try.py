# Assignment name:  Tic-Tac-Toe
# Student name: Nefi Melgar


def main():
    run = True
    list1 = 1
    p1_choice = player1_choice(list1)
    while run:
        user_input = input("Hello:  ")
        if p1_choice == True:
            run = False


def player1_choice(list1):
    if list1 == 1:
        return True
    else:
        return False


if __name__ == "__main__":
    main()
