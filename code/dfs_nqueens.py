"""
N-Queens Solver using Depth-First Search (DFS) with Timeout
Author: Abdullah Berkay Kürkçü

Note:
DFS explores all possible configurations. For large values of N, the number of
possible board states grows exponentially, leading to long processing times.
To prevent overheating and system overload, we set a 50-minute timeout limit
for each run  it tooks more hours.
"""

import time
import signal

# Custom exception to handle timeout events
class TimeoutException(Exception):
    pass

# Function to handle the signal for timeouts
def timeout_handler(signum, frame):
    raise TimeoutException

# Connect the signal handler to alarm
signal.signal(signal.SIGALRM, timeout_handler)

# Function to check if placing a queen at (row, col) is safe
def is_safe(queens, row, col):
    for r in range(row):
        if queens[r] == col or abs(queens[r] - col) == row - r:
            return False
    return True

# DFS algorithm to place queens
def dfs(queens, row, n, solutions):
    if row == n:
        solutions.append(queens[:])
        return
    for col in range(n):
        if is_safe(queens, row, col):
            queens[row] = col
            dfs(queens, row + 1, n, solutions)

# Wrapper function to solve and handle timeout
def solve_nqueens_dfs(n, timeout_seconds=30):
    solutions = []
    queens = [0] * n  # Create an empty board
    print(f"\n--- Running DFS for N = {n} ---")
    print("⏳ Timeout limit: 50 minutes")  # Display message only
    try:
        signal.alarm(timeout_seconds)  # Start timeout timer
        start = time.time()
        dfs(queens, 0, n, solutions)  # Run the DFS algorithm
        end = time.time()
        signal.alarm(0)  # Cancel alarm if finished in time
        print(f"Solutions found: {len(solutions)}")
        print(f"Execution time: {round(end - start, 3)} seconds")
    except TimeoutException:
        print("⏰ Timeout: DFS exceeded the time limit.")  # Message if timeout

# Run the solver for multiple board sizes
if __name__ == "__main__":
    for n in [10, 30, 50, 100, 200]:
        solve_nqueens_dfs(n, timeout_seconds=30)