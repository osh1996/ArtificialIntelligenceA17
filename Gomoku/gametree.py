from gamestate import GameState

class GameTree:

    def __init__(self, we_go_first, x, y):
        init_grid = [['e' for x in range(0,15)] for x in range(0,15)]
        if we_go_first:
            init_grid[x][y] = 'o'
        else:
            init_grid[x][y] = 'x'
        self.root = GameState(init_grid, x, y)

    def printTree(self):
        print(self.root.coordinate)
        for state in self.root.successors:
            self.printTree(state)