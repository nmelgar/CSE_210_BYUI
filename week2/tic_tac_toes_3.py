# Assignment name:  Tic-Tac-Toe
# Student name: Nefi Melgar


def main():
    print("")
    list_1 = ["1", "2", "x", "x", "5", "6", "7", "8", "9"]
    get_list(list_1)


def get_list(list_1):
    i = 0

    for x in list_1:
        number = list_1[i]
        index = list_1.index(number) + 1
        # print(f"{x} has index of: {index}")
        if index == 3 or index == 6:
            print(x, end="  |  ")
            print("")
            print("----------------")
        elif index != 3 or index != 6:
            print(x, end="  |  ")

        i += 1


if __name__ == "__main__":
    main()
