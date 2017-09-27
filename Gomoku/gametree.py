import numpy as np
from gamestate import GameState

class GameTree:

    def __init__(self, we_go_first, x, y):
        init_grid = np.full((15,15), "e")
        if we_go_first:
            init_grid[x][y] = "b"
        else:
            init_grid[x][y] = "w"
        self.root = GameState(init_grid, x, y)

    def getNewRoot(self, opponentsMove):
        x = opponentsMove[2]
        y = opponentsMove[1]
        successors = self.root.successors
        for state in successors:
            if state.coordinate[0] is x and state.coordinate[1] is y:
                self.root = state