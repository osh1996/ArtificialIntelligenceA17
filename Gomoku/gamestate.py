class GameState:

    def __init__(self, grid):
        self.grid = grid
        self.eval = 0

    def addMove(self, moveList):
        player = moveList[0]
        column = moveList[1]
        row = moveList[2]