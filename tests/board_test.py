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
    '''
    Test the 2 possible diagonal vectors in the game board 2d matrix.

    '''
    board = [[None]*3, [None]*3, [None]*3]
    expected_diagonalRTL = [None, None, None]
    expected_diagonalLTR = [None, None, None]
    diagonal_LTR = []
    diagonal_RTL = []
    for row in range(len(board)):
        for col in range(len(row)):
            if row == col:
                # primary diagonal where row == col.
                diagonal_LTR.append(board[row][col])
            if ((row+col) == 3 - 1):
                # secondary diagonal where row+col == n - 1 where n is the length
                # of board.
                diagonal_RTL.append(board[row][col])
    assert expected_diagonalLTR == diagonal_LTR
    assert expected_diagonalRTL == diagonal_RTL

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
