from constants import BLACK_PIECES, CHESS_BOARD, COLORS, WHITE_PIECES
from random import choice
from typing import Dict, List, Tuple, Union, Optional
import sys


def main() -> None:
    """Main function to execute the chess game logic."""
    chess_board = CHESS_BOARD
    print_info("intro")
    draw_chess_board(get_flat_board(chess_board))
    first_input = take_input(COLORS["W"], chess_board)
    if first_input and isinstance(first_input, List):
        white_figure = first_input[0]
        white_coordinate = first_input[1]
        chess_board = update_board(white_figure, white_coordinate, chess_board)
    draw_chess_board(get_flat_board(chess_board))

    for _ in range(16):
        if (coordinate := take_input(COLORS["B"], chess_board)) != "exit":
            b_figure = get_random_b_piece(chess_board)
            if coordinate and isinstance(coordinate, str):
                chess_board = update_board(b_figure, coordinate, chess_board)
                draw_chess_board(get_flat_board(chess_board))
        else:
            break

    if first_input and isinstance(first_input, List):
        all_moves, flat_board = get_all_w_moves(first_input, chess_board)
        result, pieces_taken = get_result_count(all_moves, flat_board)
        print_info("result", "", result, pieces_taken)
        draw_chess_board(flat_board)


def count_black_pieces(board: List[Dict]) -> Dict:
    """Counts the number of black pieces currently on the board."""
    piece_count = {}
    for square in board:
        for piece in square.values():
            if piece.startswith("b_") and piece not in piece_count:
                piece_count[piece] = 0
            if piece.startswith("b_") and piece in piece_count:
                piece_count[piece] += 1
    return piece_count


def get_random_b_piece(board: List[Dict]) -> str:
    """Returns a random black piece that can still be placed on board."""
    placed_pieces = count_black_pieces(board)
    available_pieces = []
    for piece_dict in BLACK_PIECES:
        for piece, max_count in piece_dict.items():
            current_count = placed_pieces.get(piece, 0)
            if current_count < max_count:
                available_pieces.append(piece)
    return choice(available_pieces)


def get_result_count(moves: Dict, flat_board: Dict) -> Tuple[int, Dict]:
    """Counts the number of black pieces that have been taken
    and gets coordinates
    """
    count = 0
    pieces_taken = {}
    for _, positions in moves.items():
        for p in positions:
            piece = flat_board.get(p, "")
            if piece.startswith("b_"):
                count += 1
                pieces_taken[p] = piece
    return count, pieces_taken


def update_board(piece: str, coordinate: str, board: List) -> List[Dict]:
    """Updates the board by placing the given piece
    at the specified coordinate.
    """
    if type(piece) is str:
        for row in board:
            if coordinate in board[board.index(row)]:
                board[board.index(row)][coordinate] = piece
                return board
    return board


def validate_input(
    user_input: str, color: str, chess_board: List[Dict]
) -> Union[str, List, bool]:
    """Validates the user input
    and returns the correct move or an error message.
    """
    user_input = user_input.strip().lower()

    if user_input == "done":
        if not is_piece_on_board(WHITE_PIECES, chess_board):
            print_info("failed_exit", COLORS["W"])
            return False
        if not is_piece_on_board(BLACK_PIECES, chess_board):
            print_info("failed_exit", COLORS["B"])
            return False
        return "exit"

    if color == COLORS["W"]:
        if " " not in user_input:
            print_info("incorrect", color)
            return False

        chess_piece, coordinate = user_input.split(" ")

        if not any(chess_piece in piece for piece in WHITE_PIECES) or not any(
            coordinate in row for row in chess_board
        ):
            print_info("incorrect", color)
            return False
        if any(row.get(coordinate) == "" for row in chess_board):
            return [chess_piece, coordinate]

    if color == COLORS["B"]:
        coordinate = user_input
        if not any(coordinate in row for row in chess_board):
            print_info("incorrect", color)
            return False
        if any(row.get(coordinate) == "" for row in chess_board):
            return coordinate

    print_info("coordinate_full")
    return False


def is_piece_on_board(chess_pieces: List[Dict], chess_board: List[Dict]) -> bool:
    """Checks if at least one piece of the given type is on the board."""
    for row in chess_board:
        for piece in chess_pieces:
            if list(piece.keys())[0] in row.values():
                return True
    return False


def get_all_w_moves(input_for_white: List, board: List[Dict]) -> Tuple[Dict, Dict]:
    """Gets all possible white chess piece moves until
    the first possible takedown of a black chess piece
    """
    piece, coordinate = input_for_white[:2]
    moves = []
    max_range = 0

    for w_piece in WHITE_PIECES:
        if piece in w_piece:
            moves = list(w_piece.values())[0]["directions"]
            max_range = list(w_piece.values())[0]["range"]

    possible_moves = {
        "horizontal": [],
        "vertical": [],
        "diagonal": [],
        "anti_diagonal": [],
    }
    # Flatten the board, makes it easier to find stuff in it
    flat_board = get_flat_board(board)
    # Horizontal row
    h_row = next(row for row in board if coordinate in row)
    h_row_values = list(h_row.keys())
    h_index = h_row_values.index(coordinate)

    # Vertical row
    v_row = [list(row.keys())[h_index] for row in board]
    v_index = v_row.index(coordinate)

    main_diag, anti_diag = get_diagonal_moves(coordinate, board)

    # Main diagonal
    d_index = main_diag.index(coordinate) if coordinate in main_diag else None

    # Anti-diagonal
    a_d_index = anti_diag.index(
        coordinate) if coordinate in anti_diag else None

    if "horizontal" in moves:
        possible_moves["horizontal"] = get_coords_in_range(
            h_index, h_row_values, max_range, flat_board, piece
        )
    if "vertical" in moves:
        possible_moves["vertical"] = get_coords_in_range(
            v_index, v_row, max_range, flat_board, piece
        )
    if "diagonal" in moves and d_index is not None:
        possible_moves["diagonal"] = get_coords_in_range(
            d_index, main_diag, max_range, flat_board, piece
        )
    if "diagonal" in moves and a_d_index is not None:
        possible_moves["anti_diagonal"] = get_coords_in_range(
            a_d_index, anti_diag, max_range, flat_board, piece
        )
    return possible_moves, flat_board


