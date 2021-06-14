# cpu.py 

This module is responsible for handling the computer player logic. 

# Algorithm 

Brandon has done this before. We should defer to him when making implementation decisions. 

- [http://article.sapub.org/10.5923.j.jgt.20200901.01.html](http://article.sapub.org/10.5923.j.jgt.20200901.01.html)
- [https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-3-tic-tac-toe-ai-finding-optimal-move/](https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-3-tic-tac-toe-ai-finding-optimal-move/)

This document contains:

- [Naiive Search code](#potential-code-for-naiive-search)
  - [Implementing it as a module](#implementing-it-as-a-module)
    - [Option 1](#option-1-instance-variable)
      - [Sequence diagram](#option-1-sequence-diagram)
    - [Option 2](#option-2-construct-it-as-needed) <<<<< We're going with this option 
      - [Sequence diagram](#option-2-sequence-diagram)
- [Matrix-based](#matrix-based)

# Potential Code for Naiive Search

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

## Implementing it as a module 

Most likely, this will have to be handled as an object.

### Option 1: Instance Variable (WE'RE NOT DOING THIS)

**NOTE**: We're going with option 2. Click [here](#option-2-construct-it-as-needed) to jump to option 2. 

We can make `Cpu` an instance variable of the `Board` object. I can't think of a good reason why it'd be implemented like this, unless the `Cpu` object has some persistent variables that needs to be kept alive while the game is progressing. 

**cpu.py**

```python
from typing import TypedDict 
import copy
from ttt.game import Game

class _score(TypedDict):
    x: int 
    o: int
    complete: bool
    
    
_move = tuple[int, int]

class Cpu:
    def __init__(self, game: Game):
        # make a copy of the ongoing game.
        self._game = copy.deepcopy(game)
    
    
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
    def __init__(self, game: Game, '...'):
        self._cpu = Cpu(game)
        # snip
        # ...
```

#### Option 1 Sequence Diagram 

```
     ┌─────┐                                 ┌───┐          ┌────┐
     │Board│                                 │Cpu│          │Game│
     └──┬──┘                                 └─┬─┘          └─┬──┘
        ────┐                                  │              │   
            │ is the self._cpu object not None?│              │   
        <───┘                                  │              │   
        │                                      │              │   
        │     self._cpu.find_best_move()       │              │   
        │─────────────────────────────────────>│              │   
        │                                      │              │   
        │      best move is: (row, col)        │              │   
        │<─────────────────────────────────────│              │   
        │                                      │              │   
        │          self._game.place_move(row, col)            │   
        │────────────────────────────────────────────────────>│   
     ┌──┴──┐                                 ┌─┴─┐          ┌─┴──┐
     │Board│                                 │Cpu│          │Game│
     └─────┘                                 └───┘          └────┘
```

### Option 2: Construct it as needed

This is likely the better choice. The downside is that the `Cpu` object lives only temporarily.

Assuming that the `Cpu` object is implemented similarly to the previous example, the `Board.run()`function could be modified slightly to allow for computer player's move inbetween human player actions.

**board.py**:

```python
from ttt.cpu import Cpu

class Board: 
    # snip
    # ...
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
                    
                # computer player's turn.
                # takes place immediately after a user input event is handled
                cpu = Cpu(self._game)
                cpu_move = cpu.find_best_move()
                self._game.place_move(cpu_move[0], cpu_move[1])
                
            pg.display.update()
            self.CLOCK.tick(self._fps)

```


#### Option 2 Sequence Diagram 

```
     ┌──────┐               ┌───────────┐                        ┌──────┐          ┌───────┐
     │PyGame│               │Board.run()│                        │cpu.py│          │game.py│
     └──┬───┘               └─────┬─────┘                        └──┬───┘          └───┬───┘
        │      pg.event.get()     │                                 │                  │    
        │ <────────────────────────                                 │                  │    
        │                         │                                 │                  │    
        │ (a list of input events)│                                 │                  │    
        │ ────────────────────────>                                 │                  │    
        │                         │                                 │                  │    
        │                         │      human player: Game.place_move(row, col)       │    
        │                         │ ──────────────────────────────────────────────────>│    
        │                         │                                 │                  │    
        │                         │         ret True if valid, False otherwise         │    
        │                         │ <──────────────────────────────────────────────────│    
        │                         │                                 │                  │    
        │                         │           cpu = Cpu()           │                  │    
        │                         │ ────────────────────────────────>                  │    
        │                         │                                 │                  │    
        │                         │          (Cpu instance)         │                  │    
        │                         │ <────────────────────────────────                  │    
        │                         │                                 │                  │    
        │                         │       cpu.find_best_move()      │                  │    
        │                         │ ────────────────────────────────>                  │    
        │                         │                                 │                  │    
        │                         │ (best move in (row, col) format)│                  │    
        │                         │ <────────────────────────────────                  │    
        │                         │                                 │                  │    
        │                         │     computer player: Game.place_move(row, col)     │    
        │                         │ ──────────────────────────────────────────────────>│    
        │                         │                                 │                  │    
        │                         │         ret True if valid, False otherwise         │    
        │                         │ <──────────────────────────────────────────────────│    
     ┌──┴───┐               ┌─────┴─────┐                        ┌──┴───┐          ┌───┴───┐
     │PyGame│               │Board.run()│                        │cpu.py│          │game.py│
     └──────┘               └───────────┘                        └──────┘          └───────┘
```


# Matrix-based 

The first article (- [http://article.sapub.org/10.5923.j.jgt.20200901.01.html](http://article.sapub.org/10.5923.j.jgt.20200901.01.html)
) talks about using a stochastic matrix. If you can think of a way to make that work, *please* document it here. 
