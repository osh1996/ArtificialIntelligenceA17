from gamestate import GameState
class Minimax:

    def __init__(self):
        initGrid = [['e' for x in range(15)] for y in range(15)]
        self.root = GameState(initGrid, -float('inf'), float('inf'), "t")