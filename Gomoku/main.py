import os.path
import time


# while not at endgame, waits for our turn, reads opponent move, then writes a move
def main():
    end = 1
    while (end):
        presenceGo()
        if (os.path.exists("end_game")):
            end = 0
            print "Reached Endgame"
            break
        print "Our Turn"

        opponent_move = read_move() #

        # AB Pruning and MiniMax algorithms

        write_move("A", 1)


# reads the file move_file and returns the parses the move as a list
def read_move():
    file = "move_file"
    f = open(file, "r")

    move = f.read().split()
    if (len(move) < 3):
        print "No Move in File"
        return None

    print "File Read"
    f.close()
    return move


# takes a columns and row and writes a move to move_file
def write_move(column, row):
    file = "move_file"
    f = open(file, 'w')

    move = "Terrance " + str(column) + " " + str(row)
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


# MAIN CALL
if __name__ == "__main__":
    main()
