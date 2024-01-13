#!/usr/bin/python3
"""
The N queens puzzle
"""
import sys


def is_safe(board, row, col, N):
    # Check if the current position is safe for a queen
    # Check the row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check the upper diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check the lower diagonal
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(N):
    board = [[0] * N for _ in range(N)]
    solutions = []
    solve_util(board, 0, N, solutions)
    return solutions


def solve_util(board, col, N, solutions):
    if col >= N:
        solution = []
        for i in range(N):
            row_str = ""
            for j in range(N):
                if board[i][j] == 1:
                    row_str += "Q"
                else:
                    row_str += "."
            solution.append(row_str)
        solutions.append(solution)
        return True

    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1

            solve_util(board, col + 1, N, solutions)

            board[i][col] = 0

    return False


def print_solutions(solutions):
    for solution in solutions:
        for row in solution:
            print(row)
        print()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(N)
    for solution in solutions:
        for row in solution:
            print(row)
        print()
