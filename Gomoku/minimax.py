import numpy as np
from copy import copy
from gamestate import GameState
import parsing

def minimax(state, alpha, beta, maximizing, depth, occupied):
    if depth == 0:
        return evalGoalState(state), state
    actions = generateActions(state, occupied)     ##generate list of potential actions
    returnState = copy(state)
    if len(actions) == 0:      ##if board is full
        return evalGoalState(state), returnState
    if maximizing is True:
        for action in actions:
            new_action = copy(action)
            new_grid = state.grid
            new_grid[new_action[0]][new_action[1]] = "o"
            nextState = GameState(new_grid, new_action[0], new_action[1])
            state.successors.append(nextState)
            newUtility, newState = minimax(nextState, alpha, beta, False, depth - 1, occupied)
            if newUtility > state.utility:
                state.utility = newUtility
                returnState = copy(nextState)
            if state.utility > alpha:
                alpha = state.utility
            if alpha >= beta:
                # print 'pruned'
                break
            # print 'for max the best move is with utility ',utility,' n state ',returnState
        return state.utility, returnState
    else:
        nextState = 0
        for action in actions:
            new_action = copy(action)
            new_grid = state.grid
            new_grid[new_action[0]][new_action[1]] = "x"
            nextState = GameState(new_grid, new_action[0], new_action[1])
            returnState = nextState
            state.successors.append(nextState)
            newUtility, newState = minimax(nextState, alpha, beta, True, depth - 1, occupied)
            if newUtility < state.utility:
                state.utility = newUtility
            if state.utility < beta:
                beta = state.utility
                returnState = newState
            if alpha >= beta:
                # print 'pruned'
                break
        return state.utility, returnState


def evalGoalState(state):
    grid = state.grid
    heuristic = 0
    row_list = parsing.getRows(grid)
    col_list = parsing.getCols(grid)
    fwd_diag_list, fwd_diag_coord = parsing.getFwdDiags(grid)
    back_diag_list, back_diag_coord = parsing.getBackDiags(grid)

    lose_string = ['xxxxx']
    win_string = ['ooooo']

    opponent_win = parsing.checkBoard(row_list, col_list, fwd_diag_list,
                                  fwd_diag_coord, back_diag_list, back_diag_coord, lose_string)
    we_win = parsing.checkBoard(row_list, col_list, fwd_diag_list,
                                  fwd_diag_coord, back_diag_list, back_diag_coord, win_string)
    if opponent_win is True:
        heuristic = -1
    if we_win is True:
        heuristic = 1

    return heuristic

def generateActions(state, occupied):
    actions = list()
    coordinate = state.coordinate
    flag = False

    xx = state.coordinate[0]
    yy = state.coordinate[1]

    ## checks adjacent tiles
    for x in range(max(xx-1, 1), min(xx+1, 15)):
        for y in range(max(yy-1, 1), min(yy+1, 15)):
            if state.grid[x][y] is "e":
                newAction = (x, y)
                if newAction not in occupied:
                    actions.append(newAction)
                    flag = True
    if not flag:
        for x in range(0,15):
            for y in range(0,15):
                if state.grid[x][y] is 'e':
                    newAction = (x, y)
                    if newAction not in occupied:
                        actions.append(newAction)
    return actions



