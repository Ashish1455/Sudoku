def row_rule(board, i, num):
    return True if num not in board[i] else False

def column_rule(board, i, num):
    return True if num not in [board[r][i] for r in range(9)] else False

def square_rule(board, row, col, num):
    r = 3*(row//3)
    c = (col//3)*3
    for i in range(3):
        for j in range(3):
            if board[r + i][c + j] == num:
                return False
    return True

def normal_rules(board, row, col, num):
    r = row_rule(board, row, num)
    c = column_rule(board, col, num)
    s = square_rule(board, row, col, num)
    return r&c&s