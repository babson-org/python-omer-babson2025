def calc_score(board: list[int]):
    """
        Determines if there's a winner on the board.
        Returns 30 if X wins, -30 if O wins, 0 otherwise.
         
        there are 8 ways to win: 3 rows, 3 columns, 2 diagnols
        if the cells in a row, column or diagnol add up to 30 return 30
        if they add upto -30 return -30
        else return 0
    """

    #  Indices reference:
    #    0 1 2
    #    3 4 5
    #    6 7 8

    def line_sum(a, b, c):
        '''
            line_sum takes 3 numbers and if the sum is either 30
            or -30 returns that sum otherwise do not return
        '''         

        # TODO: Sum the values at board[a], board[b], board[c] 
        s = board[a] + board[b] + board[c]

        # TODO: Return 30 if X wins, -30 if O wins otherwise do not return
        if s == 30 or s == -30:
            return s
        # (implicit None otherwise)

    # TODO: For each of the 8 ways to win
    lines = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
        (0, 4, 8), (2, 4, 6)              # diagonals
    ]

    # TODO: Check the cells in each row, column, or diagonal using line_sum
    for a, b, c in lines:
        res = line_sum(a, b, c)
        if res is not None:
            return res

    # TODO: Return 0 if line_sum() didn't return 30 or -30
    return 0
