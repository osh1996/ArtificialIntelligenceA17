import math
import numpy
from copy import copy

def minimax(state, alpha, beta, maximizing, depth, maxp, minp):
    if depth == 0:
        return evalState(state), state
    rowsLeft, columnsLeft = numpy.where(state == 0)     ##generate list of potential actions
    returnState = copy(state)
    if rowsLeft.shape[0] == 0:      ##if board is full
        return evalState(state), returnState
    if maximizing is True:
        utility = -float("inf")
        for i in range(0, rowsLeft.shape[0]):
            nextState = copy(state)
            nextState[rowsLeft[i], columnsLeft[i]] = maxp
            # print 'in max currently the Nextstate is ',nextState,'\n\n'
            newUtility, newState = minimax(nextState, alpha, beta, False, depth - 1, maxp, minp)
            if newUtility > utility:
                utility = newUtility
                returnState = copy(nextState)
            if utility > alpha:
                alpha = utility
            if alpha >= beta:
                # print 'pruned'
                break
            # print 'for max the best move is with utility ',utility,' n state ',returnState
        return utility, returnState
    else:
        utility = float("inf")
        for i in range(0, rowsLeft.shape[0]):
            nextState = copy(state)
            nextState[rowsLeft[i], columnsLeft[i]] = minp
            # print 'in min currently the Nextstate is ',nextState,'\n\n'
            newUtility, newState = minimax(nextState, alpha, beta, True, depth - 1, maxp, minp)
            if newUtility < utility:
                utility = newUtility
                returnState = copy(nextState)
            if utility < beta:
                beta = utility
            if alpha >= beta:
                # print 'pruned'
                break
        return utility, returnState


def evalState(state):
    # placeholder function to evaluate state for possiblity of winning
    grid = state.grid
   # parseGrid(grid)

    heuristic = 0
    return heuristic

def generateActions(state):
    # get grid with 1 layer of empties around current board
    gridSize = (8,8)
    first = (3,3)       # tile in the top left corner of trimmed game grid
    actions = list()

    for x in range(first[0], first[0]+gridSize[0]):
        for y in range(first[1], first[1]+gridSize[1]):
            if state.grid[x][y] is "e":
                newAction = (x, y)
                actions.append(newAction)
    return actions



