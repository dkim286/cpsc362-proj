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
  - `renderBoard`
    - This method takes the copied rendered message and posts it onto the board   

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
board.renderBoard()
```

# Design

## `Board` Class

This class is **purely for rendering the UI** based on the state of the `Game` instance contained within. It should contain no game logic besides calling on high-level `Game` functions to either read or modify the game state.

The `Board` class should have the these functions visible publicly (rename these or add more as more stuff gets prototyped):

- `Board.run() -> None`
  - Starts an infinite loop to keep the game going.

## Interaction With `game.py`

The `Board` object should contain a reference to the `Game` object, which represents the current state of the game:

```python
from ttt.game import Game

class Board():
    __init__(self, game: Game):
        self._game = game
        self._screen = pg.display.set_mode('...')

    # ...
    # snip
    # ...
```

The game instance reference is passed by the main function: 
```
     ┌───────┐                ┌───────┐          ┌────────┐
     │main.py│                │game.py│          │board.py│
     └───┬───┘                └───┬───┘          └───┬────┘
         │"construct Game object" │                  │     
         │───────────────────────>│                  │     
         │                        │                  │     
         │     Game instance      │                  │     
         │<───────────────────────│                  │     
         │                        │                  │     
         │        "construct Board instance"         │     
         │──────────────────────────────────────────>│     
         │                        │                  │     
         │        reference to Game instance         │     
         │──────────────────────────────────────────>│     
         │                        │                  │     
         │              Board instance               │     
         │<──────────────────────────────────────────│     
     ┌───┴───┐                ┌───┴───┐          ┌───┴────┐
     │main.py│                │game.py│          │board.py│
     └───────┘                └───────┘          └────────┘
```
## Class Diagram 

`Board` *contains* `Game`:

```
,---------------------------------------.
|Game                                   |
|---------------------------------------|
|-_ttt: list                            |
|+place_move(row: int, col: int) -> bool|
|+current_player() -> str               |
|+check_win_cond() -> str               |
`---------------------------------------'
                    |                    
                    |                    
       ,------------------------.        
       |Board                   |        
       |------------------------|        
       |-_game: Game            |        
       |-_screen: pygame.Surface|        
       |+run() -> None          |        
       `------------------------'   
```

## Running the Game

The `run()` function should have an infinite loop somewhere that runs the game continuously when called upon by `main.py`:

**main.py**:

```python
from ttt.game import Game
from ttt.board import Board

def main():
    game = Game()
    board = Board(game)
    
    board.run()

    # snip
```

**board.py**:

```python
import pygame as pg 

class Board:
    # snip

    def run(self):
        # the following is purely for example.
        # the actual implementation might differ.
        while(True):
            for event in pg.event.get():
                if event.type == QUIT:
                    pg.quit()
                    sys.exit()
                elif event.type == MOUSEBUTTONDOWN:
                    self._userClick()
                    if(winner or draw):
                        self._reset_game()
                    
            pg.display.update()
            CLOCK.tick(fps)

```

## Reading and Modifying the Game State 

The game's current state is kept track by the `Game` instance variable. 

For example, assuming that the current player needs to be determined by the board and that `Game` object has a `current_player() -> str` function visible publicly:

```
     ┌─────┐                             ┌─────┐
     │Board│                             │_game│
     └──┬──┘                             └──┬──┘
        │   self._game.current_player()     │   
        │──────────────────────────────────>│   
        │                                   │   
        │          ret 'x' or 'o'           │   
        │<──────────────────────────────────│   
        │                                   │   
        ────┐                               │   
            │ (do something with 'x' or 'o')│   
        <───┘                               │   
     ┌──┴──┐                             ┌──┴──┐
     │Board│                             │_game│
     └─────┘                             └─────┘
```

Another example:
- The board observes a user click event on row 2 and col 1 and needs to modify the game's state accordingly
- `Game` object has a `place_move(row: int, col: int) -> bool` visible publicly

```
     ┌─────┐                                  ┌─────┐
     │Board│                                  │_game│
     └──┬──┘                                  └──┬──┘
        │      self._game.place_move(2, 1)       │   
        │───────────────────────────────────────>│   
        │                                        │   
        │ret True if valid move, False otherwise │   
        │<───────────────────────────────────────│   
        │                                        │   
        ────┐                                    │   
            │ (do something with True or False)  │   
        <───┘                                    │   
     ┌──┴──┐                                  ┌──┴──┐
     │Board│                                  │_game│
     └─────┘                                  └─────┘
```

## Quitting Gracefully (or not)

The `run()` function can either handle exiting the program itself or let `main.py` decide:

```
     ┌───────┐          ┌───────┐          ┌────────┐
     │main.py│          │game.py│          │board.py│
     └───┬───┘          └───┬───┘          └───┬────┘
         │  game = Game()   │                  │     
         │─────────────────>│                  │     
         │                  │                  │     
         │ (Game instance)  │                  │     
         │<─────────────────│                  │     
         │                  │                  │     
         │        board = Board(game)          │     
         │────────────────────────────────────>│     
         │                  │                  │     
         │          (Board instance)           │     
         │<────────────────────────────────────│     
         │                  │                  │     
         ────┐              │                  │     
             │ board.run()  │                  │     
         <───┘              │                  │     
         │                  │                  │     
         ────┐              │                  │     
             │ sys.exit()   │                  │     
         <───┘              │                  │     
     ┌───┴───┐          ┌───┴───┐          ┌───┴────┐
     │main.py│          │game.py│          │board.py│
     └───────┘          └───────┘          └────────┘
```
