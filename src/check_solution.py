import sys

# esta función termina el programa si se encuentra la solución exacta, si no, intenta usar como solución el individuo con mejor fitness
def check_solution(solution, new_population, new_fitness):
    max_fitness = max(new_fitness.values())

    # si se encuentra la solución exacta, terminar el programa
    for i, individual in enumerate(new_population):
        if individual == solution:
            print(individual, "solution found", solution)
            sys.exit(0) # terminar el programa

    # si no se encuentra la solución exacta, se intenta usar el individuo con mejor fitness como solución
    for i, individual in enumerate(new_population):
        if new_fitness[i] == max_fitness:
            print(individual, "best attempt used as solution")
            return individual
