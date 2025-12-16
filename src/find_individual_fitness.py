def find_individual_fitness(solution, population):
    fitness = []

    for i in population:
        for j in enumerate(i):
            if j in enumerate(solution):
                fitness += [1]
    return fitness