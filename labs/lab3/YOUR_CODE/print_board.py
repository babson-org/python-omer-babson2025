def print_board(board: list, level: int):
    '''
    board = [
        [(' ♦', '💣'), (' ♦', '💣'), (' ♦', 1),
         (' ♦', '   '), (' ♦', '   '), (' ♦', '   ')],
        [(' ♦', 2), (' ♦', 2), (' ♦', 1),
         (' ♦', '   '), (' ♦', '   '), (' ♦', '   ')],
        [(' ♦', '   '), (' ♦', '   '), (' ♦', '   '),
         (' ♦', '   '), (' ♦', '   '), (' ♦', '   ')],
    ]
    '''
    
    line_hash = '|-----'

    # Print column indexes
    print('      ', end='')
    for idx in range(globals.COLS):
        print(f'  {idx:2}  ', end='')  # Adjust column width for alignment

    print(f'\n      {line_hash * globals.COLS}|')

    # Loop through each row and print cells
    for row in range(globals.ROWS):
        print(f'  {row:2}   ', end='')  # Adjust row index width
        for col in range(globals.COLS):
            symbol = board[row][col][level]

            # Print the symbol, ensuring alignment
            print(f'| {symbol:3} ', end='')  # Consistent width (3 spaces)

        print('|')
        print(f'      {line_hash * globals.COLS}|')