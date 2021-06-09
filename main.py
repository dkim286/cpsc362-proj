'''
Main driver for the game. 

Instantiates the Game object, handles user interactions, and draws the GUI.
'''

import pygame as pg

from ttt.game import Game
from ttt.colors import *
from ttt.board import Board
#from ttt.board import * //Depending on what gets imported into board.py
#from ttt.cpu import *


def main():
    game = Game()
    print('I made a Game object.')
    print ('Red is: {}'.format(color_to_str(RED)))

    # call checkBoardForSpace
    # call drawToken
    # call isFull
    # call checkWin
    # call functions from game.py below
if __name__ == '__main__':
    main()
