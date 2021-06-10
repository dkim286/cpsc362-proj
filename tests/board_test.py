import pytest

from ttt.board import Board


def test_board_drawToken():
    board = Board()
    x = board.drawToken('x')
    y = board.drawToken('y')
    assert x == y

# test board columns.
def test_board_columns():
    board = Board()
    pass

# test the diagonals of the board.
def test_board_diagonals():
    board = Board()
    pass

# test the rows of the board.
def test_board_rows():
    board = Board()
    pass
