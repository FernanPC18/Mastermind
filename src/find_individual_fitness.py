def find_individual_fitness(solution, population):
    fitness = {}

    for individual_number, individual in enumerate(population):
        puntuation = 0
        for gene_allele_individual in enumerate(individual):
            gene_individual = gene_allele_individual[0]
            if gene_allele_individual[1] == solution[gene_individual]:
                puntuation += 1
            elif gene_allele_individual[1] in set(solution):
                puntuation += 1
            else:
                puntuation -= 1
        fitness[individual_number + 1] = puntuation
        
    return fitness