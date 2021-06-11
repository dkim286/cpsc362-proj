import pygame as pg, sys
from pygame.locals import *
from ttt.dimensions import BOARD_WIDTH as width, BOARD_HEIGHT as height, BOARD_LINE as line_color
from ttt.colors import WHITE
from ttt.game import Game

class Board:
    # initializer with instance attributes
    def __init__(self, game: Game):
        # initializing the pygame window
        pg.init()

        self._game = game

        # this method builds the infastructure of the display
        self.screen = pg.display.set_mode((width, height + 100), 0, 32)

        pg.display.set_caption("Tic Tac Toe")

        # loading the images as python object
        initiating_window = pg.image.load('img/ttt_opening.jpg')
        self.x_img = pg.image.load("img/x.png")
        self.o_img = pg.image.load("img/o.png")

        # resizing images
        initiating_window = pg.transform.scale(initiating_window, (width, height + 100))
        self.x_img = pg.transform.scale(self.x_img, (80, 80))
        self.o_img = pg.transform.scale(self.o_img, (80, 80))

        # displaying over the screen
        self.screen.blit(initiating_window, (0, 0))

        # updating the display
        pg.display.update()
        self.screen.fill(WHITE)

        # drawing vertical lines
        pg.draw.line(self.screen, line_color, (width / 3, 0), (width / 3, height), 7)
        pg.draw.line(self.screen, line_color, (width / 3 * 2, 0), (width / 3 * 2, height), 7)

        # drawing horizontal lines
        pg.draw.line(self.screen, line_color, (0, height / 3), (width, height / 3), 7)
        pg.draw.line(self.screen, line_color, (0, height / 3 * 2), (width, height / 3 * 2), 7)

    def run(self):
        while(True):
            for event in pg.event.get():
                if event.type == QUIT:
                    pg.quit()
                    sys.exit()
                elif event.type == MOUSEBUTTONDOWN:
                    self.drawToken()
                    if(winner or draw):
                        self._game.reset_game()
                    
            pg.display.update()
            CLOCK.tick(fps)

    def drawToken(self):

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

        if(row and col and board[row-1][col-1] is None):
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
            board[row - 1][col - 1] = self._game.XO

            if self._game.XO == 'X' or self._game.XO == 'x':
                self.screen.blit(self.x_img, (posy, posx))
                self._game.XO = 'O'
            else:
                self.screen.blit(self.o_img, (posy, posx))
                self._game.XO = 'X'
            
            pg.display.update()

            self._game.win_checker()

    def drawRowLine(self, row):
        pg.draw.line(self.screen, (250,0,0), (0, (row + 1) * height / 3 - height / 6),\
                            (width, (row + 1) * height / 3 - height / 6 ), 4)
    def drawColumnLine(self, column):
        pg.draw.line (self.screen, (250,0,0),((column + 1) * width / 3 - width / 6, 0),\
                     ((column + 1) * width / 3 - width / 6, height), 4)
    
    # Draw the winning line diagonally from right to left
    def drawDiagonalRTL(self):
        pg.draw.line (self.screen, (250,70,70), (350, 50), (50, 350), 4)

    # Draw the winning line diagonally from left to right
    def drawDiagonalLTR(self):
        pg.draw.line (self.screen, (250,70,70), (50, 50), (350, 350), 4)
    # Copy Rendered Message onto the board
    def renderBoard(self):
        self.screen.fill ((0, 0, 0), (0, 400, 500, 100))
        text_rect = text.get_rect(center=(width/2, 500-50))
        self.screen.blit(text, text_rect)
        pg.display.update()
