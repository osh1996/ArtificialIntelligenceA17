import numpy as np
import time


# takes a board and returns a list of the rows of the board formatted as strings
# tested
def getRows(board):
    boardAsList = list(board)
    rowList = list()
    for row in boardAsList:
        rowString = ""
        for item in row:
            rowString = rowString + str(item)
        rowList.append(rowString)
    return rowList


# takes board and returns a list of the columns of the board formatted as strings\
# tested
def getCols(board):
    boardAsList = list(board)
    colList = list()
    for i in range(0, 14):
        colString = ""
        for row in boardAsList:
            colString = colString + str(row[i])
        colList.append(colString)
    return colList


# takes a board and returns the top -> bottom diagonals as a list of strings
# tested
def getFwdDiags(board):
    diagList = list()
    cList = list()
    startRow = 10
    startCol = 0
    while startRow > -1:
        diagString = ''
        coordList = list()
        row = startRow
        col = startCol
        while row < 15:
            diagString = diagString + str(board[row][col])
            coord = (row, col)
            coordList.append(coord)
            row = row + 1
            col = col + 1
        diagList.append(diagString)
        cList.append(coordList)
        startRow = startRow - 1

    startCol = 1
    startRow = 0
    while startCol < 11:
        diagString = ''
        coordList = list()
        row = startRow
        col = startCol
        while col < 15:
            diagString = diagString + str(board[row][col])
            coord = (row, col)
            coordList.append(coord)
            row = row + 1
            col = col + 1
        diagList.append(diagString)
        cList.append(coordList)
        startCol = startCol + 1
    return diagList, cList


# takes a board and returns the bottom -> top diagonals as a list of strings
# tested
def getBackDiags(board):
    diagList = list()
    cList = list()

    startRow = 14
    startCol = 10
    while startCol > -1:
        diagString = ''
        coordList = list()
        row = startRow
        col = startCol
        while col < 15:
            diagString = diagString + str(board[row][col])
            coord = (row, col)
            coordList.append(coord)
            row = row - 1
            col = col + 1
        diagList.append(diagString)
        cList.append(coordList)
        startCol = startCol - 1

    startRow = 13
    startCol = 0
    while startRow > 3:
        diagString = ''
        coordList = list()
        row = startRow
        col = startCol
        while row > -1:
            diagString = diagString + str(board[row][col])
            coord = (row, col)
            coordList.append(coord)
            row = row - 1
            col = col + 1
        diagList.append(diagString)
        cList.append(coordList)
        startRow = startRow - 1
    return diagList, cList


# top priority moves
def topPriority():
    l = list()
    l.append('x' 'e' 'x' 'x' 'x')
    l.append('xxexx')
    l.append('xxxex')
    l.append('oxxxxe')
    l.append('xexxx'[::-1])
    l.append('xxexx'[::-1])
    l.append('xxxex'[::-1])
    l.append('oxxxxe'[::-1])
    return l


# checks rows for any top priority moves and returns a tuple of the best move
# tested
def checkRows(rowList, searchList):
    i = 0
    for item in rowList:
        for case in searchList:
            index = item.find(case)
            if (index > -1):
                addIndex = case.find('e')
                coord = (i, index + addIndex)
                return coord
        i += 1


# checks columns for any top priority moves and returns a tuple of the best move
# tested
def checkCols(colList, searchList):
    i = 0
    topList = topPriority()
    for item in colList:
        for case in searchList:
            index = item.find(case)
            if (index > -1):
                addIndex = case.find('e')
                coord = (index + addIndex, i)
                return coord
        i += 1


# checks forward diagonals for top priority moves and returns a tuple
# tested
def checkFwdDiags(fwdDiagList, coordList, searchList):
    i = 0
    for item in fwdDiagList:
        for case in searchList:
            index = item.find(case)
            if (index > -1):
                addIndex = case.find('e')
                coord = coordList[i][index + addIndex]
                return coord
        i += 1


# checks the backward diagonals for top priority moves and returns a tuple
# tested
def checkBackDiags(backDiagList, coordList, searchList):
    i = 0
    for item in backDiagList:
        for case in searchList:
            index = item.find(case)
            if (index > -1):
                addIndex = case.find('e')
                coord = coordList[i][index + addIndex]
                return coord
        i += 1

#testing stuff

# board = np.identity(15, int)
# startTime = time.time()
# #print "GETROWS"
# print getRows(board)
# #print "GETCOLS/n"
# print getCols(board)
# #print "FWDDIAGS/n"
# diagList, coordList = getFwdDiags(board)
# #print "BACKDIAGS/n"
# print getBackDiags(board)
# endTime = time.time() - startTime
# print endTime

# a = np.full((15,15), 'e')
# for i in range(3,10):
#     a[i][10 - i] = 'x'
# for i in range(3,10):
#     a[i][0] = 'x'
# a[8][2] = 'e'
# a[0][4] = 'e'
# print a
# c, d  = getBackDiags(a)
# print checkBackDiags(c,d)