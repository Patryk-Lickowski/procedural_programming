# main.py
from board import (
    create_board,
    display_board,
    make_move,
    check_winner,
    check_draw
)
from player import get_player_move, switch_player

def play_game():
    # Create the board and set the current player to X
    board = create_board()
    current_player = 'X'

    while True:
        # Display the board
        display_board(board)
        # Get player input
        row, col = get_player_move(board, current_player)
        # If making the move is succesful, and the win condition has been met, display win message
        if make_move(board, row, col, current_player):
            if check_winner(board, current_player):
                display_board(board)
                print(f"Player {current_player} wins!")
                break
            # If the draw condition has been met, display draw message
            if check_draw(board):
                display_board(board)
                print("It's a draw!")
                break
        # Switch players
        current_player = switch_player(current_player)

if __name__ == '__main__':
    play_game()
