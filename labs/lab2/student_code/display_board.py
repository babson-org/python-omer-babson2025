from utils import clear_screen
def print_board(board: list[int]):
    """
        Display the Tic-Tac-Toe board with human-friendly layout.
        [10, 2, 3, 4, -10, 6, 7, 8, 10] ->

        X | 2 | 3
        ---------
        4 | O | 6
        ---------
        7 | 8 | X
    """
    
    def cell(value: int) -> str:
        # TODO: Return 'X' if value == 10
        if value == 10:
            return 'X'
        # TODO: Return 'O' if value == -10
        if value == -10:
            return 'O'
        # TODO: Otherwise, return str(value)
        return str(value)
        
    clear_screen()          
    print()                 

    # TODO: Loop through rows
    for row in range(3):
        # TODO: For each row, print formatted board row using cell()
        row_values = [cell(board[row*3 + col]) for col in range(3)]
        print('   |   |   ')
        print(f' {row_values[0]} | {row_values[1]} | {row_values[2]} ')
        print('   |   |   ')
        if row < 2:
            print('-----------')
    print()
