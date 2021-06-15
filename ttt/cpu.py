import pygame as pg, sys
import copy

import random
from ttt.game import Game

# custom type that shows the x and y coordinates of the cell (x,y).
_move = (int, int)

class Cpu:
    '''
    Provides functions and other tools for the computer player logic.

    '''

    def __init__(self, game: Game):
        '''
        Constructor for the Cpu class.

        Params:
            game (Game): Reference to a game object. A deep-copy is taken as an
            instance variable.
        '''
        # make a copy of the ongoing game instead of ruining it
        self._game = copy.deepcopy(game)


    def find_best_move(self) -> _move :
        '''
        Find the best possible move for the current game by starting the
        recursive _min_max() call chain.

        Returns:
            move (_move): A (row, col) list representing the best move.
        '''

        # Calculate the random row and col
        rand_rows = random.sample([1, 2, 3], 3)
        rand_cols = random.sample([1, 2, 3], 3)

        for row in rand_rows:
            for col in rand_cols:
                # If a move can be placed, return those values
                if self._game.place_move(row, col):
                    _move = (row,) + (col,)
                    return _move

    def _min_max(self, depth: str, min_max: bool) -> int:
        '''
        Simulate all possible moves of the board and return the score once the
        simulation is finished.

        Parameters:
            depth (str): Current depth of the recursive call.
            min_max (bool): Whether the current run is being calculated for the
                            the maximizer

        Returns:
            score (int): Negative for minimizer win, positive for maximizer win.
        '''
        pass


    def _evaluate_game(self) -> int:
        '''
        Evaluate the finished game and return an appropriate score.

        Returns:
            score (int): The score of the finished game.
                         - Negative = Minimizer wins
                         - Positive = Maximizer wins
                         - Zero = Draw (confirm this with Brandon
        '''
        pass
