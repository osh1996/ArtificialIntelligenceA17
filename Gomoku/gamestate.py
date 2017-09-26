class GameState:

    def __init__(self, grid, alpha, beta):
        self.grid = grid
        self.eval = 0
        self.successors = list()


    def addMove(self, moveList):
        player = moveList[0]
        column = moveList[1]
        row = moveList[2]