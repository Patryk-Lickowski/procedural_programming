# test_tictactoe.py
from board import (
    create_board,
    is_valid_move,
    make_move,
    check_rows,
    check_columns,
    check_diagonals,
    check_winner,
    check_draw,
)
from player import switch_player


def test_create_board():
    board = create_board()
    assert len(board) == 3
    assert all(len(row) == 3 for row in board)
    assert all(cell is None for row in board for cell in row)


def test_is_valid_move():
    board = create_board()
    assert is_valid_move(board, 0, 0) is True
    assert is_valid_move(board, 3, 0) is False   # Out of bounds
    assert is_valid_move(board, -1, 1) is False  # Negative index

    board[1][1] = "X"
    assert is_valid_move(board, 1, 1) is False  # Already occupied


def test_make_move():
    board = create_board()
    assert make_move(board, 0, 2, "X") is True
    assert board[0][2] == "X"
    assert make_move(board, 0, 2, "O") is False  # Cannot overwrite X
    assert board[0][2] == "X"


def test_check_winner():
    # Row win
    row_board = [
        ["X", "X", "X"],
        [None, "O", None],
        ["O", None, None],
    ]
    assert check_rows(row_board, "X") is True
    assert check_winner(row_board, "X") is True
    assert check_winner(row_board, "O") is False

    # Column win
    col_board = [
        ["O", "X", None],
        ["O", "X", None],
        ["O", None, "X"],
    ]
    assert check_columns(col_board, "O") is True
    assert check_winner(col_board, "O") is True

    # Diagonal win
    diag_board = [
        ["X", "O", None],
        ["O", "X", None],
        [None, None, "X"],
    ]
    assert check_diagonals(diag_board, "X") is True
    assert check_winner(diag_board, "X") is True


def test_check_draw():
    full_board = [
        ["X", "O", "X"],
        ["X", "O", "O"],
        ["O", "X", "X"],
    ]
    assert check_draw(full_board) is True

    unfinished_board = create_board()
    assert check_draw(unfinished_board) is False


def test_switch_player():
    assert switch_player("X") == "O"
    assert switch_player("O") == "X"
