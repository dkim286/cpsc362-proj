import pytest

from ttt.board import Board


def test_board_drawToken():
    board = Board()
    x = board.drawToken('x')
    y = board.drawToken('y')
    assert x == y

