import random

def select_first_parents(fitness, population):
    parents = random.choices(population, weights = fitness.values(),k=10)
    return fitness, parents