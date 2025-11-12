import globals

try:
    from YOUR_CODE.get_adjacent_cells import get_adjacent_cells
except ModuleNotFoundError:
    from get_adjacent_cells import get_adjacent_cells

try:
    MINE = globals.MINE
except AttributeError:
    MINE = globals.MINES

def count_adjacent_mines(board):
    rows, cols = len(board), len(board[0])
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == MINE:
                continue
            cnt = 0
            for nr, nc in get_adjacent_cells(r, c, rows, cols):
                if board[nr][nc] == MINE:
                    cnt += 1
            board[r][c] = cnt

if __name__ == "__main__":
    # import the sibling directly when running this file
    try:
        from YOUR_CODE.initialize_board import initialize_board
    except ModuleNotFoundError:
        from initialize_board import initialize_board

    b = initialize_board(3, 4, 0)
    # place two test mines
    b[0][0] = MINE
    b[1][2] = MINE
    count_adjacent_mines(b)
    for row in b:
        print(row)
