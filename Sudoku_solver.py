from rules import normal_rules

def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

def backtrack(board):
    empty = find_empty(board)
    if not empty:
        return True
    row, col = empty
    for i in range(1, 10):
        if normal_rules(board, row, col, i):
            board[row][col] = i
            if backtrack(board):
                return True
            board[row][col] = 0
    return False

def solveSudoku(board):
    if backtrack(board):
        return board
    return None