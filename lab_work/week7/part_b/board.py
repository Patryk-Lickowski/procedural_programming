
def create_board() -> list[list[str | None]]:
    return [[None for _ in range(3)] for _ in range(3)]

def display_board(board):
    for row_index, row in enumerate(board):
        formatted_row = [cell if cell is not None else " " for cell in row]
        print(" | ".join(formatted_row))
        if row_index < 2:
            print("-" * 9)

def is_valid_move(board, row, col):
    # Check if the row and column selection are in range of the board
    if row not in range(3) or col not in range(3):
        return False

    # Check if the selected square is empty
    if board[row][col] is not None:
        return False
    return True


def make_move(board, row, col, player):
    # Check if the move is valid using existing function
    if is_valid_move(board, row, col):
        # Move is valid therefore add player move
        board[row][col] = player
        return True
    return False

def check_rows(board, player):
    # For each row check if every cell is the same symbol
    for col in range(3):
        if all(cell == player for cell in board[col]):
            return True
        return False

def check_columns(board, player):
    # For each column check if every cell is the same symbol
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
        return False

def check_diagonals(board, player):
    # For every coordinate where both numbers are the same e.g. (0,0), (1,1) check if all symbols are the same
    for col in range(3):
        if all(board[i][i] == player for i in range(3)):
            return True
        if all(board[i][2 - 1] == player for i in range(3)):
            return True
        return False

def check_winner(board, player):
    # If any of the checks return True, return True as game is won
    return check_rows(board, player) or check_columns(board, player) or check_diagonals(board, player)

def check_draw(board):
    # If any spaces are None return False as player can make a move
    for row in board:
        if None in row:
            return False
    return True
