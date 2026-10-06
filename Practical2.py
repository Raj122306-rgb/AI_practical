#N-queen problem
"""
def print_board(board):
    for row in board:
        print(" ".join(row))
    print()


def check_q(board, row, col, n):

    # Check column
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    # Check upper-left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1

    return True


def solve_queens(board, row, n):

    if row == n:
        print_board(board)
        return True

    for col in range(n):
        if check_q(board, row, col, n):
            board[row][col] = 'Q'

            if solve_queens(board, row + 1, n):
                return True

            board[row][col] = '.'

    return False


def queens():
    n = int(input("Enter value of N: "))

    board = []

    for i in range(n):
        row = []
        for j in range(n):
            row.append('.')
        board.append(row)

    if not solve_queens(board, 0, n):
        print("No solution found")


queens()
"""
#tower of hanoi
def hanoi(n, source, helper, destination):

    if n == 1:
        print("Move Disk 1 from", source, "to", destination)

    else:
        hanoi(n - 1, source, destination, helper)

        print("Move Disk", n, "from", source, "to", destination)

        hanoi(n - 1, helper, source, destination)


n = int(input("Enter number of disks: "))

hanoi(n, "A", "B", "C")
