# cpuselect.py

This module should be responsible for spawning a dialogue window that asks the player whether they want to play a hotseat game (PvP) or agains the computer (PvCpu). 

## Dependencies 

Dialogues and buttons seem to be from a module called `pygame_gui`: 

- [pygame_gui](https://pygame-gui.readthedocs.io/en/latest/index.html)
- [Doc about listening to button clicks](https://pygame-gui.readthedocs.io/en/latest/events.html)

## RFC: Hypothetical Use 

For this to work, a few of the modules would have to be modified: 

1. main.py creates the `CpuSelect` object
2. `CpuSelect` object spawns a dialogue window that asks the player if they want to play a hotseat game or against the computer 
3. User clicks [Hotseat] or [Solo] button 
4. Click event is captured by `CpuSelect` and a flag of some sort is returned to main.py 
5. main.py then passes that flag to `Board.run()` 

```
     ┌───────┐                                        ┌────────────┐          ┌───────┐          ┌────────┐
     │main.py│                                        │cpuselect.py│          │game.py│          │board.py│
     └───┬───┘                                        └─────┬──────┘          └───┬───┘          └───┬────┘
         │               select = CpuSelect()               │                     │                  │     
         │──────────────────────────────────────────────────>                     │                  │     
         │                                                  │                     │                  │     
         │                CpuSelect instance                │                     │                  │     
         │<──────────────────────────────────────────────────                     │                  │     
         │                                                  │                     │                  │     
         │         is_hotseat = select.is_hotseat()         │                     │                  │     
         │──────────────────────────────────────────────────>                     │                  │     
         │                                                  │                     │                  │     
         │True if [Hotseat] clicked, False if [Solo] clicked│                     │                  │     
         │<──────────────────────────────────────────────────                     │                  │     
         │                                                  │                     │                  │     
         │                                                  │                     │                  │     
         │                             game = Game()        │                     │                  │     
         │───────────────────────────────────────────────────────────────────────>│                  │     
         │                                                  │                     │                  │     
         │                             Game instance        │                     │                  │     
         │<───────────────────────────────────────────────────────────────────────│                  │     
         │                                                  │                     │                  │     
         │                                                  │                     │                  │     
         │                                    board = Board(game)                 │                  │     
         │───────────────────────────────────────────────────────────────────────────────────────────>     
         │                                                  │                     │                  │     
         │                                      Board instance                    │                  │     
         │<───────────────────────────────────────────────────────────────────────────────────────────     
         │                                                  │                     │                  │     
         │                                   board.run(is_hotseat)                │                  │     
         │───────────────────────────────────────────────────────────────────────────────────────────>     
     ┌───┴───┐                                        ┌─────┴──────┐          ┌───┴───┐          ┌───┴────┐
     │main.py│                                        │cpuselect.py│          │game.py│          │board.py│
     └───────┘                                        └────────────┘          └───────┘          └────────┘
```

## Potential Modifications to the Existing Code 

If the above outlined scheme is used, then the existing code would have to be modified slightly.

### main.py 

main.py would be the one responsible for spawning the dialogue and passing the result to `Board.run()`:

```python
def main():
    select = CpuSelect()
    is_hotseat = select.is_hotseat()   # True if user clicks [Hotseat], 
                                       # False if user clicks [Solo]

    game = Game()
    board = Board(game) 
    board.run(is_hotseat)
```

### board.py 

Why was the `Cpu` move portion of the code thrown into `drawToken()` function? Whatever, it's too late now. 

This is why functions shouldn't do more than what it says on the tin. Now we have a giant `drawToken` function that does way more than simply drawing a token. 

**run()**:

```python 
def run(self, is_hotseat) -> None: 
    # snip
    elif event.type == MOUSEBUTTONDOWN:
        self.drawToken(is_hotseat) 
    # snip
```

**drawToken()**:

Change the `else` clause at line 135 to an `elif`. Let the `Cpu` take a turn only if the flag is false.

```python 
    # snip
    elif not is_hotseat:
        # computer player's turn.
        # takes place immediately after a user input event is handled
        cpu = Cpu(self._game)
        cpu.printBoard()
        cpu_move = cpu.find_best_move()
    # snip

```
