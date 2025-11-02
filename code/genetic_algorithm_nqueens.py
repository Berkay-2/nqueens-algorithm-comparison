"""
N-Queens Solver using Genetic Algorithm
Author: Abdullah Berkay Kürkçü

This Genetic Algorithm maintains a population of boards (chromosomes),
evolves them using selection, crossover, and mutation, and tries to reach a solution
with zero attacking pairs.
"""

import random
import time

# Fitness function: count number of pairs of queens that are attacking each other
def fitness(board):
    n = len(board)
    conflicts = 0
    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j] or abs(board[i] - board[j]) == j - i:
                conflicts += 1
    return conflicts

# Generate a random chromosome (board)
def random_board(n):
    return [random.randint(0, n - 1) for _ in range(n)]

# Crossover between two parent boards
def crossover(parent1, parent2):
    n = len(parent1)
    point = random.randint(0, n - 1)
    child = parent1[:point] + parent2[point:]
    return child

# Mutate a board by changing one position to a new random column
def mutate(board, mutation_rate):
    n = len(board)
    for i in range(n):
        if random.random() < mutation_rate:
            board[i] = random.randint(0, n - 1)
    return board

# Select the best boards from the population
def select(population, scores, num):
    sorted_pop = [board for _, board in sorted(zip(scores, population))]
    return sorted_pop[:num]

# Genetic Algorithm implementation
def solve_nqueens_genetic(n, population_size=100, generations=1000, mutation_rate=0.03):
    population = [random_board(n) for _ in range(population_size)]
    for generation in range(generations):
        scores = [fitness(board) for board in population]
        if 0 in scores:
            best = population[scores.index(0)]
            return best, generation

        selected = select(population, scores, population_size // 2)
        children = []

        while len(children) < population_size:
            p1, p2 = random.sample(selected, 2)
            child = crossover(p1, p2)
            child = mutate(child, mutation_rate)
            children.append(child)

        population = children

    # Return best attempt if perfect solution not found
    best = min(population, key=fitness)
    return best, generations

if __name__ == "__main__":
    # Run for each N value
    for n in [10, 30, 50, 100, 200]:
        print(f"\n--- Running Genetic Algorithm for N = {n} ---")
        start = time.time()
        solution, generation = solve_nqueens_genetic(n)
        end = time.time()
        print(f"Generations: {generation}")
        print(f"Conflicts: {fitness(solution)}")
        print(f"Execution time: {round(end - start, 3)} seconds")