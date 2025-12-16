def find_individual_fitness(solution, population):
    fitness = {}
    puntuation = 0

    for posicion, i in enumerate(population):
        for j in enumerate(i):
            j_position = j[0]
            if j[1] == solution[j_position] or (j in solution):
                puntuation += 1
            else:
                puntuation -= 1
        fitness[posicion + 1] = puntuation
        
    return fitness