import pygame as pg, sys
import copy

from random import random
from ttt.game import Game

# custom type that shows the x and y coordinates of the cell (x,y).
_move = list[int, int]

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
        row = random.randint(1,3)
        col = random.randint(1,3)

        # If the CPU can not place a token, restart the function
        if(not self._game.place_move(row, col)):
            self.find_best_move()

        # If a move can be placed, return those values
        else:
            _move.append(row)
            _move.append(col)
            return _move


    def _min_max(self, min_max: bool) -> int:
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
