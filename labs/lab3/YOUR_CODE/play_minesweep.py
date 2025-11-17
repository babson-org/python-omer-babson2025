
import os, sys, random


_here = os.path.dirname(__file__)                          
game_dir = _here if os.path.basename(_here) != "__pycache__" else os.path.dirname(_here)
lab_dir = os.path.dirname(game_dir)                        
if lab_dir not in sys.path:
    sys.path.insert(0, lab_dir)

import globals  
from YOUR_CODE.initialize_board import initialize_board
from YOUR_CODE.place_random_mines import place_random_mines
from YOUR_CODE.count_adjacent_mines import count_adjacent_mines
from YOUR_CODE.update_board import update_board
from YOUR_CODE.game_won import game_won

try:
    MINE = globals.MINE
except AttributeError:
    MINE = globals.MINES
HIDDEN = getattr(globals, "HIDDEN", "♦")
BOOM   = getattr(globals, "BOOM", "*")
FLAG   = getattr(globals, "FLAG", "⚑")  

def print_board(board, flagged: set[tuple[int,int]]):
    rows, cols = len(board), len(board[0])
    print("\n    " + " ".join(f"{c:>2}" for c in range(cols)))
    print("   +" + "---" * cols + "+")
    for r in range(rows):
        row_out = []
        for c in range(cols):
            ch = FLAG if (r, c) in flagged and board[r][c] == HIDDEN else board[r][c]
            row_out.append(f"{ch:>1}")
        print(f"{r:>2} | " + " ".join(row_out) + " |")
    print("   +" + "---" * cols + "+\n")

def print_base(b):
    print("\n# DEBUG base (mines=*)")
    for row in b:
        print(" ".join("*" if x == MINE else str(x) for x in row))
    print()

def parse_coords(text: str):
    """Accept 'r c', 'r,c', or '(r,c)'. Return (r,c) or None on failure."""
    clean = text.replace("(", "").replace(")", "").replace(",", " ").strip()
    parts = clean.split()
    if len(parts) != 2:
        return None
    try:
        return int(parts[0]), int(parts[1])
    except Exception:
        return None

def main():
    rows, cols, mines = 6, 8, 8

    random.seed()  
    base = initialize_board(rows, cols, 0)
    place_random_mines(base, mines)
    count_adjacent_mines(base)
    display = [[HIDDEN for _ in range(cols)] for _ in range(rows)]
    flagged: set[tuple[int,int]] = set() 

    while True:
        print_board(display, flagged)
        raw = input(
    "Your move → type row col (e.g., 2 3). "
    "Type 'debug' to peek or 'quit' to exit: "
).strip().lower()

        if raw in {"quit"}:
            print("bye!")
            break
        if raw in {"debug"}:
            print_base(base)
            continue

        # toggle flag: command starts with 'f'
        if raw.startswith("f"):
            coords = parse_coords(raw[1:].strip())
            if coords is None:
                print("Flag format: f 2 3 (or f 2,3)"); continue
            r, c = coords
            if not (0 <= r < rows and 0 <= c < cols):
                print("Out of bounds."); continue
            if display[r][c] != HIDDEN:
                print("Cannot flag revealed cells."); continue
            if (r, c) in flagged:
                flagged.remove((r, c))
            else:
                flagged.add((r, c))
            continue

            
        coords = parse_coords(raw)
        if coords is None:
            print("Enter two integers like: 2 3"); continue
        r, c = coords
        if not (0 <= r < rows and 0 <= c < cols):
            print("Out of bounds."); continue
        if (r, c) in flagged:
            print("Cell is flagged. Unflag first: f", r, c); continue
        if display[r][c] != HIDDEN:
            print("Already revealed."); continue

        status = update_board(base, display, r, c)
        if status == "mine":
            # reveal all mines for final board
            for rr in range(rows):
                for cc in range(cols):
                    if base[rr][cc] == MINE:
                        display[rr][cc] = BOOM
            print_board(display, flagged)
            print("💥 Boom!")
            break
        if game_won(base, display):
            print_board(display, flagged)
            print("🎉 You win!")
            break

if __name__ == "__main__":
    main()
