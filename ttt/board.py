import pygame as pg, sys
from pygame.locals import *
from ttt.dimensions import *
from ttt.colors import *
from ttt.game import Game

IMG_DIR = 'img/'

X_IMG_PATH = IMG_DIR + 'x.png'
O_IMG_PATH = IMG_DIR + 'o.png'
OPENING_IMG_PATH = IMG_DIR + 'ttt_opening.jpg'

GAME_NAME = 'Tic Tac Toe'

class Board:
    # initializer with instance attributes
    def __init__(self, game: Game):
        # initializing the pygame window
        pg.init()
        self.fps = 30
        self.CLOCK = pg.time.Clock()
        self._game = game

        # initialize the UI window
        flags = 0
        color_depth = 32
        self._screen = pg.display.set_mode(UI_SIZE, flags, color_depth)

        pg.display.set_caption(GAME_NAME)

        # loading the images as python object
        splash_screen = pg.image.load(OPENING_IMG_PATH)
        self.x_img = pg.image.load(X_IMG_PATH)
        self.o_img = pg.image.load(O_IMG_PATH)

        # resizing images
        splash_screen = pg.transform.scale(splash_screen, UI_SIZE)
        self.x_img = pg.transform.scale(self.x_img, GRID_SIZE)
        self.o_img = pg.transform.scale(self.o_img, GRID_SIZE)

        # display splash screen
        origin = (0, 0)
        self._screen.blit(splash_screen, origin)

        # updating the display
        pg.display.update()
        self._screen.fill(WHITE)

        # drawing vertical lines
        thickness = 7
        pg.draw.line(self._screen, RED, T12, (T32[0], T32[1] + GRID_HEIGHT), thickness)
        pg.draw.line(self._screen, RED, T13, (T33[0], T33[1] + GRID_HEIGHT), thickness)

        # drawing horizontal lines
        pg.draw.line(self._screen, RED, T21, (T23[0] + GRID_WIDTH, T23[1]), thickness)
        pg.draw.line(self._screen, RED, T31, (T33[0] + GRID_WIDTH, T33[1]), thickness)

        pg.display.update()

    def run(self):
        while(True):
            for event in pg.event.get():
                if event.type == QUIT:
                    pg.quit()
                    sys.exit()
                elif event.type == MOUSEBUTTONDOWN:
                    self.drawToken()
                    winner = self._game.win_checker()
                    if(winner != 'N'):
                        self._game.reset_game()
                    
            pg.display.update()
            self.CLOCK.tick(self.fps)

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

        if(row and col and self._game.board[row-1][col-1] is None):
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
            previous_token = self.self._game._XO

            good_move = self._game.place_move(row, col)

            if (good_move and previous_token == 'x'):
                self._screen.blit(self.x_img, (posy, posx))

            elif (good_move and previous_token == 'o'):
                self._screen.blit(self.o_img, (posy, posx))
            
            pg.display.update()

            self._game.win_checker()

    def drawRowLine(self, row):
        pg.draw.line(self._screen, (250,0,0), (0, (row + 1) * height / 3 - height / 6),\
                            (width, (row + 1) * height / 3 - height / 6 ), 4)
    def drawColumnLine(self, column):
        pg.draw.line (self._screen, (250,0,0),((column + 1) * width / 3 - width / 6, 0),\
                     ((column + 1) * width / 3 - width / 6, height), 4)
    
    # Draw the winning line diagonally from right to left
    def drawDiagonalRTL(self):
        pg.draw.line (self._screen, (250,70,70), (350, 50), (50, 350), 4)

    # Draw the winning line diagonally from left to right
    def drawDiagonalLTR(self):
        pg.draw.line (self._screen, (250,70,70), (50, 50), (350, 350), 4)
        
    # Copy Rendered Message onto the board
    def renderBoard(self):
        self._screen.fill ((0, 0, 0), (0, 400, 500, 100))
        text_rect = text.get_rect(center=(width/2, 500-50))
        self._screen.blit(text, text_rect)
        pg.display.update()
