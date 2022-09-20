# Assignment name:  Tic-Tac-Toe
# Student name: Nefi Melgar


def main():
    rows = 3
    row_break = 1
    index_counter = 0

    #
    list1 = get_list(rows)
    print(print_list(list1))

    p1_choice = 0
    p2_choice = 0

    p1 = int(input("Choose a number: "))

    if p1 in list1:
        list1.pop(p1)
        list1.insert(p1, "X")
        p1_choice = p1
    print(print_list(list1))

    p2 = int(input("Choose a number: "))

    if p2 in list1:
        list1.pop(p2)
        list1.insert(p2, "o")
        p2_choice = p2

    print(print_list(list1))


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


if __name__ == "__main__":
    main()
