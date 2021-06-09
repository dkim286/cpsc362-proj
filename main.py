'''
Main driver for the game. 

Instantiates the Game object, handles user interactions, and draws the GUI.
'''

import pygame as pg

from ttt.game import Game
from ttt.colors import *
from ttt.board import Board

def main():
    game = Game()
    print('I made a Game object.')
    print ('Red is: {}'.format(color_to_str(RED)))

if __name__ == '__main__':
    main()
