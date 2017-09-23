import os.path
import time

def main():

     end = 1
     while(end):
        presenceGo()
        if (os.path.exists("end_game")):
            end = 0
            break
        print "Our Turn"

        opponent_move = read_move()
        #AB Pruning and MiniMax algorithms

        write_move("A", 1)


def read_move():
    file = "move_file"
    f = open(file, "r")

    move = f.read().split()
    else:
        print "No Move in File"

    #add move to board
    print "File Read"
    f.close()


def write_move(column,row):
    file = "move_file"
    f = open(file, 'w')

    move = "Terrance " + str(column) + " " + str(row)
    print move
    f.write(move)

    print "File Written"
    f.close()


def presenceGo():
    while(True):
        if(os.path.exists("Terrance.go")):
            return
        time.sleep(.05)


if __name__ == "__main__":
    main()

