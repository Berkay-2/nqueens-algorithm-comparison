"""
N-Queens Solver using Hill Climbing with Timeout
Author: Abdullah Berkay Kürkçü

Note:
Hill Climbing is a local search algorithm that usually finds a solution faster than DFS.
However, for large N or unlucky starting points, it can still take a long time or get stuck.
To avoid system strain, we enforce a 50-minute timeout.
"""

import random
import time
import signal

# Exception class for timeout
class TimeoutException(Exception):
    pass

# Timeout signal handler
def timeout_handler(signum, frame):
    raise TimeoutException

# Connect signal handler
signal.signal(signal.SIGALRM, timeout_handler)

# Calculate number of attacking queen pairs (lower is better)
def fitness(board):
    conflicts = 0
    n = len(board)
    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j] or abs(board[i] - board[j]) == j - i:
                conflicts += 1
    return conflicts

# Hill Climbing algorithm with restart
def solve_nqueens_hill_climbing(n, max_steps=1000):
    board = [random.randint(0, n - 1) for _ in range(n)]  # Start with a random board
    for step in range(max_steps):
        current_fitness = fitness(board)
        if current_fitness == 0:
            return board, step  # Found solution
        neighbors = []
        for row in range(n):
            for col in range(n):
                if board[row] != col:
                    new_board = list(board)
                    new_board[row] = col
                    neighbors.append((fitness(new_board), new_board))
        board = min(neighbors, key=lambda x: x[0])[1]  # Choose best neighbor
    return board, max_steps  # Return even if not solved

# Run algorithm with timeout handling
if __name__ == "__main__":
    for n in [10, 30, 50, 100, 200]:
        print(f"\n--- Running Hill Climbing for N = {n} ---")
        print("⏳ Timeout limit: 50 minutes")  # Displayed limit
        try:
            signal.alarm(30)  
            start = time.time()
            solution, steps = solve_nqueens_hill_climbing(n)
            end = time.time()
            signal.alarm(0)
            print(f"Steps taken: {steps}")
            print(f"Conflicts: {fitness(solution)}")
            print(f"Execution time: {round(end - start, 3)} seconds")
        except TimeoutException:
            print("⏰ Timeout: Hill Climbing exceeded the time limit.")