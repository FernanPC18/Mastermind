from src.generate_solution import generate_solution
from src.generate_first_population import generate_first_population
from src.find_individual_fitness import find_individual_fitness

from src.select_first_parents import select_first_parents

def main():

    solution = generate_solution()
    population = generate_first_population()
    find_individual_fitness(solution, population)

    fitness = find_individual_fitness(solution, population)
    select_first_parents(fitness, population)

if __name__ == "__main__":
    main()