def get_flat_board(board: List[Dict]) -> Dict:
    """Flattens the List of Dictionaries and returns a singular Dictionary"""
    return {k: v for row in board for k, v in row.items()}


def get_diagonal_moves(coordinate: str, board: List[Dict]) -> Tuple[List, List]:
    """Returns all possible diagonal and reversed diagonal coordinates"""
    col, row = coordinate[0], int(coordinate[1])
    col_index = ord(col) - ord("a")
    row_index = 8 - row

    main_diag = []
    anti_diag = []

    # Traverse board to find diagonal positions
    for i in range(len(board)):
        row_keys = list(board[i].keys())

        # Main diagonal
        if 0 <= i - row_index + col_index < len(row_keys):
            main_diag.append(row_keys[i - row_index + col_index])

        # Anti-diagonal
        if 0 <= row_index + col_index - i < len(row_keys):
            anti_diag.append(row_keys[row_index + col_index - i])
    return main_diag, anti_diag


def get_coords_in_range(
    index: int, line: List, max_range: int, board: Dict, piece_type: str
) -> List:
    """Gets the final list of all possible moves, using the index as a starting
    point on the provided list and then iterates left and right sides,
    breaking at first black chess piece
    """
    moves = []
    # Left side
    first_half = line[:index]
    first_half = first_half[::-1]  # reversed
    for item in first_half:
        current_item_index = line.index(item)
        if index - max_range <= current_item_index < index:
            piece = board.get(item)
            if piece != "" and piece != piece_type:
                moves.append(item)
                break
            if piece == "":
                moves.append(item)
    # Right side
    for item in line:
        current_item_index = line.index(item)
        if index < current_item_index <= index + max_range:
            piece = board.get(item)
            if piece != "" and piece != piece_type:
                moves.append(item)
                break
            if piece == "":
                moves.append(item)
    return moves


def take_input(color: str, chess_board: List[Dict]) -> Union[str, List, bool]:
    """Takes user input for a move and validates it."""
    failed_attempts = 0
    while True:
        user_input = input(f"Enter your {color} piece: ")
        if user_input := validate_input(user_input, color, chess_board):
            if user_input == "exit":
                return user_input
            else:
                print_info("correct", color)
                return user_input
        else:
            failed_attempts += 1
            if failed_attempts == 3:
                sys.exit("You failed 3 times in a row dummy, I quit!")
            continue


def print_info(
    info_type: str,
    color: Optional[str] = None,
    score: Optional[int] = None,
    pieces_taken: Optional[Dict] = None,
) -> None:
    """Prints formatted information messages based on the program state."""
    output = ""

    match info_type:
        case "correct":
            output = f"\tYour {color} piece has been successfully added!"
        case "incorrect":
            output = f"\tFailed to add: {color} piece, try the required format:"
            if color == COLORS["W"]:
                output += "\n\t\tWhite piece example: Knight b8"
            else:
                output += "\n\t\tBlack piece example: c2"
        case "failed_exit":
            output = f"\tFailed to exit: missing at least one {color} piece on board"
            if color == COLORS["W"]:
                output += f"\n\t\t\tmissing at least one {COLORS['B']} piece."
        case "coordinate_full":
            output = "\tThis coordinate is already taken!"
        case "result":
            if pieces_taken:
                output = f"Pieces taken ({score}):"
                for pos, piece in pieces_taken.items():
                    output += f"\n\t{pos}: {piece}"
            else:
                output = "No pieces taken."
        case "intro":
            pieces_list = ""
            available_pieces = [list(item.keys())[0] for item in WHITE_PIECES]
            for index in range(len(available_pieces)):
                pieces_list += f"\t{index + 1}) {available_pieces[index]}\n"
            output = f"""
    Choose a white piece to place on the board:
    {pieces_list}
    Enter the piece name and its coordinates (e.g., Queen c5)

    For black pieces, enter only the coordinates (e.g., c3)
    Add up to 16 pieces or type 'Done' to finish after placing at least one"""
        case _:
            output = "Unexpected info_type"

    print(output)


def draw_chess_board(board: Dict) -> None:
    """Prints out a formatted chess board."""
    files = "   " + "   ".join(
        [f"{chr(c)}".center(8) for c in range(ord("a"), ord("h") + 1)]
    )
    print(files)
    print("   " + "-" * 87)
    for rank in range(8, 0, -1):
        row_display = []
        for file in "abcdefgh":
            coord = f"{file}{rank}"
            piece = board.get(coord, " ")
            row_display.append(piece.center(8))
        print(f"{rank} | " + " | ".join(row_display) + " |")
        print("   " + "-" * 87)


if __name__ == "__main__":
    main()
