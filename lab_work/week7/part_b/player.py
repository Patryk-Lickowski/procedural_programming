from board import is_valid_move

def get_player_move(board, player):
    while True:
        # Get player input for row and column
        try:
            row = int(input(f"Player {player}, enter row (0-2): "))
            col = int(input(f"Player {player}, enter column (0-2): "))
            # Check if the move is valid
            if is_valid_move(board, row, col):
                return row, col
            else:
                print("Invalid move. Make sure the square is on the board and empty.")
        # If a character is input, return error
        except ValueError:
            print("Invalid input. Please enter numbers only.")


def switch_player(player):
    # If the current player is O switch to X else switch to X
    return 'O' if player == 'X' else 'X'
