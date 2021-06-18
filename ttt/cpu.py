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

        # # For when CPU start working, this would be the call for _min_max:
        # bestVal = -1000
        # bestMove = (-1, -1)

        # # Traverse all cells, evaluate minimax function
        # for i in range(3) :
        #     for j in range(3) :

        #         # Check if cell is empty
        #             if (self._game._board[i][j] == None) :

        #                 # Make a move
        #                 self._game._board[i][j] = self._game.player

        #                 # Compute if it was a good move
        #                 moveValuation = self._min_max(0, False)

        #                 # Undo the move
        #                 board[i][j] = None

        #                 # If the value of the current move is better, store it
        #                 if (moveValuation > bestVal) :
        #                     bestMove = (i, j)
        #                     bestVal = moveVal

        # return bestMove

    def _min_max(self, depth: int, min_max: bool) -> int:
        '''
        Simulate all possible moves of the board and return the score once the
        simulation is finished.

        Parameters:
            depth (int): Current depth of the recursive call.
            min_max (bool): Whether the current run is being calculated for the
                            the maximizer

        Returns:
            score (int): Negative for minimizer win, positive for maximizer win.
        '''
        score = self._evaluate_game()

        # If max has won the game
        if (score == 10):
            return score

        # If min has won the game
        if (score == -10):
            return score

        # If there are no more moves and no winner, than tie
        if (self.isMovesLeft() == False):
            return 0

        # If this max's move
        if (min_max):
            best = -1000

            # Look through the board
            for i in range(3) :        
                for j in range(3) :
                    # Check if cell is empty
                    if (self._game._board[i][j] == None) :
                    
                        # Make the move
                        self._game._board[i][j] = self._game.player
    
                        # Call minimax recursively and choose the maximum value
                        best = max(best, self._min_max(depth + 1, not min_max))
    
                        # Undo the move
                        self._game._board[i][j] = None
            return best

        # If this min's move
        else :
            best = 1000
 
            # Traverse the board
            for i in range(3) :        
                for j in range(3) :
                
                    # Check if cell is empty
                    if (self._game._board[i][j] == None) :
                    
                        # Make the move and place the opponent's
                        self._game._board[i][j] = self._game.get_opponent()
    
                        # Call minimax recursively and choose the minimum value
                        best = min(best, self._min_max(depth + 1, not min_max))
    
                        # Undo the move
                        board[i][j] = None
            return best

    def _evaluate_game(self) -> int:
        '''
        Evaluate the finished game and return an appropriate score.

        Returns:
            score (int): The score of the finished game.
                         - Negative = Minimizer wins
                         - Positive = Maximizer wins
                         - Zero = Draw (confirm this with Brandon
        '''
        # Checking for Rows for X or O victory
        for row in range(3) :
            if (self._game.board[row][0] == self._game.board[row][1] and self._game.board[row][1] == self._game.board[row][2]) :
                if (self._game.board[row][0] == self._game.player) :
                    return 10
                elif (self._game.board[row][0] == self._game.get_opponent()):
                    return -10

        # Checking for Columns for X or O victory
        for col in range(3) :
            if (self._game.board[0][col] == self._game.board[1][col] and self._game.board[1][col] == self._game.board[2][col]) :
                if (self._game.board[0][col] == self._game.player) :
                    return 10
                elif (self._game.board[0][col] == self._game.get_opponent()):
                    return -10

        # Checking for Diagonals for X or O victory
        if (self._game.board[0][0] == self._game.board[1][1] and self._game.board[1][1] == self._game.board[2][2]) :
            if (self._game.board[0][0] == self._game.player) :
                return 10
            elif (self._game.board[0][0] == self._game.get_opponent()) :
                return -10

        if (self._game.board[0][2] == self._game.board[1][1] and self._game.board[1][1] == self._game.board[2][0]) :
            if (self._game.board[0][2] == self._game.player) :
                return 10
            elif (self._game.board[0][2] == self._game.get_opponent()) :
                return -10

        # Else if none of them have won then return 0
        return 0

    # This function returns true if there are moves remaining
    def isMovesLeft(self) -> bool:
        for i in range(3) :
            for j in range(3) :
                if (self._game.board[i][j] == None):
                    return True
        return False
