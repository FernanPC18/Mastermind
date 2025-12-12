def find_fitness(solution, population):
    fitness = 0
    
    for i in enumerate(population):
        if enumerate(population) == enumerate(solution) or population in solution:
            fitness += 1    
    return fitness