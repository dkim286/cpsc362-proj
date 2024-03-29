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

# Playable area's dimension as a size tuple.
BOARD_SIZE = (BOARD_WIDTH, BOARD_HEIGHT)

# Dimension of each grid square.
GRID_WIDTH = BOARD_WIDTH // 3
GRID_HEIGHT = BOARD_HEIGHT // 3

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

# Grid offsets.
# Each coordinate represents the top left corner of each grid square.
T11 = (0,0)
T12 = (BOARD_WIDTH // 3, 0)
T13 = (BOARD_WIDTH // 3 * 2, 0)

T21 = (0, BOARD_WIDTH / 3)
T22 = (BOARD_WIDTH // 3, BOARD_WIDTH // 3)
T23 = (BOARD_WIDTH // 3 * 2, BOARD_WIDTH // 3)

T31 = (0, BOARD_WIDTH // 3 * 2)
T32 = (BOARD_WIDTH // 3, BOARD_WIDTH // 3 * 2)
T33 = (BOARD_WIDTH // 3 * 2, BOARD_WIDTH // 3 * 2)

# Grid offsets as a single nested list.
GRID_OFFSETS = [[T11, T12, T13],
                [T21, T22, T23],
                [T31, T32, T33]]


# For Winning Lines

# Vertical lines - Winning Column

# Start
WC11 = (0 + BOARD_WIDTH // (3 * 2), 0)
WC12 = ((BOARD_WIDTH // 3) + BOARD_WIDTH // (3 * 2), 0)
WC13 = (BOARD_WIDTH // 3 * 2 +  BOARD_WIDTH // (3 * 2) , 0)
# End
WC31 = (0 + (BOARD_WIDTH // (3 * 2)), BOARD_HEIGHT)
WC32 = (BOARD_WIDTH // 3 + (BOARD_WIDTH // (3 * 2)), BOARD_HEIGHT)
WC33 = (BOARD_WIDTH // 3 * 2 + (BOARD_WIDTH // (3 * 2)), BOARD_HEIGHT)

# Horizontal lines - Winning Row

# Start
WR11 = (0, BOARD_HEIGHT // (3 * 2))
WR12 = (0, BOARD_HEIGHT // 3 + (BOARD_HEIGHT // (3 * 2)))
WR13 = (0, BOARD_HEIGHT // 3 * 2 + (BOARD_HEIGHT // (3 * 2)))
# End
WR31 = (BOARD_WIDTH, BOARD_HEIGHT // (3 * 2))
WR32 = (BOARD_WIDTH, BOARD_HEIGHT // 3 + (BOARD_HEIGHT // (3 * 2)))
WR33 = (BOARD_WIDTH, BOARD_HEIGHT // 3 * 2 + (BOARD_HEIGHT // (3 * 2)))

# Diagonal lines 

# Start
#RTL
WD11 = (0, 0)
#LTR
WD13 = (BOARD_WIDTH, 0)
# End
#RTL
WD31 = (BOARD_WIDTH, BOARD_HEIGHT)
#LTR
WD33 = (0, BOARD_HEIGHT)


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







