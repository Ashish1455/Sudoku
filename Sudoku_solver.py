from random import shuffle
from rules import normal_rules

def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

def backtrack(board, mode):
    empty = find_empty(board)
    if not empty:
        return True
    row, col = empty
    arr = list(range(1, 10))
    if mode:
        shuffle(arr)

    for i in arr:
        if normal_rules(board, row, col, i):
            board[row][col] = i
            if backtrack(board, mode):
                return True
            board[row][col] = 0
    return False

def solveSudoku(board, mode=0):
    if backtrack(board, mode):
        return board
    return None