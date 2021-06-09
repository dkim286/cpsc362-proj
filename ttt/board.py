import pygame as pg
from ttt.dimensions import BOARD_WIDTH as width, BOARD_HEIGHT as height, BOARD_LINE as line_color, TTT as board

class Board:
    # setting up a 3 * 3 board in canvas
    board = [[None] * 3, [None] * 3, [None] * 3]
    
    # initializer with instance attributes
    def __init__(self):
        # initializing the pygame window
        pg.init()

        # this method builds the infastructure of the display
        screen = pg.display.set_mode((width, height + 100), 0, 32)

        pg.display.set_caption("Tic Tac Toe")

        # loading the images as python object
        initiating_window = pg.image.load('img/ttt_opening.jpg')
        x_img = pg.image.load("img/x.png")
        y_img = pg.image.load("img/y.png")

        # resizing images
        initiating_window = pg.transform.scale(initiating_window, (width, height + 100))
        x_img = pg.transform.scale(x_img, (80, 80))
        y_img = pg.transform.scale(y_img, (80, 80))

        # displaying over the screen
        screen.blit(initiating_window, (0, 0))

        # updating the display
        pg.display.update()
        screen.fill(255, 255, 255)

        # drawing vertical lines
        pg.draw.line(screen, line_color, (width / 3, 0), (width / 3, height), 7)
        pg.draw.line(screen, line_color, (width / 3 * 2, 0), (width / 3 * 2, height), 7)

        # drawing horizontal lines
        pg.draw.line(screen, line_color, (0, height / 3), (width, height / 3), 7)
        pg.draw.line(screen, line_color, (0, height / 3 * 2), (width, height / 3 * 2), 7)

    def drawToken(self, token):

        # get coordinates of mouse click
        x, y = pg.mouse.get_pos()

        # get column of mouse click
        if( x < width / 3):
            col = 1
        elif (x < width / 3 * 2):
            col = 2
        elif(x < width):
            col = 3
        else:
            col = None
    
        # get row of mouse click
        if(y < height / 3):
            row = 1
        elif (y < height / 3 * 2):
            row = 2
        elif(y<height):
            row = 3 
        else:
            row = None

        if(row and col):
            # Find the x cordinate for the rows for the token to be placed
            if row == 1:
                posx = 30
            elif row == 2:
                posx = width / 3 + 30
            else:
                posx = width / 3 * 2 + 30

            # Find the y cordinate for the rows for the token to be placed
            if col == 1:
                posy = 30
            elif col == 2:
                posy = height / 3 + 30
            else:
                posy = height / 3 * 2 + 30

            # Place the token
            board[row - 1][col - 1] = token

            if token == 'X' or token == 'x':
                screen.blit(x_img, (posy, posx))
            else:
                screen.blit(y_img, (posy, posx))
            
            pg.display.update()

    def drawRowLine(self, row):
        pg.draw.line(screen, (250,0,0), (0, (row + 1) * height / 3 - height / 6),\
                            (width, (row + 1) * height / 3 - height / 6 ), 4)
    def drawColumnLine(self, column):
        pg.draw.line (screen, (250,0,0),((col + 1) * width / 3 - width / 6, 0),\
                     ((col + 1) * width / 3 - width / 6, height), 4)
    
    # Draw the winning line diagonally from right to left
    def drawDiagonalRTL(self):
        pg.draw.line (screen, (250,70,70), (350, 50), (50, 350), 4)

    # Draw the winning line diagonally from left to right
    def drawDiagonalLTR(self):
        pg.draw.line (screen, (250,70,70), (50, 50), (350, 350), 4)

        