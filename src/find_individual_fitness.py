def find_individual_fitness(solution, population):
    fitness = {}

    for individual_number, individual in enumerate(population):
        puntuation = 0
        for gene_individual in enumerate(individual):
            gene_population = gene_individual[0]
            if gene_individual[1] == solution[gene_population] or (gene_individual in solution):
                puntuation += 1
            else:
                puntuation -= 1
        fitness[individual_number + 1] = puntuation
        
    return fitness