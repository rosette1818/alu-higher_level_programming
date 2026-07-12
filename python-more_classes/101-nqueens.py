#!/usr/bin/python3
"""Solves the N queens puzzle.

Prints every possible solution to placing N non-attacking queens on
an N x N chessboard, one solution per line.
"""
import sys


def is_safe(queens, row, col):
    """Check if a queen can be placed at (row, col) without attacks.

    Args:
        queens (list): The columns of queens placed in previous rows.
        row (int): The row to place the new queen in.
        col (int): The column to place the new queen in.

    Returns:
        bool: True if placing the queen is safe, False otherwise.
    """
    for prev_row, prev_col in enumerate(queens):
        if prev_col == col:
            return False
        if abs(prev_col - col) == abs(prev_row - row):
            return False
    return True


def solve(n):
    """Find and print all solutions for placing n queens on an n x n board.

    Args:
        n (int): The size of the board and number of queens.
    """
    queens = []

    def backtrack(row):
        """Recursively try to place a queen in each row."""
        if row == n:
            solution = [[i, queens[i]] for i in range(n)]
            print(solution)
            return
        for col in range(n):
            if is_safe(queens, row, col):
                queens.append(col)
                backtrack(row + 1)
                queens.pop()

    backtrack(0)


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

    solve(N)
