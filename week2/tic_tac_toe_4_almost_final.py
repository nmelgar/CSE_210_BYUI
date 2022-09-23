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
    # welcome the user
    print("-------------------------------")
    print("Welcome to the Tic-Tac-Toe game")
    print("-------------------------------")
    print("The first in connect 3 wins!---")
    print("-------------------------------")

    # print the board of the game
    print_board(dict_1)
    print("")
    run = True

    # run the game
    while run:
        player1_choice(dict_1)
        print_board(dict_1)
        if winner(dict_1) == False:
            print("")
            break

        player2_choice(dict_1)
        print_board(dict_1)
        if winner(dict_1) == False:
            print("")
            break


def print_board(dict_1):
    """This function will print the board for the players
    Input: dictionary with the numbers from 1 to 9
    Output: The 1-9 board ready to play
    """
    print("")
    for key, value in dict_1.items():
        if key == 3 or key == 6:
            print(value, end="  |  ")
            print("")
            print("----------------")
        else:
            print(value, end="  |  ")


def player1_choice(dict_1):
    """This function will allow the player to choose an available number
    Input: a valid integer
    Output: will update the dictionary with an X at the selected key
    """
    print("")
    choice = int(input("\nPlayer 1 Choose a number: "))
    if choice not in dict_1:
        print("Please enter a valid number")
        print("\nWe will pass to tht next player")
    else:
        dict_1.update({choice: "X"})


def player2_choice(dict_1):
    """This function will allow the player to choose an available number
    Input: a valid integer
    Output: will update the dictionary with an O at the selected key
    """
    print("")
    choice = int(input("\nPlayer 2 Choose a number: "))
    if choice not in dict_1:
        print("Please enter a valid number")
        print("\nWe will pass to tht next player")
    else:
        dict_1.update({choice: "O"})


def winner(dict_1):
    """This function will decide if there is a winner
    Input: the dictionary with the new values for the keys
    """
    for key, value in dict_1.items():
        # for player 1 to win
        if dict_1[1] == "X" and dict_1[2] == "X" and dict_1[3] == "X":
            print("\nPlayer 1 wins!")
            return False
        elif dict_1[1] == "X" and dict_1[4] == "X" and dict_1[7] == "X":
            print("\nPlayer 1 wins!")
            return False
        elif dict_1[1] == "X" and dict_1[5] == "X" and dict_1[9] == "X":
            print("\nPlayer 1 wins!")
            return False
        elif dict_1[2] == "X" and dict_1[5] == "X" and dict_1[8] == "X":
            print("\nPlayer 1 wins!")
            return False
        elif dict_1[3] == "X" and dict_1[6] == "X" and dict_1[9] == "X":
            print("\nPlayer 1 wins!")
            return False
        elif dict_1[3] == "X" and dict_1[5] == "X" and dict_1[7] == "X":
            print("\nPlayer 1 wins!")
            return False
        elif dict_1[4] == "X" and dict_1[5] == "X" and dict_1[6] == "X":
            print("\nPlayer 1 wins!")
            return False
        elif dict_1[7] == "X" and dict_1[8] == "X" and dict_1[9] == "X":
            print("\nPlayer 1 wins!")
            return False

        # for player 2 to win
        elif dict_1[1] == "O" and dict_1[2] == "O" and dict_1[3] == "O":
            print("\nPlayer 2 wins!")
            return False
        elif dict_1[1] == "O" and dict_1[4] == "O" and dict_1[7] == "O":
            print("\nPlayer 2 wins!")
            return False
        elif dict_1[1] == "O" and dict_1[5] == "O" and dict_1[9] == "O":
            print("\nPlayer 2 wins!")
            return False
        elif dict_1[2] == "O" and dict_1[5] == "O" and dict_1[8] == "O":
            print("\nPlayer 2 wins!")
            return False
        elif dict_1[3] == "O" and dict_1[6] == "O" and dict_1[9] == "O":
            print("\nPlayer 2 wins!")
            return False
        elif dict_1[3] == "O" and dict_1[5] == "O" and dict_1[7] == "O":
            print("\nPlayer 2 wins!")
            return False
        elif dict_1[4] == "O" and dict_1[5] == "O" and dict_1[6] == "O":
            print("\nPlayer 2 wins!")
            return False
        elif dict_1[7] == "O" and dict_1[8] == "O" and dict_1[9] == "O":
            print("\nPlayer 2 wins!")
            return False


if __name__ == "__main__":
    main()
