# board.py

This module represents the board and screen of Tic Tac Toe.

# Board

## Appearance

```
+-----+-----+-----+
| T11 | T12 | T13 |
| --- | --- | --- |
| T21 | T22 | T23 |
| --- | --- | --- |
| T31 | T32 | T33 |
+-----+-----+-----+

```

## Assumptions 

- Each player will click one of the 9 availalble squares.

## Board Methods
  - `drawToken`
    - This method draws a token to the board of the screen.
  - `drawRowLine`
    - This method draws the winning line across the row passed in.
  - `drawColumnLine`
    - This method draws the winning line down the column passed in.
  - `drawDiagonalRTL`
    - This method draws the winning line diagonally from right to left.
  - `drawDiagonalLTR`
    - This method draws the winning line diagonally from left to right.

## Potential Use Examples 

```python
from ttt.board.py import *         # Board 

Board board

board.drawToken('X')
board.drawToken('O')
board.drawRowLine(1)
board.drawColumnLine(1)
board.drawDiagonalRTL()
board.drawDiagonalLTR()
