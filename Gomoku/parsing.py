import numpy as np

# takes a board and returns a list of the rows of the board formatted as strings
def getRows(board):
    boardAsList = list(board)
    rowList = list()
    for row in boardAsList:
        rowString = ""
        for item in row:
            rowString = rowString + str(item)
        rowList.append(rowString)
    return rowList

#takes board and returns a list of the columns of the board formatted as strings
def getCols(board):
    boardAsList = list(board)
    colList = list()
    for i in range(0,14):
        colString = ""
        for row in boardAsList:
            colString = colString + str(row[i])
        colList.append(colString)
    return colList

# takes a board and returns the top -> bottom diagonals as a list of strings
def getFwdDiags(board):
    diagList = list()

    startRow = 10
    startCol = 0
    while startRow > -1:
        diagString = ''
        row = startRow
        col = startCol
        while row < 15:
            diagString = diagString + str(board[row][col])
            row = row + 1
            col = col + 1
        diagList.append(diagString)
        startRow = startRow - 1

    startCol = 1
    startRow = 0
    while startCol < 11:
        diagString = ''
        row = startRow
        col = startCol
        while col < 15:
            diagString = diagString + str(board[row][col])
            row = row + 1
            col = col + 1
        diagList.append(diagString)
        startCol = startCol + 1
    return diagList

# takes a board and returns the bottom -> top diagonals as a list of strings
def getBackDiags(board):
    diagList = list()

    startRow = 14
    startCol = 10
    while startCol > -1:
        diagString = ''
        row = startRow
        col = startCol
        while col < 15:
            diagString = diagString + str(board[row][col])
            row = row - 1
            col = col - 1
        diagList.append(diagString)
        startCol = startCol - 1

    startRow = 13
    startCol = 0
    while startRow > 3:
        diagString = ''
        row = startRow
        col = startCol
        while row > -1:
            diagString = diagString + str(board[row][col])
            row = row - 1
            col = col - 1
        diagList.append(diagString)
        startRow = startRow - 1
    return diagList


