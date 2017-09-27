class GameState:

    def __init__(self, grid, x, y):
        self.grid = grid
        self.eval = 0
        self.coordinate = (x,y)
        self.successors = list()

    ## takes in the current grid
    ## returns result of evaluation function on current board state
    def evaluate(self, grid):
        return 0
