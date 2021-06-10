# game.py

This module represents the state of the game. It handles all game logic and **should not** be involved in touching the UI in any way. The UI might as well not exist as far as this module is concerned. 

# Design

## `Game` Class

### Public

The `Game` class should have functions similar to these visible publicly (rename these, make changes, or add more as the module changes):

- `Game.place_move(row: int, col: int) -> bool`
  - Attempt to place a move in [`row`, `col`], where each value ranges from 1 to 3 inclusive. 
  - Return `True` if valid. Return `False` otherwise. 
- `Game.current_player() -> str`
  - Return `'x'` if it's X's turn. Return `'o'` if it's O's turn. 
- `Game.check_win_condition() -> str`
  - Determine the win condition. 
  - Return `'x'` or `'o'` if X or O won, respectively. Return `'draw'` if it's a draw.

### Private 

The state of the game is tracked via a nested list representing the 3x3 grid:

```python 
class Game:
    __init__(self):
        self._ttt = [[None] * 3,
                     [None] * 3, 
                     [None] * 3]
        # snip
```

The `Game` class should have some utility functions at the implementer's discretion. Some example might include:

- `Game._get_value(row: int, col: int) -> str`
  - Get the value currently in [`row`, `col`].
  - Params:
    - `row`: Row number in logical form (1 to 3 inclusive)
    - `col`: Column number in logical form (1 to 3 inclusive) 
  - Return whatever's in `self._ttt[row, col]`. Return `None` if empty.

## Interacting with `board.py`

This module **does not** touch the UI in any way. The `Game` class is expected to be an instance variable of `Board` and keeps track of the game state. 

For details, see [board.md](board.md).




