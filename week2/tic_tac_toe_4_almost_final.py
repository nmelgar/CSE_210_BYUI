# Assignment name:  Tic-Tac-Toe
# Student name: Nefi Melgar


def main():
    dict_1 = {
        1: "1",
        2: "2",
        3: "3",
        4: "4",
        5: "5",
        6: "6",
        7: "7",
        8: "8",
        9: "9"
    }
    print("-------------------------------")
    print("Welcome to the Tic-Tac-Toe game")
    print("-------------------------------")
    print("The first in connect 3 wins!---")
    print("-------------------------------")

    print_board(dict_1)
    print("")
    run = True
    while run:
        player1_choice(dict_1)
        print_board(dict_1)
        winner(dict_1)
        player2_choice(dict_1)
        print_board(dict_1)
        winner(dict_1)


def print_board(dict_1):
    print("")
    for key, value in dict_1.items():
        if key == 3 or key == 6:
            print(value, end="  |  ")
            print("")
            print("----------------")
        else:
            print(value, end="  |  ")


def player1_choice(dict_1):
    print("")
    choice = int(input("\nPlayer 1 Choose a number: "))
    dict_1.update({choice: "X"})


def player2_choice(dict_1):
    print("")
    choice = int(input("\nPlayer 2 Choose a number: "))
    dict_1.update({choice: "O"})


def winner(dict_1):
    for key, value in dict_1.items():

        # for player 1 to win
        if key == 1 and value == "X" and key == 2 and value == "X":
            print("\nPlayer 1 wins!")
        # elif (key == 1 and value == "X") and (key == 4 and value == "X") and (key == 7 and value == "X"):
        #     print("\nPlayer 1 wins!")
        # elif (key == 1 and value == "X") and (key == 5 and value == "X") and (key == 9 and value == "X"):
        #     print("\nPlayer 1 wins!")
        # elif (key == 2 and value == "X") and (key == 5 and value == "X") and (key == 8 and value == "X"):
        #     print("\nPlayer 1 wins")
        # elif (key == 3 and value == "X") and (key == 6 and value == "X") and (key == 9 and value == "X"):
        #     print("\nPlayer 1 wins")
        # elif (key == 3 and value == "X") and (key == 5 and value == "X") and (key == 7 and value == "X"):
        #     print("\nPlayer 1 wins")
        # elif (key == 4 and value == "X") and (key == 5 and value == "X") and (key == 6 and value == "X"):
        #     print("\nPlayer 1 wins")
        # elif (key == 7 and value == "X") and (key == 8 and value == "X") and (key == 9 and value == "X"):
        #     print("\nPlayer 1 wins")

        # for player 2 to win
        # elif (key == 1 and value == "O") and (key == 2 and value == "O") and (key == 3 and value == "O"):
        #     print("\nPlayer 2 wins!")
        # elif (key == 1 and value == "O") and (key == 4 and value == "O") and (key == 7 and value == "O"):
        #     print("\nPlayer 2 wins!")
        # elif (key == 1 and value == "O") and (key == 5 and value == "O") and (key == 9 and value == "O"):
        #     print("\nPlayer 2 wins!")
        # elif (key == 2 and value == "O") and (key == 5 and value == "O") and (key == 8 and value == "O"):
        #     print("\nPlayer 2 wins!")
        # elif (key == 3 and value == "O") and (key == 6 and value == "O") and (key == 9 and value == "O"):
        #     print("\nPlayer 2 wins!")
        # elif (key == 3 and value == "O") and (key == 5 and value == "O") and (key == 7 and value == "O"):
        #     print("\nPlayer 2 wins!")
        # elif (key == 4 and value == "O") and (key == 5 and value == "O") and (key == 6 and value == "O"):
        #     print("\nPlayer 2 wins!")
        # elif (key == 7 and value == "O") and (key == 8 and value == "O") and (key == 9 and value == "O"):
        #     print("\nPlayer 2 wins!")


if __name__ == "__main__":
    main()
