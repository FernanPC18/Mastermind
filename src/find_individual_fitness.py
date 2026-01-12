def find_individual_fitness(solution, population):
    fitness = {}

    # * Individual_number es el indice de cada individuo e individual es cada individuo
    for individual_number, individual in enumerate(population):
        # fitness_score es la puntuación que tendrá cada individuo
        fitness_score = 4
        # Trabajar sobre copias para poder marcar genes ya contados
        individual_copy = list(individual)
        solution_copy = list(solution)

        for gene_individual, allele_individual in enumerate(individual_copy):
            # Si el alelo ya fue marcado como None (ya procesado), saltarlo
            if allele_individual is None:
                continue

            # Comprobación de match exacto en la misma posición (y marcarlo)
            if allele_individual == solution_copy[gene_individual]:
                fitness_score += 1
                individual_copy[gene_individual] = None
                solution_copy[gene_individual] = None

            # No hay coincidencia
            else:
                fitness_score -= 1
                individual_copy[gene_individual] = None

        fitness[individual_number] = fitness_score

    return fitness