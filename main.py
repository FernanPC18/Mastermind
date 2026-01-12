from src.generate_solution import generate_solution
from src.generate_first_population import generate_first_population
from src.find_individual_fitness import find_individual_fitness

from src.select_first_parents import select_first_parents

from src.create_offspring import create_first_offspring
from src.create_offspring import create_new_population
from src.create_offspring import mutation

from src.check_solution import check_solution
from src.display_solution_comparison import display_solution_comparison


def main():
    solution = generate_solution()
    population = generate_first_population()

    fitness = find_individual_fitness(solution, population)
    generation = 1

    while generation <= 12:
        # seleccionar padres usando el fitness más reciente
        parents = select_first_parents(fitness, population)

        # crear descendientes y actualizar población
        population, fitness = create_first_offspring(parents, population, solution)

        # generar nueva población basada en la población actual
        old_fitness = find_individual_fitness(solution, population)
        new_population, _ = create_new_population(population, old_fitness, solution)

        # aplicar mutación a cada individuo de la nueva población
        for individual in new_population:
            mutation(individual)

        # reemplazar población por la nueva y recalcular fitness
        population = new_population
        fitness = find_individual_fitness(solution, population)

        display_solution_comparison(generation, individual, solution)
        check_solution(solution, population, fitness, generation)
        generation += 1

if __name__ == "__main__":
    main()