def get_adjacent_cells(r: int, c: int, rows: int, cols: int):
    """Yield valid neighbors in 8 directions."""
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            if dr == 0 and dc == 0:
                continue
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                yield nr, nc

if __name__ == "__main__":
    print(sorted(get_adjacent_cells(0, 0, 3, 4)))  # corners
    print(sorted(get_adjacent_cells(1, 1, 3, 4)))  # middle
