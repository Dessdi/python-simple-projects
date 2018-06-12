import numpy as np

def drawGameBoard(matrix):
    sign = " "
    for n in range(0, len(matrix)):
        for i in range(0, len(matrix)):
            print(" ---   ", end="\t")
        print("\n")
        for j in range(0, len(matrix)):
            if matrix[n][j] == 1:
                sign = "o"
            elif matrix[n][j] == 2:
                sign = "x"
            elif matrix[n][j] == 0:
                sign = " "
            print("|  " + sign, end="\t", )
        print("|\n")

    for i in range(0, len(matrix)):
        print(" ---", end="\t")
    print("\n")

def checkColumn(matrix, columnNumber):
    result = False
    for i in range(1, len(matrix)):
        if matrix[0][columnNumber] > 0:
            if matrix[i][columnNumber] == matrix[0][columnNumber]:
                result = True
            else:
                result = False
                break
        else:
            result = False
            break
    return result

def checkRow(matrix, rowNumber):
    result = False
    for i in range(1, len(matrix)):
        if matrix[rowNumber][0] > 0:
            if matrix[rowNumber][i] == matrix[rowNumber][0]:
                result = True
            else:
                result = False
                break
        else:
            result = False
            break
    return result

def checkDiagonal(matrix):
    result = False
    for i in range(1, len(matrix)):
        if matrix[0][0] != 0:
            if matrix[i][i] == matrix[0][0]:
                result = True
            else:
                result = False
                break
        else:
            result = False
            break

    if result == False:
        for i in range(1, len(matrix)):
            if matrix[0][len(matrix)-1] > 0:
                if matrix[i][len(matrix)-1-i] == matrix[0][len(matrix)-1]:
                    result = True
                else:
                    result = False
                    break
            else:
                result = False
                break
    return result

def checkWinner(matrix):

    isWinner = False
    for i in range(len(matrix)):
        isWinner = checkRow(matrix, i)
        if isWinner == True:
            break

    if isWinner == False:
        for i in range(len(matrix)):
            isWinner = checkColumn(matrix, i)
            if isWinner == True:
                break
    if isWinner == False:
        isWinner = checkDiagonal(matrix)
    return isWinner

def setFieldValue(matrix, user):
    print("user: " + str(user))
    row = int(input("select row: ")) - 1
    column = int(input("select column: ")) - 1

    while row >= len(matrix) or column >= len(matrix) or matrix[row][column] != 0:
        print("select empty field \n")
        row = int(input("select row: "))
        column = int(input("select column: "))

    matrix[row][column] = user
    drawGameBoard(matrix)
    return matrix

def play(matrix):

    freeFields = sum(x.count(0) for x in matrix)

    while checkWinner(matrix) == False:

        for i in range(1, 3):
            if freeFields > 0:
                matrix = setFieldValue(matrix, i)
                freeFields = sum(x.count(0) for x in matrix)
                if checkWinner(matrix) == True:
                    print("winner is player " + str(i))
                    break
            else:
                print("no winner ")
                break

        if freeFields == 0:
            break


game = ([0, 0, 0], [0, 0, 0], [0, 0, 0])
play(game)