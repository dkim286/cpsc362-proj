import pytest
import pygame as pg, sys
from ttt.colors import WHITE
from ttt.dimensions import BOARD_WIDTH as width, BOARD_HEIGHT as height, TTT as board
from ttt.board import Board
from ttt.game import Game

# test the game status.
def test_update_board():
    board = Board()


# test the column win scenario.
def test_check_column_win(self):
    board = [['O', 'O', 'O'], [None, None, None], [None, None, None]]
    pass

# test the row win scenario.
def test_check_row_win(self):
    board = [['X', None, None], ['X', None, None], ['X', None, None]]
    pass

# test the diagonal win scenario.
def test_check_first_diagonal_win(self):
    board = [['X', None, None], [ None, 'X', None], [None, None, 'X']]
    pass

# test the second diagonal win scenario.
def test_check_second_diagonal_win(self):
    board = [[None, None, 'O'], [None, 'O', None], ['O', None, None]]
    pass
