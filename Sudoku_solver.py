from random import shuffle
from rules import normal_rules

def precompute_cells():
    Used = {}
    for row in range(9):
        for col in range(9):
            used = {(i, col) for i in range(9)}
            used |= {(row, i) for i in range(9)}
            r, c = 3*(row//3), 3*(col//3)
            used |= {(r+i, c+j) for i in range(3) for j in range(3)}
            used.discard((row, col))
            Used[(row, col)] = used
    return Used

def possible_cells(board, row, col, cells):
    return list(set(range(1, 10)) - {board[r][c] for r, c in cells[(row, col)]})

def mrv(board, cells):
    best, best_digits = None, None
    for r in range(9):
        for c in range(9):
            if not board[r][c]:
                digits = possible_cells(board, r, c, cells)
                if not digits:
                    return (r, c), []
                if best is None or len(digits) < len(best_digits):
                    best, best_digits = (r, c), digits
                    if len(digits) == 1:
                        return best, best_digits
    return best, best_digits

def backtrack(board, mode, cells):
    rc, arr = mrv(board, cells)
    if not rc:
        return True
    row, col = rc

    if mode:
        shuffle(arr)

    for i in arr:
        board[row][col] = i
        if backtrack(board, mode, cells):
            return True
        board[row][col] = 0
    return False

def solveSudoku(board, mode=0):
    cells = precompute_cells()
    if backtrack(board, mode, cells):
        return board
    return None