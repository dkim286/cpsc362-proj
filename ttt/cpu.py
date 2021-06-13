import pygame as pg, sys
from ttt.dimensions import *

class Cpu:
    '''
    Provides functions and other tools for the computer player logic.

    '''

    # CPU Constructor
    def __init__(self, x : int, y : int):
        self._move = (x,y)

    def find_best_move(self, depth: int) :
        pass

    def _min_max(self):
        pass

    def _evaluate_game(self):
        pass
