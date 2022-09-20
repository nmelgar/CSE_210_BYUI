# Assignment name:  Tic-Tac-Toe
# Student name: Nefi Melgar


def main():
    grid()


def grid():
    rows = 3
    rows_and_columns = rows * rows
    numbers = range(0, rows_and_columns + 1)
    list1 = list(numbers)
    print(list1)

    print(list1[2])

    list1.pop(2)
    list1.insert(2, "X")

    print(list1)


if __name__ == "__main__":
    main()
