'''
Manages and manipulates the board, e.g. functions to actually change the state
of the Game object.
'''
import game.py
#going to need to import the width and height of the screen from game.py

class Board:

    # setting up a 3 * 3 board in canvas
    
    # initializer with instance attributes
    def __init__(self):

    # this function checks if a token can be placed
    def checkBoardForSpace(self, x, y, token):
        

    def drawToken(self, row, col, token):

    # this function will check if the board is full and a tie
    def isFull(self):

    # check if there is a winner by calling the check functions, this will return either the winner or ' '
    def checkWin(self):
        