import pygame as pg, sys
from ttt.colors import WHITE
from ttt.dimensions import BOARD_WIDTH as width, BOARD_HEIGHT as height, TTT as board
from ttt.boards import *
import time

class Game:
    '''
    A class that represents the game's state.

    Handles everything with regards to the state of the game and modifying it,
    if applicable. 
    '''
    # Global Variables
    XO = 'x'
    winner = None
    draw = False
    
    # Helper util to monitor the game status.
    def draw_game_status(self):
        global draw

        if winner is None:
            status = XO.upper() + "'s Turn"
        else:
            status = winner.upper() + " wins!"
        if draw:
            status = 'Game drawn!'
        font = pg.font.Font(None, 30)
        text = font.render(status, 1, WHITE)
        renderBoard(self)
        
    # Helper util to check the win state of the game.
    def win_checker(self):
        global winner,draw

        # check for winning rows
        for row in range (0,3):
            if ((board[row][0] == board[row][1] == board[row][2]) and(board[row][0] is not None)):
                # this row won
                winner = board[row][0]
                drawRowLine(self, row)
                break
                
        # check for winning columns
        for col in range (0, 3):
            if (board[0][col] == board[1][col] == board[2][col]) and (board[0][col] is not None):
                # this column won
                winner = board[0][col]
                #draw winning line
                drawColumnLine(self, column)
                break
                
        # check for diagonal winners
        if (board[0][0] == board[1][1] == board[2][2]) and (board[0][0] is not None):
            # game won diagonally left to right
            winner = board[0][0]
            drawDiagonalLTR(self)
        if (board[0][2] == board[1][1] == board[2][0]) and (board[0][2] is not None):
            # game won diagonally right to left
            winner = board[0][2]
            drawDiagonalRTL(self)
        if(all([all(row) for row in board]) and winner is None ):
            draw = True
        draw_game_status(self)

    # Helper util to reset the game state.
    def reset_game(self):
        global winner, draw

        time.sleep(3)
        XO = 'x'
        draw = False
        __init__(self)
        winner = None
        board = [[None]*3,[None]*3,[None]*3]
