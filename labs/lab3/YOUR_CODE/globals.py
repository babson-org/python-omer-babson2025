ROWS = None
COLS = None
MINES = None

def initialize_board(rows: int, cols: int, fill: int = 0):
    """Return rows x cols 2D list filled with `fill`."""
    return [[fill for _ in range(cols)] for _ in range(rows)]

import random, globals

def place_random_mines(board, num_mines: int):
    """Place `num_mines` mines (globals.MINE) in-place without duplicates."""
    rows, cols = len(board), len(board[0])
    assert 0 <= num_mines < rows * cols, "invalid number of mines"
    spots = [(r, c) for r in range(rows) for c in range(cols)]
    for r, c in random.sample(spots, k=num_mines):
        board[r][c] = globals.MINE

def get_adjacent_cells(r: int, c: int, rows: int, cols: int):
    """Yield valid neighbors in 8 directions."""
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            if dr == 0 and dc == 0:
                continue
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                yield nr, nc

import globals

def game_won(base_board, display_board):
    """True if every non-mine cell is revealed on display_board."""
    rows, cols = len(base_board), len(base_board[0])
    for r in range(rows):
        for c in range(cols):
            if base_board[r][c] != globals.MINE and display_board[r][c] == globals.HIDDEN:
                return False
    return True
