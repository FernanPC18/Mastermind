def find_individual_fitness(solution, population):
    fitness = {}

    # * Individual_number es el indice de cada individuo e individual es cada individuo
    for individual_number, individual in enumerate(population):
        # fitness_score es la puntuación que tendrá cada individuo
        fitness_score = 4
        individual_copy = individual[:]

        # * gene_allele_individual es el indice y uno de los elementos de individual
        for gene_individual, allele_individual in enumerate(individual_copy):
            individual_copy[gene_individual] = None

            if allele_individual == solution[gene_individual]:
                fitness_score += 1
            elif allele_individual in solution:
                fitness_score += 1
            else:
                fitness_score -= 1

        fitness[individual_number] = fitness_score

    return fitness
