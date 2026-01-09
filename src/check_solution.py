# esta función termina el programa si se encuentra la soluión exacta, si no, "intentará" usar como solución el individuo con mejor fitness
def check_solution(solution, population, fitness):
    max_fitness = max(fitness.values())
    for i, individual in enumerate(population):
        if individual == solution:
            return print("final solution found")
    # si no se encuentra la solución exacta, se intenta usar el individuo con mejor fitness como solución
        else:
            if fitness[i] == max_fitness:
                return individual