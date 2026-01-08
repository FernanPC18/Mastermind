from src.generate_solution import generate_solution
from src.generate_first_population import generate_first_population
from src.find_individual_fitness import find_individual_fitness

from src.select_first_parents import select_first_parents

from src.create_offspring import create_first_offspring
from src.create_offspring import create_new_population
from src.create_offspring import mutation

from src.check_solution import check_solution


def main():
    solution = generate_solution()
    population = generate_first_population()

    fitness = find_individual_fitness(solution, population)
    parents = select_first_parents(fitness, population)

    select_first_parents(fitness, population)

    create_first_offspring(parents, population, solution)

    old_fitness = find_individual_fitness(solution, population)

    create_new_population(population, old_fitness, solution)

    mutation(population)

    check_solution(solution, population, fitness)


if __name__ == "__main__":
    main()