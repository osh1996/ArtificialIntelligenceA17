import os.path
import time
from gametree import GameTree
from minimax import minimax


# while not at endgame, waits for our turn, reads opponent move, then writes a move
def main():
    end = True
    color = ''
    firstMove = True
    while (end):
        tree = None
        presenceGo()
        if os.path.exists("end_game"):
            end = False
            break
        print "Our Turn"

        opponent_move = read_move()
        if firstMove is True:
            if(opponent_move == None):
                tree = GameTree(True, 7, 7)
                write_move(7,7)
                firstMove = False
            else:
                tree = GameTree(False, opponent_move[2], opponent_move[1])
                best_value, chosen_state = minimax(tree.root, -float('inf'), float('inf'), False, 10)
                x, y = chosen_state.coordinate
                write_move(x,y)
                firstMove = False
        else:
            assert tree is not None
            tree.getNewRoot(opponent_move)
            best_value, chosen_state = minimax(tree.root, -float('inf'), float('inf'), True, 10)
            x, y = chosen_state.coordinate
            tree.root = chosen_state
            write_move(x,y)






# reads the file move_file and returns the parses the move as a list
def read_move():
    file = "move_file"
    f = open(file, "r")

    move = f.read().split()
    if (len(move) < 3):
        print "No Move in File"
        return None
    move[2] = move[2]-1
    move[1] = getColIndex(move[1]) #converts to index form

    f.close()
    return move


# takes a columns and row and writes a move to move_file
def write_move(column, row):
    file = "move_file"
    f = open(file, 'w')

    move = "Terrance " + getColName(column) + " " + str(row+1) # converts to final output
    print move
    f.write(move)

    print "File Written"
    f.close()


# polls for presence of our team's .go file at a rate of 50Hz
def presenceGo():
    while (True):
        if (os.path.exists("Terrance.go")):
            break
        time.sleep(.05)

#takes a column string and returns an index
def getColIndex(string):
    if string == 'A':
        return 0
    if string == 'B':
        return 1
    if string == 'C':
        return 2
    if string == 'D':
        return 3
    if string == 'E':
        return 4
    if string == 'F':
        return 5
    if string == 'G':
        return 6
    if string == 'H':
        return 7
    if string == 'I':
        return 8
    if string == 'J':
        return 9
    if string == 'K':
        return 10
    if string == 'L':
        return 11
    if string == 'M':
        return 12
    if string == 'N':
        return 13
    if string == 'O':
        return 14
    return "item not on board"


#takes a column index and returns a string
def getColName(col):
    if col == 0:
        return 'A'
    if col == 1:
        return 'B'
    if col == 2:
        return 'C'
    if col == 3:
        return 'D'
    if col == 4:
        return 'E'
    if col == 5:
        return 'F'
    if col == 6:
        return 'G'
    if col == 7:
        return 'H'
    if col == 8:
        return 'I'
    if col == 9:
        return 'J'
    if col == 10:
        return 'K'
    if col == 11:
        return 'L'
    if col == 12:
        return 'M'
    if col == 13:
        return 'N'
    if col == 14:
        return 'O'
    return "index out of bounds"

# MAIN CALL
if __name__ == "__main__":
    main()
