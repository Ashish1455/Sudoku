import random
from Sudoku_solver import find_empty
from Sudoku_solver import solveSudoku
from rules import normal_rules

def solution_counter(board):

    empty = find_empty(board)
    if not empty:
        return 1

    row, col = empty
    arr = list(range(1, 10))
    count = 0

    for i in arr:
        if normal_rules(board, row, col, i):
            board[row][col] = i
            count += solution_counter(board)
            board[row][col] = 0
            if count > 1:
                return count

    return count

def core(board, difficulty):

    goal_cells = 40 - 2*difficulty - random.randrange(2)
    filled_cells = 81

    while filled_cells > goal_cells:
        row, col = random.randrange(9), random.randrange(9)
        if board[row][col] != 0:
            temp, board[row][col] = board[row][col], 0
            solutions = solution_counter(board)
            if solutions != 1:
                board[row][col] = temp
            else:
                filled_cells -= 1

    return board


def generator(board, difficulty):
    board = solveSudoku(board, 1)
    return core(board, difficulty)


if __name__ == '__main__':
    board1 = [[0 for _ in range(9)] for _ in range(9)]
    board1[0][0] = 3
    difficulty1 = random.randrange(1, 11)
    generator(board1, difficulty1)