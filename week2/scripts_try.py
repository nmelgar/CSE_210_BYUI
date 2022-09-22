# Assignment name:  Tic-Tac-Toe
# Student name: Nefi Melgar


def main():
    run = True
    rows = 3
    row_break = 1
    index_counter = 0

    list1 = get_list(rows)
    print_list(list1)

    p1_choice = 0
    p2_choice = 0

    while run:
        player1_choice(list1)
        if win_or_not(list1):
            run = False
        player2_choice(list1)
        if win_or_not(list1):
            run = False


# def win_or_not(list1):
#     global run
#     # for player 1 to win
#     if list1[1] == "X" and list1[2] == "X" and list1[3] == "X":
#         print("\nPlayer 1 won")
#         return True

def win_or_not(list1):
    global run
    # for player 1 to win
    if list1[1] == "X" and list1[2] == "X" and list1[3] == "X":
        print("\nPlayer 1 won")
        return True
    elif list1[1] == "X" and list1[4] == "X" and list1[7] == "X":
        print("\nPlayer 1 won")
        return True
    elif list1[1] == "X" and list1[5] == "X" and list1[9] == "X":
        print("\nPlayer 1 won")
        return True
    elif list1[2] == "X" and list1[5] == "X" and list1[8] == "X":
        print("\nPlayer 1 won")
        return True
    elif list1[3] == "X" and list1[6] == "X" and list1[9] == "X":
        print("\nPlayer 1 won")
        return True
    elif list1[3] == "X" and list1[5] == "X" and list1[7] == "X":
        print("\nPlayer 1 won")
        return True
    elif list1[4] == "X" and list1[5] == "X" and list1[6] == "X":
        print("\nPlayer 1 won")
        return True
    elif list1[7] == "X" and list1[8] == "X" and list1[9] == "X":
        print("\nPlayer 1 won")
        return True

    # for player 2 to win
    elif list1[1] == "o" and list1[2] == "o" and list1[3] == "o":
        print("Player 2 won")
        return True
    elif list1[1] == "o" and list1[4] == "o" and list1[7] == "o":
        print("\nPlayer 2 won")
        return True
    elif list1[1] == "o" and list1[5] == "o" and list1[9] == "o":
        print("\nPlayer 2 won")
        return True
    elif list1[2] == "o" and list1[5] == "o" and list1[8] == "o":
        print("\nPlayer 2 won")
        return True
    elif list1[3] == "o" and list1[6] == "o" and list1[9] == "o":
        print("\nPlayer 2 won")
        return True
    elif list1[3] == "o" and list1[5] == "o" and list1[7] == "o":
        print("\nPlayer 2 won")
        return True
    elif list1[4] == "o" and list1[5] == "o" and list1[6] == "o":
        print("\nPlayer 2 won")
        return True
    elif list1[7] == "o" and list1[8] == "o" and list1[9] == "o":
        print("\nPlayer 2 won")
        return True

# this will create the list of numbers


def get_list(rows):
    rows_and_columns = rows * rows
    numbers = range(0, rows_and_columns + 1)
    list1 = list(numbers)

    return list1


def print_list(list1):
    for x in list1:
        if x != 0:
            print(x, end=' | ')


def player1_choice(list1):
    p1 = int(input("\nPlayer 1 Choose a number: "))
    if p1 in list1:
        list1.pop(p1)
        list1.insert(p1, "X")
        # p1_choice = p1
    print_list(list1)


def player2_choice(list1):
    p2 = int(input("\nPlayer 2 Choose a number: "))
    if p2 in list1:
        list1.pop(p2)
        list1.insert(p2, "o")
        # p2_choice = p2

    print_list(list1)


if __name__ == "__main__":
    main()
