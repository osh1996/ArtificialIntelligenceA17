class GameState:

    def __init__(self, grid, x, y):
        self.grid = grid
        self.eval = 0
        self.coordinate = (x,y)
        self.successors = list()
