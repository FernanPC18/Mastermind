def find_individual_fitness(solution, population):
    fitness = {}
    puntuation = 0

    for i in population:
        for j in enumerate(i):
            j_position = j[0]
            if j[1] == solution[j_position]:
                puntuation += 1
            else:
                puntuation -= 1
    return fitness