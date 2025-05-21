#!/usr/bin/python3
"""Task 0"""
import sys


def is_safe(board, row, col, N):
    """
    Check if a queen can be safely placed at (row, col).
    - No queen should be in the same column.
    - No queen should be in the same diagonal.
    """
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(N, row=0, board=[], solutions=[]):
    """
    Recursively solve the N queens problem.
    - N: size of the board (N x N)
    - row: current row to place a queen
    - board: current state, where index is row and value is column of queen
    - solutions: list to collect all valid board configurations
    """
    if row == N:
        # A full solution is found, format as list of [row, col] positions
        solutions.append([[r, board[r]] for r in range(N)])
        return
    for col in range(N):
        if is_safe(board, row, col, N):
            board.append(col)        # Place queen
            solve_nqueens(N, row + 1, board, solutions)
            board.pop()              # Backtrack


def main():
    """
    Entry point of the program. Handles input validation and solution output.
    """
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

    solutions = []
    solve_nqueens(N, board=[], solutions=solutions)
    for sol in solutions:
        print(sol)


if __name__ == "__main__":
    main()
