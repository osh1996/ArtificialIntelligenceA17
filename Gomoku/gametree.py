import numpy as np
from gamestate import GameState

class GameTree:

    def __init__(self, we_go_first):
        init_grid = np.full((15,15), "e")
        if we_go_first:
            init_grid[7][7] = "b"
        self.root = GameState(init_grid, -float('inf'), float('inf'))

