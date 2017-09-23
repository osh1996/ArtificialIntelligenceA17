import os
import time


def loop():
     end = 1
     while(end):
        presenceGo()
        if (os.path.isFile("end_game")):
            end = 0
        read_move()
        #AB Pruning and MiniMax algorithms
        move = 0
        write_move(move)




def read_move():
    a = 1

def write_move(move):
    b = 1

def presenceGo():
    while(True):
        if(os.path.isfile("Terrance.go")):
            return
        time.sleep(.05)
