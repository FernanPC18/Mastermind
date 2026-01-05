def find_individual_fitness(solution, population):
    fitness = []

    # * Individual_number es el indice de cada individuo e individual es cada individuo
    for individual_number, individual in enumerate(population):
        # fitness_score es la puntuación que tendrá cada individuo
        fitness_score = 4
        individual_copy = individual[:]
        solution_copy = solution[:]

        # * gene_allele_individual es el indice y uno de los elementos de individual

        for gene_individual, allele_individual in enumerate(individual_copy):

            if allele_individual == solution[gene_individual]:
                fitness_score += 1
                individual_copy[gene_individual] = None
                solution_copy[gene_individual] = None

            elif allele_individual in solution:
                fitness_score += 1
                individual_copy[gene_individual] = None
                solution_copy[gene_individual] = None

            else:
                fitness_score -= 1
                individual_copy[gene_individual] = None
                solution_copy[gene_individual] = None


        fitness.append((individual_number, fitness_score))
    
    return fitness
