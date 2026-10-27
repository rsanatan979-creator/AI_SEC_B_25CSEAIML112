def print_board(board):
    for row in board:
        print(" ".join(row))


def is_safe(board, row, col):
    for i in range(col):
        if board[row][i] == 'Q':
            return False

    i = row - 1
    j = col - 1

    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    i = row + 1
    j = col - 1

    while i < 8 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i += 1
        j -= 1

    return True


def solve(board, col):
    if col == 8:
        return True

    for row in range(8):
        if is_safe(board, row, col):
            board[row][col] = 'Q'

            if solve(board, col + 1):
                return True

            board[row][col] = '-'

    return False


board = [['-' for _ in range(8)] for _ in range(8)]

if solve(board, 0):
    print("Solution for the 8-Queens problem:")
    print_board(board)
else:
    print("No solution exists.")