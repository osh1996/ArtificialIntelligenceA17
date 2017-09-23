import os.path
import time







def main():
     end = 1
     while(end):
        presenceGo()
        if (os.path.exists("end_game")):
            end = 0
        read_move()
        #AB Pruning and MiniMax algorithms
        move = 0
        write_move(move)

def read_move():
    file = "move_file"
    f = open(file, "r")
    move = f.read()
    print move



def write_move(move):
    b = 1

def presenceGo():
    while(True):
        if(os.path.exists("Terrance.go")):
            print "Our Turn"
            return
        time.sleep(.05)

if __name__ == "__main__":
    main()