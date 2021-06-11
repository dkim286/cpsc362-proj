# cpu.py 

This module is responsible for handling the computer player logic. 

# Algorithm 

I'm not going to hold your hand through this. There are plenty of resources online on how to create an algorithm that plays tic tac toe. 

- [http://article.sapub.org/10.5923.j.jgt.20200901.01.html](http://article.sapub.org/10.5923.j.jgt.20200901.01.html)
- [https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-3-tic-tac-toe-ai-finding-optimal-move/](https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-3-tic-tac-toe-ai-finding-optimal-move/)

## Potential Code for Naiive Search

The best possible move for the computer player could be determined by naiively (is it really naiive?) running a simulated game, running it through to completion, and then use the move that has the best winning potential. 

Here's a half-baked Python code for searching naiively. It may not be correct, so use your judgment: 

```python
from typing import TypedDict
from ttt.game import Game, X, O, DRAW, UNDECIDED


class _score(TypedDict):
    x: int
    o: int
    complete: bool


def evaluate_game(game: Game) -> _score:
    '''
    Evaluate the current finished game and see if anybody's won.
    
    Parameters: 
        game (Game): The game to evaluate.
    
    Returns:
        score (_score): The score that results from this finished game.
    '''
    score: _score = {'x': 0, 'o': 0, 'complete': False}
    game_outcome = game.win_checker()
    
    if game_outcome == X:
        score['x'] = 1
    elif game_outcome == O:
        score['o'] = 1
    
    if game_outcome != UNDECIDED:
        score['complete'] = True
    
    return score
    

def min_max(game: Game, depth: int, player: str) -> _score:
    '''
    Simulate all possible moves of the board and return the score once the 
    simulation is finished.
    
    Parameters: 
        game (Game): The game to evaluate.
        depth (int): Current depth of the recursive call.
        player (str): Whether the current player that wants to win is X 
                      or O.
    
    Returns:
        score (_score): The score resulting from the simulated move.
    '''
    score = evaluate_game(game)
    
    if score['complete']:
        return score
    
    current_best = -1 

    # make all possible moves 
    for row in range(3):
        for col in range(3):
            if game.place_move(row, col) == False:
                continue
            if player == X:
                next_move = min_max(game, depth + 1, O)
            else:
                next_move = min_max(game, depth + 1, X)
            current_best = max(current_best, next_move)
            
            # this function probably needs to be implemented: 
            game.undo() 
    
    return current_best


_move = tuple[int, int]
def find_best_move(game: Game, player: str) -> _move:
    '''
    Find the best possible move for the current game by starting the recursive
    call chain on min_max().
    
    Parameters:
        game (Game): The current game to evaluate.
        player (str): The player that wants to find the best move.
    
    Returns:
        move (_move): A row-column tuple representing the best move.
    '''
    current_best = -1
    best_move: _move = (-1, -1)
    
    for row in range(3):
        for col in range(3):
            if game.place_move(row, col) == False:
                continue 
            if player == X:
                simulated_value = min_max(game, 0, O)
            else:
                simulated_value = min_max(game, 0, X)
            
            # this functions probably needs to be implemented 
            game.undo()
            
            # we have a new contender for the best possible move
            if simulated_value > current_best:
                best_move: _move = (row, col)
                current_best = simulated_value
    
    return best_move 
    
    
# snip

game = Game()
player = X

while True:
    best_move = find_best_move(game, player)
    game.place_move(best_move[0], best_move[1])
    
    if player == X:
        player = O
    else:
        player = X

```

# Implementing it as a module 

Most likely, this will have to be handled as an object.

**cpu.py**

```python
from typing import TypedDict 
from ttt.game import Game

class _score(TypedDict):
    x: int 
    o: int
    complete: bool
    
    
_move = tuple[int, int]

class Cpu:
    def __init__(self, game: Game):
        self._game = game 
    
    
    def find_best_move(self) -> _move: 
        # snip
        # ...
        current_best = self._min_max()
        # snip
        # ...
        return best_move
    
    def _min_max(self, depth) -> _score:
        score: _score = self._evaluate_game()
        # snip 
        # ...

    def _evaluate_game(self) -> _score: 
        # snip
        # ...
        
```

**board.py**

```python
from ttt.cpu import Cpu

# snip
# ...

class Board: 
    def __init__(self, cpu: Cpu, '...'):
        self._cpu = cpu
        # snip
        # ...
```
