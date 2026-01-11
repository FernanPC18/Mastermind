def find_individual_fitness(solution, population):
    fitness = {}

    # * Individual_number es el indice de cada individuo e individual es cada individuo
    for individual_number, individual in enumerate(population):
        # fitness_score es la puntuación que tendrá cada individuo
        fitness_score = 4
        # Trabajar sobre copias para poder marcar genes ya contados
        individual_copy = list(individual)
        solution_copy = list(solution)

        # Iterar sólo hasta la longitud mínima para evitar 'individual out of range'
        for gene_individual in range(min(len(individual_copy), len(solution_copy))):
            allele = individual_copy[gene_individual]

            # si ya fue marcado como None (por seguridad), saltar
            if allele is None:
                continue

            # Coincidencia exacta (misma posición)
            if allele == solution_copy[gene_individual]:
                fitness_score += 1
                individual_copy[gene_individual] = None
                solution_copy[gene_individual] = None

            # Coincidencia de color en otra posición
            elif allele in solution_copy:
                match_individual = solution_copy.index(allele)
                fitness_score += 1
                individual_copy[gene_individual] = None
                solution_copy[match_individual] = None

            # No hay coincidencia
            else:
                fitness_score -= 1
                individual_copy[gene_individual] = None

        fitness[individual_number] = fitness_score

    return fitness
