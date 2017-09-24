import numpy
from gamestate import GameState

class GameTree:

    def __init__(self):
        init_grid = numpy.array([['e' for x in range(15)] for y in range(15)], numpy.string_)
        self.root = GameState(init_grid, -float('inf'), float('inf'), "t")