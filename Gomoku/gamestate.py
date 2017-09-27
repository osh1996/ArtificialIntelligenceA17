class GameState:

    def __init__(self, grid, x, y):
        self.grid = grid
        self.eval = 0
        self.coordinate = (x,y)
        self.successors = list()

    def addMove(self, moveList):
        player = moveList[0]
        column = moveList[1]
        row = moveList[2]