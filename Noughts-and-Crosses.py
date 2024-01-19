def print_grid(grid):
    print("            A   B   C ")
    for count, row in enumerate(grid):
        print("          %i %s | %s | %s " % (count + 1, row[0], row[1], row[2]))
        if count == 2:
            break
        else:
            print("           ---+---+---")


def choose_location():
    while True:
        print("\nWhich row do you want to fill in?")
        row_number = input(">>> ")
        if (row_number not in ["1", "2", "3"]):
            input("Not a row. Press enter to continue:\n>>> ")
            print("\n\n\n\n")
            continue
        else:
            row_number = int(row_number) - 1
            break

    while True:
        print("\nWhich column do you want to fill in?")
        column_number = input(">>> ")
        if (column_number not in ["a", "A", "b", "B", "c", "C"]):
            input("Not a column. Press enter to continue:\n>>> ")
            print("\n\n\n\n")
            continue
        else:
            column_number = { "A" : 0,
                              "B" : 1,
                              "C" : 2}[column_number.upper()]
            break

    return (column_number, row_number)


def add_shape(shape, grid, x, y):
    grid[y][x] = shape

    return grid


def is_valid_input(grid, x, y):
    return grid[y][x] == " " and (x in [0, 1, 2]) and (y in [0, 1, 2])


def is_board_full(grid):
    return all(map(lambda x : x != " ", [cell for row in grid for cell in row]))


def game(grid, current_turn=False):
    turn = ("X", "O")

    while True:
        print("\n\n\n\n\n" + turn[current_turn] + "'s turn")
        print_grid(grid)

        while True:
            coordinates = choose_location()
            if is_valid_input(grid, *coordinates):
                break
            else:
                input("\nInvalid input. Press enter to continue:\n>>>")
                print("\n\n\n\n")
                print_grid(grid)
    
        grid = add_shape(turn[current_turn], grid, *coordinates)

        if is_board_full(grid):
            print("\n\n\n")
            print_grid(grid)
            print("\n\
                   \n         +-------------+\
                   \n         |             |\
                   \n         |             |\
                   \n         |  GAME OVER  |\
                   \n         |             |\
                   \n         |             |\
                   \n         +-------------+\
                   \n\n\n\
                ")
            break

        current_turn = not current_turn



if __name__ == "__main__":
    game([[" "] * 3 for _ in range(3)])
