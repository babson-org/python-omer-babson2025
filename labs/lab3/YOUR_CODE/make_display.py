import globals
HIDDEN = getattr(globals, "HIDDEN", "♦")

def make_display(rows: int, cols: int):
    return [[HIDDEN for _ in range(cols)] for _ in range(rows)]
