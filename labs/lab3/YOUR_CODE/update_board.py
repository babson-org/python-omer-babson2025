from collections import deque
import globals

try:
    from YOUR_CODE.get_adjacent_cells import get_adjacent_cells
except ModuleNotFoundError:
    from get_adjacent_cells import get_adjacent_cells

# mine + symbols from prof globals
try:
    MINE = globals.MINE
except AttributeError:
    MINE = globals.MINES

HIDDEN = getattr(globals, "HIDDEN", "♦")
BOOM   = getattr(globals, "BOOM",   "*")

def update_board(base_board, display_board, r: int, c: int):
    """
    Reveals cell (r,c) on display_board using base_board values.
    Returns: 'mine' (hit a mine), 'ok' (revealed), or 'noop' (already revealed).
    """
    rows, cols = len(base_board), len(base_board[0])

    if display_board[r][c] != HIDDEN:
        return "noop"

    if base_board[r][c] == MINE:
        display_board[r][c] = BOOM
        return "mine"

    def reveal(rr, cc):
        val = base_board[rr][cc]
        display_board[rr][cc] = " " if val == 0 else str(val)

    # single number
    if base_board[r][c] > 0:
        reveal(r, c)
        return "ok"

    # flood-fill zeros + border numbers
    q = deque([(r, c)])
    while q:
        cr, cc = q.popleft()
        if display_board[cr][cc] != HIDDEN:
            continue
        reveal(cr, cc)
        if base_board[cr][cc] == 0:
            for nr, nc in get_adjacent_cells(cr, cc, rows, cols):
                if display_board[nr][nc] == HIDDEN and base_board[nr][nc] != MINE:
                    if base_board[nr][nc] == 0:
                        q.append((nr, nc))
                    else:
                        reveal(nr, nc)
    return "ok"

if __name__ == "__main__":
    # tiny sanity test
    try:
        from YOUR_CODE.initialize_board import initialize_board
        from YOUR_CODE.count_adjacent_mines import count_adjacent_mines
    except ModuleNotFoundError:
        from initialize_board import initialize_board
        from count_adjacent_mines import count_adjacent_mines

    base = initialize_board(4, 5, 0)
    base[0][0] = MINE; base[2][3] = MINE  # deterministic mines
    count_adjacent_mines(base)
    display = [[HIDDEN for _ in range(5)] for _ in range(4)]

    print(update_board(base, display, 3, 4))  # likely 0 → flood-fill
    for row in display: print(row)
