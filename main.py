'''
Main driver for the game. 

Instantiates the Game object, handles user interactions, and draws the GUI.
'''

import pygame as pg

from ttt.game import Game
from ttt.colors import *
from ttt.board import *
from ttt.cpuselect import *


def main():
    select = CpuSelect()
    is_hotseat = select.is_hotseat()
    game = Game()
    board = Board(game)
    board.run(is_hotseat)

if __name__ == '__main__':
    main()
