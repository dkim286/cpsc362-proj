from typing import TypedDict
import time

import pygame as pg, sys
from pygame.locals import *

from ttt.dimensions import *
from ttt.colors import *
from ttt.game import Game, X, O, DRAW, UNDECIDED

IMG_DIR = 'img/'

X_IMG_PATH = IMG_DIR + 'x.png'
O_IMG_PATH = IMG_DIR + 'o.png'
OPENING_IMG_PATH = IMG_DIR + 'ttt_opening.jpg'

GAME_NAME = 'Tic Tac Toe'
WIN_MSG = "Player {} has won!"
DRAW_MSG = "It's a draw."


class Board:
    def __init__(self, game: Game):
        '''
        Constructor for the Board object.
        Parameters:
            game (Game): A reference to the Game object.
        '''
        # initializing the pygame window
        pg.init()

        # instance variables
        self._fps = 30
        self.CLOCK = pg.time.Clock()
        self._game = game

        # initialize the UI window
        flags = 0
        color_depth = 32
        self._screen = pg.display.set_mode(UI_SIZE, flags, color_depth)

        pg.display.set_caption(GAME_NAME)

        # loading the images as python object
        splash_screen = pg.image.load(OPENING_IMG_PATH)
        self._x_img = pg.image.load(X_IMG_PATH)
        self._o_img = pg.image.load(O_IMG_PATH)

        # resizing images
        splash_screen = pg.transform.scale(splash_screen, UI_SIZE)
        self._x_img = pg.transform.scale(self._x_img, GRID_SIZE)
        self._o_img = pg.transform.scale(self._o_img, GRID_SIZE)

        # display splash screen
        origin = (0, 0)
        self._screen.blit(splash_screen, origin)

        # updating the display
        pg.display.update()

        self._draw_ui()


    def run(self) -> None:
        '''
        Runs the game in an infinite loop, accepting user input all the while.
        '''
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
            self.CLOCK.tick(self._fps)


    def drawToken(self) -> None:
        '''
        Read the current game state and draw a token where appropriate.
        '''
        # get coordinates of mouse click
        x, y = pg.mouse.get_pos()

        # get column of mouse click
        if x < BOARD_WIDTH / 3:
            col = 1
        elif x < BOARD_WIDTH / 3 * 2:
            col = 2
        elif x < BOARD_WIDTH:
            col = 3
        else:
            col = None
    
        # get row of mouse click
        if y < BOARD_HEIGHT / 3:
            row = 1
        elif y < BOARD_HEIGHT / 3 * 2:
            row = 2
        elif y < BOARD_HEIGHT:
            row = 3 
        else:
            row = None

        '''
        if row and col and self._game.board[row-1][col-1] is None:
            # Find the x cordinate for the rows for the token to be placed
            if row == 1:
                posx = 30
            elif row == 2:
                posx = BOARD_WIDTH / 3 + 30
            else:
                posx = BOARD_WIDTH / 3 * 2 + 30

            # Find the y cordinate for the rows for the token to be placed
            if col == 1:
                posy = 30
            elif col == 2:
                posy = BOARD_HEIGHT / 3 + 30
            else:
                posy = BOARD_HEIGHT / 3 * 2 + 30
        '''

        location = GRID_OFFSETS[row - 1][col - 1]

        # Place the token
        previous_token = self._game.player

        good_move = self._game.place_move(row, col)

        if (good_move and previous_token == X):
            self._screen.blit(self._x_img, location)

        elif (good_move and previous_token == O):
            self._screen.blit(self._o_img, location)

        pg.display.update()

        # Check if anyone has won. If so, consider the game to be over.
        winner = self._game.win_checker()
        game_over = False

        if winner == DRAW:
            self.render_message(DRAW_MSG)
            game_over = True
        elif winner == UNDECIDED:
            pass
        else:
            self.render_message(WIN_MSG.format(winner))
            game_over = True

        # If the game is over, reset and redraw the game.
        if game_over:
            self._game.reset_game()
            self._draw_ui()



    def drawRowLine(self, row: int) -> None:
        '''
        Draw the winning line across the specified row.

        Paramters:
            row (int): The row number (1 to 3 inclusive).
        '''
        x_end = BOARD_X + BOARD_WIDTH
        y_offset = BOARD_Y + ((row - 1) * GRID_HEIGHT) + (GRID_HEIGHT // 2)

        start = (BOARD_X, y_offset)
        end = (x_end, y_offset)
        thickness = 4

        pg.draw.line(self._screen, RED, start, end, thickness)
        pg.display.update()


    def drawColumnLine(self, column: int) -> None:
        '''
        Draw the winning line down the specified column.

        Parameters:
            column (int): The column number (1 to 3 inclusive).
        '''
        x_offset = BOARD_X + ((column - 1) * GRID_WIDTH) + (GRID_WIDTH // 2)
        y_end = BOARD_Y + BOARD_HEIGHT

        start = (x_offset, BOARD_Y)
        end = (x_offset, y_end)
        thickness = 4

        pg.draw.line(self._screen, RED, start, end, thickness)
        pg.display.update()


    def drawDiagonalRTL(self) -> None:
        '''
        Draw the winning line diagonally from right to left.
        '''
        start = (BOARD_X + BOARD_WIDTH, BOARD_Y)
        end = (BOARD_X, BOARD_Y + BOARD_HEIGHT)
        thickness = 4

        pg.draw.line (self._screen, RED, start, end, thickness)
        pg.display.update()


    def drawDiagonalLTR(self) -> None:
        '''
        Draw the winning line diagonally from left to right.
        '''
        start = (BOARD_X, BOARD_Y)
        end = (BOARD_X + BOARD_WIDTH, BOARD_Y + BOARD_HEIGHT)
        thickness = 4

        pg.draw.line (self._screen, RED, start, end, thickness)


    def render_message(self, message: str) -> None:
        '''
        Render the status message in the status area.

        Parameters:
            message (str): The message to render.
        '''
        self._render_status_area()

        font_size = 30
        font = pg.font.Font(None, font_size)

        antialias = 1
        text = font.render(message, antialias, WHITE)

        x_center = (STATUS_X + STATUS_WIDTH) // 2
        y_center = STATUS_Y + STATUS_HEIGHT // 2
        center = (x_center, y_center)
        text_rect = text.get_rect(center=center)
        self._screen.blit(text, text_rect)

        pg.display.update()
        time.sleep(3)


    def _render_status_area(self) -> None:
        '''
        Render the status area at the bottom of the board
        '''
        status_rectangle = (STATUS_X, STATUS_Y, STATUS_WIDTH, STATUS_HEIGHT)
        self._screen.fill(BLACK, status_rectangle)
        pg.display.update()


    def _draw_ui(self) -> None:
        self._screen.fill(WHITE)

        # drawing vertical lines
        thickness = 7
        pg.draw.line(self._screen, RED, T12, (T32[0], T32[1] + GRID_HEIGHT), thickness)
        pg.draw.line(self._screen, RED, T13, (T33[0], T33[1] + GRID_HEIGHT), thickness)

        # drawing horizontal lines
        pg.draw.line(self._screen, RED, T21, (T23[0] + GRID_WIDTH, T23[1]), thickness)
        pg.draw.line(self._screen, RED, T31, (T33[0] + GRID_WIDTH, T33[1]), thickness)

        self._render_status_area()

        pg.display.update()
