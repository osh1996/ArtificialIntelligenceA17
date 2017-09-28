import parsing

class GameState:

    def __init__(self, grid, x, y):
        self.grid = grid
        self.utility = 0
        self.coordinate = (x,y)
        self.successors = list()

    ## takes in the current grid
    ## returns result of evaluation function on current board state
    def evaluate(self, grid):
        heuristic = 0
        row_list = parsing.getRows(grid)
        col_list = parsing.getCols(grid)
        fwd_diag_list, fwd_diag_coord = parsing.getFwdDiags(grid)
        back_diag_list, back_diag_coord = parsing.getBackDiags(grid)

        ## recognizes board states that will lead to a loss
        defend_top_priority = parsing.topPriority()
        top_prio_flag = False
        top_priority_result = parsing.checkBoard(row_list, col_list, fwd_diag_list,
                                  fwd_diag_coord, back_diag_list, back_diag_coord, defend_top_priority)
        if top_priority_result is True:
            top_prio_flag = True

        ## recognizes board states that will lead to a fairly immediate win
        win_strings = parsing.winningStrings()
        win_flag = False
        win_strings_result = parsing.checkBoard(row_list, col_list, fwd_diag_list,
                                                 fwd_diag_coord, back_diag_list, back_diag_coord, win_strings)
        if win_strings_result is True:
            win_flag = True

        if top_prio_flag:
            if win_flag:
                heuristic = 0 ##placeholder
                ##figure out what to do when theres a winning and losing state
            else:
                heuristic = -1
        else:
            if win_flag:
                heuristic = 1
        return heuristic