import os.path
import time
import copy
import parsing
from gametree import GameTree
from minimax import minimax


# while not at endgame, waits for our turn, reads opponent move, then writes a move
def main():
    end = True
    firstMove = True
    tree = None
    grid = [['e' for x in range(0,15)] for x in range(0,15)]
    occupied = set()
    while (end):
        print(occupied)
        presenceGo()
        if os.path.exists("end_game"):
            end = False
            break
        opponent_move = read_move()

        if opponent_move is not None and firstMove is False:
            occupied.add((opponent_move[2], opponent_move[1]))
        if firstMove is True:
            firstMove = False
            tree = GameTree(True, 7, 7)
            grid[7][7] = 'o'
            write_move(7,7)
            occupied.add((7,7))
        else:
            best_value, chosen_state, actions = minimax(tree.root, -float('inf'), float('inf'), True, 2, occupied)
            x = 0
            y = 0

            heuristic3 = list()
            heuristic2 = list()
            heuristic1 = list()
            heuristic0 = list()
            move_coord = None
            for action in actions:
                x = action[0]
                y = action[1]
                new_grid = copy.deepcopy(grid)
                if new_grid[x][y] is 'e':
                    new_grid[x][y] = 'o'
                    heuristic, coordinate = evaluate(new_grid)
                    if heuristic > -1:
                        if heuristic is 0:
                            heuristic0.append(coordinate)
                        if heuristic is 1:
                            heuristic1.append(coordinate)
                        if heuristic is 2:
                            heuristic2.append(coordinate)
                        if heuristic is 3:
                            heuristic3.append(coordinate)
            if len(heuristic0) > 0:
                move_coord= heuristic0[0]
            if len(heuristic1) > 0:
                move_coord= heuristic1[0]
            if len(heuristic2) > 0:
                move_coord= heuristic2[0]
            if len(heuristic3) > 0:
                move_coord= heuristic3[0]

            break_flag = False
            if move_coord is None:
                for x in range(0, 15):
                    if break_flag is True:
                        break
                    for y in range(0, 15):
                        if grid[x][y] is 'e':
                            break_flag = True
                            write_move(x, y)
                            grid[x][y] = 'o'
                            break
            else:
                tree.root = chosen_state
                write_move(move_coord[0],move_coord[1])
                occupied.add((move_coord[0],move_coord[1]))


# reads the file move_file and returns the parses the move as a list
def read_move():
    file = "move_file"
    f = open(file, "r")

    move = f.read().split()
    if (len(move) < 3):
        return None
    move[2] = int(move[2])-1
    move[1] = getColIndex(move[1]) #converts to index form
    f.close()
    return move


# takes a columns and row and writes a move to move_file
def write_move(column, row):
    file = "move_file"
    f = open(file, 'w')

    move = "Terrance " + getColName(column) + " " + str(row+1) # converts to final output
    f.write(move)
    f.close()


# polls for presence of our team's .go file at a rate of 50Hz
def presenceGo():
    while (True):
        if (os.path.exists("Terrance.go")):
            break
        time.sleep(.05)

#takes a column string and returns an index
def getColIndex(string):
    return ord((string.lower())) - ord('a')


#takes a column index and returns a string
def getColName(col):
    return chr(col+ord('a'))


    ## takes in the current grid
    ## returns result of evaluation function on current board state
def evaluate(grid):
    heuristic = -1
    row_list = parsing.getRows(grid)
    col_list = parsing.getCols(grid)
    fwd_diag_list, fwd_diag_coord = parsing.getFwdDiags(grid)
    back_diag_list, back_diag_coord = parsing.getBackDiags(grid)

    ## recognizes board states that will lead to an future win
    two_win_strings = parsing.winInTwo()
    two_win_result = parsing.checkBoard(row_list, col_list, fwd_diag_list,
                                            fwd_diag_coord, back_diag_list, back_diag_coord, two_win_strings)
    if two_win_result is not False:
        heuristic = 0

    ## recognizes board states that will lead to a future loss
    two_lose_strings = parsing.loseInTwo()
    two_lose_result = parsing.checkBoard(row_list, col_list, fwd_diag_list,
                                            fwd_diag_coord, back_diag_list, back_diag_coord, two_lose_strings)
    if two_lose_result is not False:
        heuristic = 1

    ## recognizes board states that will lead to an immediate win
    win_strings = parsing.winningStrings()
    win_strings_result = parsing.checkBoard(row_list, col_list, fwd_diag_list,
                                            fwd_diag_coord, back_diag_list, back_diag_coord, win_strings)
    if win_strings_result is not False:
        heuristic = 2

    ## recognizes board states that will lead to a loss
    defend_top_priority = parsing.topPriority()
    top_priority_result = parsing.checkBoard(row_list, col_list, fwd_diag_list,
                              fwd_diag_coord, back_diag_list, back_diag_coord, defend_top_priority)
    if top_priority_result is not False:
        heuristic = 3

    if heuristic is 0:
        return (0, two_win_result)
    if heuristic is 1:
        return (1, two_lose_result)
    if heuristic is 2:
        return (2, win_strings_result)
    if heuristic is 3:
        return (3, top_priority_result)

    return (-1, None)


# MAIN CALL
if __name__ == "__main__":
    main()
