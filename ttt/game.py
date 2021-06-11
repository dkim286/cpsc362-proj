import pygame as pg, sys
from ttt.colors import WHITE
from ttt.dimensions import BOARD_WIDTH as width, BOARD_HEIGHT as height, TTT as board
from ttt.board import *
import time


DRAW = 'D'
UNDECIDED = 'N'

X = 'x'
O = 'o'

class Game:
    '''
    A class that represents the game's state.

    Handles everything with regards to the state of the game and modifying it,
    if applicable. 
    '''
    
    # Game Constructor
    def __init__(self):
        self._player = X
        self._board = [[None]*3,[None]*3,[None]*3]
    
        
    # Helper util to check the win state of the game.
    def win_checker(self) -> str:

        # check for winning rows
        for row in range (0,3):
            if ((board[row][0] == board[row][1] == board[row][2]) and(board[row][0] is not None)):
                return self._winner()
                
        # check for winning columns
        for col in range (0, 3):
            if (board[0][col] == board[1][col] == board[2][col]) and (board[0][col] is not None):
                return self._winner()

        # check for diagonal winners
        if (board[0][0] == board[1][1] == board[2][2]) and (board[0][0] is not None):
            return self._winner()
        if (board[0][2] == board[1][1] == board[2][0]) and (board[0][2] is not None):
            return self._winner()

        if(all([all(row) for row in board])):
            return DRAW

        return UNDECIDED

    # Helper util to reset the game state.
    def reset_game(self):
        time.sleep(3)
        self._player = X
        self._board = [[None]*3,[None]*3,[None]*3]
    
    # Helper util to place an X or O onto the chosen space within the board
    def place_move(self, row: int, col: int) -> bool:
        if self._board[row-1][col-1] == None:
            self._board[row-1][col-1] = self._player
            self._change_player()
            return True
        else:
            return False
            
    # Helper util to change the current active player
    def _change_player(self) -> None:
        if self._player == X:
            self._player = O
        else:
            self._player = X

    def _winner(self) -> str:
        if self._player == X:
            return O
        return X
