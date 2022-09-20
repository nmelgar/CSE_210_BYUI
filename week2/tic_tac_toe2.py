# Assignment name:  Tic-Tac-Toe
# Student name: Nefi Melgar


def main():
    rows = 3
    row_break = 1
    list1 = get_list(rows)
    # print(list1[2])
    # grid(list1)
    # print(list1)
    # list1.pop(3)
    # list1.insert(3, "X")
    index_counter = 0
    for x in list1:
        if x != 0:
            print(x, end=' | ')
        if list1[index_counter] == rows * row_break:
            print("")
            print("-----------")
            row_break += 1
        index_counter += 1


# this will create the grid using the list of numbers
# def grid(list1):
    # print(list1)
    # print(list1[2])
    # list1.pop(2)
    # list1.insert(2, "X")
    # print(list1)


# this will create the list of numbers
def get_list(rows):

    rows_and_columns = rows * rows
    numbers = range(0, rows_and_columns + 1)
    list1 = list(numbers)

    return list1


if __name__ == "__main__":
    main()
