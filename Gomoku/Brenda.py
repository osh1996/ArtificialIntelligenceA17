import os
import time

def main():
    board = [['e' for x in range(0,15)] for x in range(0,15)]
    end = True
    while (end):
        presenceGo()
        if os.path.exists("end_game"):
            end = False
            break
        opponent_move = read_move()
        if opponent_move == None:
            board[0][0] = 'o'
            write_move(0,0)
        else:
            opp_x = int(opponent_move[2])
            opp_y = int(opponent_move[1])

            board[opp_x][opp_y] = 'o'
            flag = False
            for x in range(0,15):
                if flag is True:
                    break
                for y in range(0,15):
                    if board[x][y] is 'e':
                        flag = True
                        write_move(x,y)
                        board[x][y] = 'o'
                        break




# reads the file move_file and returns the parses the move as a list
def read_move():
    file = "move_file"
    time.sleep(1)
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

    move = "Brenda " + getColName(column) + " " + str(row+1) # converts to final output
    print move
    f.write(move)

    print "File Written"
    f.close()


# polls for presence of our team's .go file at a rate of 50Hz
def presenceGo():
    while (True):
        if (os.path.exists("Brenda.go")):
            break
        time.sleep(.05)

#takes a column string and returns an index
def getColIndex(string):
    if string == 'A' or string == 'a':
        return 0
    if string == 'B' or string == 'b':
        return 1
    if string == 'C' or string == 'c':
        return 2
    if string == 'D' or string == 'd':
        return 3
    if string == 'E' or string == 'e':
        return 4
    if string == 'F' or string == 'f':
        return 5
    if string == 'G' or string == 'g':
        return 6
    if string == 'H' or string == 'h':
        return 7
    if string == 'I' or string == 'i':
        return 8
    if string == 'J' or string == 'j':
        return 9
    if string == 'K' or string == 'k':
        return 10
    if string == 'L' or string == 'l':
        return 11
    if string == 'M' or string == 'm':
        return 12
    if string == 'N' or string == 'n':
        return 13
    if string == 'O' or string == 'p':
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


if __name__ == "__main__":
    main()