"""
N-Queens Solver using Simulated Annealing Algorithm
Author: Abdullah Berkay Kürkçü

Simulated Annealing is a probabilistic optimization algorithm that sometimes accepts worse solutions
to escape local minima. It mimics the process of annealing in metallurgy.
"""

import random
import math
import time

# Function to calculate number of conflicting queen pairs
def fitness(board):
    conflicts = 0
    n = len(board)
    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j] or abs(board[i] - board[j]) == j - i:
                conflicts += 1
    return conflicts

# Generate a neighbor by changing one row's queen to a new random column
def random_neighbor(board):
    n = len(board)
    new_board = list(board)
    row = random.randint(0, n - 1)
    new_col = random.randint(0, n - 1)
    new_board[row] = new_col
    return new_board

# Simulated Annealing implementation
def solve_nqueens_simulated_annealing(n, initial_temp=1000, cooling_rate=0.95, max_steps=10000):
    board = [random.randint(0, n - 1) for _ in range(n)]
    temp = initial_temp

    for step in range(max_steps):
        current_fitness = fitness(board)
        if current_fitness == 0:
            return board, step
        neighbor = random_neighbor(board)
        delta = fitness(neighbor) - current_fitness

        # Accept if better or with certain probability if worse
        if delta < 0 or random.random() < math.exp(-delta / temp):
            board = neighbor

        temp *= cooling_rate
        if temp < 1e-10:
            break

    return board, step

if __name__ == "__main__":
    # Run for each N value
    for n in [10, 30, 50, 100, 200]:
        print(f"\n--- Running Simulated Annealing for N = {n} ---")
        start = time.time()
        solution, steps = solve_nqueens_simulated_annealing(n)
        end = time.time()
        print(f"Steps taken: {steps}")
        print(f"Conflicts: {fitness(solution)}")
        print(f"Execution time: {round(end - start, 3)} seconds")