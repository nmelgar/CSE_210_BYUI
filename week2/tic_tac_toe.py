# Assignment name:  Tic-Tac-Toe
# Student name: Nefi Melgar


def main():
    grid()


def grid():
    rows = 3
    rows_times_columns = rows * rows
    list1 = range(1, rows_times_columns + 1)
    for x in list1:
        print(x, end=' | ')
        if x == rows:
            print("")
            print("-----------")
        elif x == rows * 2:
            print("")
            print("-----------")
        # elif x == rows * 3:
        #     print("")
        #     print("-----------")


if __name__ == "__main__":
    main()
