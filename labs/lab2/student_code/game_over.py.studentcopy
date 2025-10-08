from calc_score import calc_score
def game_over(board: list[int]):
    """
        After every move (see play_game) we check to see if the game 
        is over.  The game is over if calc_score() returns 30 or -30
        or if ther are no open moves left on the board
        Returns True if the game has a winner or no remaining moves, False otherwise.
    """
    
    # TODO: Check if all cells are filled (abs(cell) == 10)
    all_filled = all(abs(cell) == 10 for cell in board)

    # TODO: Use calc_score to check if someone has won
    score = calc_score(board)

    # TODO: Return True if game over, otherwise False
    if score == 30 or score == -30:
        return True
    if all_filled:
        return True
    return False

    


