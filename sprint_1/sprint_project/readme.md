# A Chess Question

## Description

*A Chess Question* is a Python-based chess simulation where a user places white pieces on a board and the program randomly generates black pieces. The game calculates valid moves for the selected white piece and determines how many black pieces it can capture.

## Features

- Allows the user to place one white piece on the board.
- Asks to place 1-16 black pieces and then randomly picks chess pieces.
- Calculates all possible moves for the selected white piece.
- Determines the number of black pieces that can be captured.
- Displays a chessboard with the current game state.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/TuringCollegeSubmissions/ertamos-DS.v3.1.1.6
   cd ertamos-DS.v3.1.1.6
   ```

2. Ensure you have Python installed (version 3.6+ recommended).

3. Run the program:
   ```bash
   python a_chess_question.py
   ```
## Usage

1. Choose a white piece from the available options and provide its starting position.
   ```
   Example: Queen d4
   ```

2. The program will then ask you to place up to 16 black pieces at your given position but randomly select a piece.

3. The board will be displayed, showing all pieces.

4. The program calculates possible moves for the white piece and determines how many black pieces can be captured.

## Files

- `a_chess_question.py` – Main game logic and functions.
- `constants.py` – Contains piece definitions and the chessboard structure.

## Example Output

```
Choose a white piece to place on the board:
	1) queen
	2) king
	3) bishop
	4) rook

Enter the piece name and its coordinates (e.g., Queen c5)

For black pieces, enter only the coordinates (e.g., c3)
Add up to 16 pieces or type 'Done' to finish after placing at least one.
```

```
Pieces taken (3):
	d5: b_pawn
	f6: b_knight
	g7: b_rook
```
