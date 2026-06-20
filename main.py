from view_window import run_window
from sudoku_generator import generator

empty_board = [[0 for _ in range(9)] for _ in range(9)]
empty_board[0][0] = 3

if __name__ == '__main__':
    board = generator(empty_board, 1)
    run_window(board)