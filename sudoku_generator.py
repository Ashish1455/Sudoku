import random
from Sudoku_solver import mrv, solveSudoku, precompute_cells
from rules import normal_rules

def postive_diagonal_remove(board, cells):
    removing = (cells // 3 + random.randrange(-cells//9, cells//9))//3

    for i in range(removing):
        row, col = random.randrange(3), random.randrange(3)
        while board[row][col] == 0:
            row, col = random.randrange(3), random.randrange(3)
        board[row][col] = 0
        row, col = random.randrange(3,6), random.randrange(3,6)
        while board[row][col] == 0:
            row, col = random.randrange(3, 6), random.randrange(3, 6)
        board[row][col] = 0
        row, col = random.randrange(6,9), random.randrange(6,9)
        while board[row][col] == 0:
            row, col = random.randrange(6,9), random.randrange(6,9)
        board[row][col] = 0

    return board

def solution_counter(board, cells):
    rc, arr = mrv(board, cells)
    if not rc:
        return 1
    row, col = rc
    count = 0

    for i in arr:
        board[row][col] = i
        count += solution_counter(board, cells)
        board[row][col] = 0
        if count > 1:
            return count
    return count

def core(board, difficulty, cells):
    if difficulty == 11:
        goal_cells = 17
    else:
        goal_cells = 40 - 2*difficulty - random.randrange(2)

    board = postive_diagonal_remove(board, 81 - goal_cells)

    filled_positions = [(r, c) for r in range(9) for c in range(9) if board[r][c] != 0]
    random.shuffle(filled_positions)
    filled_cells = len(filled_positions)

    for row, col in filled_positions:
        if filled_cells <= goal_cells:
            break
        temp, board[row][col] = board[row][col], 0
        solutions = solution_counter(board, cells)
        if solutions != 1:
            board[row][col] = temp
        else:
            filled_cells -= 1

    return board

def generator(board, difficulty):
    cells = precompute_cells()
    board = solveSudoku(board, 1)
    board = core(board, difficulty, cells)
    return board


if __name__ == '__main__':
    board1 = [[0 for _ in range(9)] for _ in range(9)]
    board1[0][0] = 3
    difficulty1 = random.randrange(1, 11)
    generator(board1, difficulty1)