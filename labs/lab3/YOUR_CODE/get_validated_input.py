def get_validated_input(prompt: str, rows: int, cols: int, revealed: set[tuple[int,int]]):
    """
    Ask until the user enters a valid (row, col) inside bounds
    and not already revealed. Accepts 'r c' or 'r,c'.
    """
    while True:
        raw = input(prompt).strip()
        try:
            r, c = map(int, raw.replace(",", " ").split())
            if 0 <= r < rows and 0 <= c < cols and (r, c) not in revealed:
                return r, c
            else:
                print("Out of bounds or already revealed. Try again.")
        except Exception:
            print("Invalid input. Enter two integers like: 2 3")
