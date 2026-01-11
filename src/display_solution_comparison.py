from src.find_individual_fitness import find_individual_fitness

def display_solution_comparison(generation, individual, solution):
    display_comparison = ""
    result_individual = ""
    result_solution = ""
    for i,j in enumerate(individual):
        if j == solution[i]:
            display_comparison += " O "
            result_individual += j
        else:
            display_comparison += " X "
            result_individual += j

    for i, j in enumerate(solution):
        result_solution += j

    # Calcula el fitness individual del individuo mostrado

    individual_fitness = find_individual_fitness(solution, [individual])
    if generation < 10:
        return print(generation, "º", " GENERATION ", result_individual, "->", display_comparison, individual_fitness[0], result_solution)
    else: 
        return print(generation, "º", "GENERATION ", result_individual, "->", display_comparison, individual_fitness[0], result_solution)