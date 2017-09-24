import numpy as np
from gamestate import GameState

class GameTree:

    def __init__(self):
        init_grid = np.full((15,15), "e")
        self.root = GameState(init_grid, -float('inf'), float('inf'), "t")

