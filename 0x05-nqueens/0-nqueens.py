#!/usr/bin/python3
"""Solving N Queens Problem"""
import sys

def printSolution(board):
    """Print allocated positions to the queen"""
    solution = []

    for r in range(len(board)):
        for c in range(len(board)):
            if c == board[r]:
                solution.append([r, c])
    print(solution)

def is_position_safe(board, r, c, row):
    """Checks if the position is safe for the queen"""
    return board[r] in (c, c - r + row, r - row + c)

def recursive_solve(board, row):
    """Find all safe positions where the queen can be allocated"""
    n = len(board)
    if row == n:
        printSolution(board)
    else:
        for c in range(n):
            allowed = True
            for r in range(row):
                if is_position_safe(board, r, c, row):
                    allowed = False
            if allowed:
                board[row] = c
                recursive_solve(board, row + 1)

def create_board(size):
    """Generates the board"""
    return [0] * size

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    N = int(sys.argv[1])
    myboard = create_board(N)
    recursive_solve(myboard, 0)
