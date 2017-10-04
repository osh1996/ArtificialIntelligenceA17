import parsing

class GameState:

    def __init__(self, grid, x, y):
        self.grid = grid
        self.utility = 0
        self.evaluation = 0
        self.coordinate = (x,y)
        self.successors = list()
