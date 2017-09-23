import math


def minimax(state, alpha, beta, maximizing, depth, maxp, minp):
    if depth == 0:
        return evalState(state), state
        rowsLeft, columnsLeft = np.where(state == 0)
    returnState = copy(state)
    if rowsLeft.shape[0] == 0:
        return evalState(state), returnState
    if maximizing == True:
        utility = -math.inf
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
                break;
            # print 'for max the best move is with utility ',utility,' n state ',returnState
        return utility, returnState
    else:
        utility = math.inf
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
                break;
        return utility, returnState


def evalState(state):
    # placeholder function to evaluate state for possiblity of winning
    heuristic = 0
    return heuristic
