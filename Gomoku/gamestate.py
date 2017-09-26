class GameState:

    def __init__(self, grid, alpha, beta, whosMove):
        self.grid = grid
        self.eval = 0
        self.whosMove = whosMove
        self.successors = list()


    def addMove(self, moveList):
        player = moveList[0]
        column = moveList[1]
        row = moveList[2]