import numpy as np

global N
N = 4


def printSolution(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j])


# check whether there is a conflict
def isSafe(board, row, col):
    # check the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # check lower diagonal on left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True


def nQueen(board, col):
    # 递归函数的出口条件
    # if all queens are placed then return True
    if col == N:
        return True

    for i in range(N):
        if isSafe(board, i, col):
            board[i][col] = 1
            if nQueen(board, col + 1) == True:
                return True
            board[i][col] = 0
    return False


def solveNQ():
    board = np.zeros((4, 4), dtype=int)
    if nQueen(board, 0) == False:
        print("Solution does not exist")
        return False

    printSolution(board)
    return True


if __name__ == "__main__":
    solveNQ()
