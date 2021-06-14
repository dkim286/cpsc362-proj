import pygame as pg, sys
from ttt.dimensions import *

# custom type that shows the x and y coordinates of the cell (x,y).
_move = (int, int)

class Cpu:
    '''
    Provides functions and other tools for the computer player logic.

    '''

    # CPU Constructor
    def __init__(self, x : int, y : int):
        self._move = (x,y)

    # helper util to find the next possible move for the cpu player.
    def find_best_move(self, depth: int) -> _move :
        pass

    # helper util to find the next cell for the game.
    def _min_max(self) -> int:
        pass

    # helper util to evaluate the game state.
    def _evaluate_game(self) -> int:
        pass
