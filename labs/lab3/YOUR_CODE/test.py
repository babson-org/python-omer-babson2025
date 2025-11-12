# labs/lab3/test.py
import globals

from YOUR_CODE.initialize_board import initialize_board
from YOUR_CODE.place_random_mines import place_random_mines
from YOUR_CODE.count_adjacent_mines import count_adjacent_mines
from YOUR_CODE.update_board import update_board
from YOUR_CODE.game_won import game_won

HIDDEN = getattr(globals, "HIDDEN", "♦")
try:
    MINE = globals.MINE
except AttributeError:
    MINE = globals.MINES

def dump(title, grid):
    print("\n" + title)
    for r in grid:
        print(" ".join(str(x) for x in r))

def main():
    rows, cols, mines = 6, 8, 8
    base = initialize_board(rows, cols, 0)
    place_random_mines(base, mines)
    count_adjacent_mines(base)
    display = [[HIDDEN for _ in range(cols)] for _ in range(rows)]

    # click a few safe-ish cells
    for r, c in [(0,0), (rows//2, cols//2), (rows-1, cols-1)]:
        if base[r][c] != MINE:
            print("click", (r, c), "->", update_board(base, display, r, c))

    dump("DISPLAY", display)
    print("won?", game_won(base, display))

if __name__ == "__main__":
    main()
