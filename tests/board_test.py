import pytest

from ttt.board import Board


def test_board_drawToken():
    board = Board()
    x = board.drawToken('x')
    y = board.drawToken('y')
    assert x == y

# test board columns.
def test_board_columns():
    '''
    Test the formation columns in the game board 2d matrix..

    Note : The result here is casted to tuple when values of the columns are
    extracted through zip. But the values and dimension should remain equal.
    '''
    board = [[None]*3, [None]*3, [None]*3]
    columns = list(zip(*board))
    expected_columns = [(None, None, None), (None, None, None), (None, None, None)]
    assert columns == expected_columns

# test the diagonals of the board.
def test_board_diagonals():
    board = Board()
    pass

# test the rows of the board.
def test_board_rows():
    '''
    Test the formation rows in the game board 2d matrix.

    '''
    board = [[None]* 3, [None] * 3, [None] * 3]
    rows = []
    for row in board:
        rows.append(row)
    expected_rows = [[None, None, None], [None, None, None], [None, None, None]]
    assert rows == expected_rows
