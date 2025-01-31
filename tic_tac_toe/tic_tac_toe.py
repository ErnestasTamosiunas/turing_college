import sys
import random


def main():
    game_loop()


def validate_input(user_input, board):
    coordinates = []

    if "," in user_input:
        x, y = user_input.split(",")
        if x.isdigit() and y.isdigit():
            x = int(x)
            y = int(y)
        else:
            return coordinates
        if not 0 <= x <= 2 or not 0 <= y <= 2:
            return coordinates
        if board[x][y] == "":
            coordinates.append(x)
            coordinates.append(y)
            return coordinates
    return coordinates


def make_a_move(user_coordinates, board):
    x, y = user_coordinates[:2]
    board[x][y] = "X"
    if check_win("X", board):
        draw_board(board)
        sys.exit("You are the winner!")
    comp_x = 0
    comp_y = 0

    board_has_space = False
    for row in board:
        if "" in row:
            board_has_space = True

    if board_has_space is False:
        draw_board(board)
        sys.exit("It's a tie!")

    board_has_space = False
    while True:
        comp_x = random.randint(0, 2)
        comp_y = random.randint(0, 2)
        if board[comp_x][comp_y] == "":
            board[comp_x][comp_y] = "O"
            break

        if "" in board:
            print("we have an empty space!")
    if check_win("O", board):
        draw_board(board)
        sys.exit("Computer wins!")

    return board


def check_win(char, board):
    coordinates = []
    horizontal = {}
    vertical = {}
    diagonal = set()
    reverse_diagonal = set()
    for b in range(len(board)):
        for n in range(len(board[b])):
            if board[b][n] == char:
                coordinates.append([b, n])

    for c in coordinates:
        if c[0] not in horizontal.keys():
            horizontal[c[0]] = [c[1]]
        else:
            horizontal[c[0]].append(c[1])
        if c[1] not in vertical.keys():
            vertical[c[1]] = [c[0]]
        else:
            vertical[c[1]].append(c[0])
        if c[0] == c[1]:
            diagonal.add((c[0], c[1]))
        if c[0] + c[1] == 2:
            reverse_diagonal.add((c[0], c[1]))
    for h in horizontal:
        if len(horizontal[h]) == 3:
            return True
    for v in vertical:
        if len(vertical[v]) == 3:
            return True
    if len(diagonal) == 3 or len(reverse_diagonal) == 3:
        return True


def draw_board(board):
    for line in board:
        print(line)


def game_loop():
    board = [
        ["", "", ""],
        ["", "", ""],
        ["", "", ""],
    ]
    while True:
        user_input = input("Your move: ")
        user_coordinates = validate_input(user_input, board)

        if len(user_coordinates) == 2:
            make_a_move(user_coordinates, board)
            draw_board(board)
        else:
            continue


if __name__ == "__main__":
    main()
