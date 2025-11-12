def initialize_board(rows: int, cols: int, fill: int = 0):
    """Return rows x cols 2D list filled with `fill`."""
    return [[fill for _ in range(cols)] for _ in range(rows)]
def initialize_board(rows: int, cols: int, fill: int = 0):
    return [[fill for _ in range(cols)] for _ in range(rows)]

if __name__ == "__main__":  
    b = initialize_board(3, 4, 0)
    print(b)
