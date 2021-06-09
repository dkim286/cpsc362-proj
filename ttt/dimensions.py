'''
Provides any coordinate tuples or rectangle definitions to be used by the game.

All definitions are compatible with PyGame's coordinate and rectangle tuples:
- coordinates: (x, y)
- rectangles: (x_offset, y_offset, width, height)

+-----+-----+-----+
| T11 | T12 | T13 |
| --- | --- | --- |
| T21 | T22 | T23 |
| --- | --- | --- |
| T31 | T32 | T33 |
+-----+-----+-----+
'''

################################################################################
# BOARD
################################################################################

########################################
# Size
########################################

# Playable area dimension (board).
BOARD_WIDTH = 400
BOARD_HEIGHT = 400
BOARD_LINE = (10, 10, 10)

#TicTacToe 3x3 board
TTT = [[None]*3,[None]*3,[None]*3]

# Playable area's dimension as a size tuple.
BOARD_SIZE = (BOARD_WIDTH, BOARD_HEIGHT)

# Dimension of each grid square.
GRID_WIDTH = BOARD_WIDTH / 3
GRID_HEIGHT = BOARD_HEIGHT / 3

# Each grid square's dimension as a size tuple.
GRID_SIZE = (GRID_WIDTH, GRID_HEIGHT)

########################################
# Offset
########################################

# Playable area's X and Y coordinates (top left).
BOARD_X = 0
BOARD_Y = 0

# Playable area's xy as a tuple.
BOARD_OFFSET = (BOARD_X, BOARD_Y)

# Grid coordinates.
# Each coordinate represents the top left corner of each grid square.
T11 = (0,0)
T12 = (BOARD_WIDTH / 3, 0)
T13 = (BOARD_WIDTH / 3 * 2, 0)

T21 = (0, BOARD_WIDTH / 3)
T22 = (BOARD_WIDTH / 3, BOARD_WIDTH / 3)
T23 = (BOARD_WIDTH / 3 * 2, BOARD_WIDTH / 3)

T31 = (0, BOARD_WIDTH / 3 * 2)
T32 = (BOARD_WIDTH / 3, BOARD_WIDTH / 3 * 2) 
T33 = (BOARD_WIDTH / 3 * 2, BOARD_WIDTH / 3 * 2)



################################################################################
# UI
################################################################################

########################################
# Size
########################################

# Status area's dimension.
STATUS_WIDTH = BOARD_WIDTH
STATUS_HEIGHT = 100

# Status area's dimension as a size tuple.
STATUS_SIZE = (STATUS_WIDTH, STATUS_HEIGHT)

# Entire UI's dimension.
UI_WIDTH = BOARD_WIDTH
UI_HEIGHT = BOARD_HEIGHT + STATUS_HEIGHT

# Entire UI's dimension as a size tuple.
UI_SIZE = (UI_WIDTH, UI_HEIGHT)

########################################
# Offset
########################################

# Status area's X and Y coordinates (top left).
STATUS_X = 0
STATUS_Y = BOARD_HEIGHT

# Status area's X and Y coordinates as an offset tuple.
STATUS_OFFSET = (STATUS_X, STATUS_Y)







