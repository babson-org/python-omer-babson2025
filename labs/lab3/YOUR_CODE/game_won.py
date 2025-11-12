import globals

try:
    MINE = globals.MINE
except AttributeError:
    MINE = globals.MINES
HIDDEN = getattr(globals, "HIDDEN", "♦")

def game_won(base_board, display_board):
    """
    Return True iff every non-mine cell on base_board is revealed on display_board.
    A cell is 'unrevealed' if it equals HIDDEN.
    """
    rows, cols = len(base_board), len(base_board[0])
    for r in range(rows):
        for c in range(cols):
            if base_board[r][c] != MINE and display_board[r][c] == HIDDEN:
                return False
    return True

if __name__ == "__main__":  # tiny self-test
    try:
        from YOUR_CODE.initialize_board import initialize_board
    except ModuleNotFoundError:
        from initialize_board import initialize_board

    b = initialize_board(2, 2, 0)             # no mines
    d = [["1", "1"], [" ", "1"]]              # everything revealed
    print(game_won(b, d))                     # -> True

    d2 = [[HIDDEN, "1"], [" ", "1"]]          # one hidden safe cell
    print(game_won(b, d2))                    # -> False
