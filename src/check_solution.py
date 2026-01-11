# esta función termina el programa si se encuentra la soluión exacta, si no, "intentará" usar como solución el individuo con mejor fitness
def check_solution(solution, new_population, new_fitness):
    max_fitness = max(new_fitness.values())
    for i, individual in enumerate(new_population):
        if individual == solution:
            return print(individual, "solution found", solution)
    # si no se encuentra la solución exacta, se intenta usar el individuo con mejor fitness como solución
        else:
            if new_fitness[i] == max_fitness:
                return individual, print(individual, "best attempt used as solution")