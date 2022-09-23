# Assignment name:  Tic-Tac-Toe
# Student name: Nefi Melgar


def main():
    print("")
    list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    get_list(list_1)


def get_list(list_1):
    for x in range(len(list_1)):
        print(list_1[x], end="  |  ")
    

if __name__ == "__main__":
    main()
