import random

def select_first_parents(fitness, population):
    weights = []
    for individual_fitness in fitness:
        weights.append(individual_fitness[1])
    parents = random.choices(population, weights=weights, k=20)
    return parents
