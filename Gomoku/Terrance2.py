import os.path
import time
from gametree import GameTree
from minimax import minimax


# while not at endgame, waits for our turn, reads opponent move, then writes a move
def main():
    occupied = set()
    end = True
    firstMove = True
    tree = None
    while (end):
        presenceGo()
        if os.path.exists("end_game"):
            end = False
            break

        opponent_move = read_move()
        if opponent_move is not None:
            occupied.add((opponent_move[2], opponent_move[1]))
        if firstMove is True:
            if(opponent_move == None):
                firstMove = False
                tree = GameTree(True, 7, 7)
                write_move(7,7)
                occupied.add((7,7))
            else:
                firstMove = False
                tree = GameTree(False, opponent_move[2], opponent_move[1])
                tree.getNewRoot(opponent_move)
                best_value, chosen_state = minimax(tree.root, -float('inf'), float('inf'), False, 3, occupied)
                x, y = chosen_state.coordinate
                write_move(x,y)
                occupied.add((x,y))
        else:
            tree.getNewRoot(opponent_move)
            best_value, chosen_state = minimax(tree.root, -float('inf'), float('inf'), True, 3, occupied)
            value = chosen_state.evaluate(chosen_state.grid)
            #if value is -1:

            x, y = chosen_state.coordinate
            tree.root = chosen_state
            write_move(x,y)
            occupied.add((x,y))






# reads the file move_file and returns the parses the move as a list
def read_move():
    file = "move_file"
    f = open(file, "r")

    move = f.read().split()
    if (len(move) < 3):
        #print "No Move in File"
        return None
    move[2] = int(move[2])-1
    move[1] = getColIndex(move[1]) #converts to index form
    # print "MOVES"
    # print move
    # print move[1]
    # print move[2]
    f.close()
    return move


# takes a columns and row and writes a move to move_file
def write_move(column, row):
    file = "move_file"
    f = open(file, 'w')

    move = "Terrance2 " + getColName(column) + " " + str(row+1) # converts to final output
    f.write(move)
    f.close()


# polls for presence of our team's .go file at a rate of 50Hz
def presenceGo():
    while (True):
        if (os.path.exists("Terrance2.go")):
            break
        time.sleep(.05)

#takes a column string and returns an index
def getColIndex(string):
    return ord((string.lower())) - ord('a')


#takes a column index and returns a string
def getColName(col):
    return chr(col+ord('a'))


# MAIN CALL
if __name__ == "__main__":
    main()
