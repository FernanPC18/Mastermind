from src.generate_solution import generate_solution
from src.generate_first_population import generate_first_population
from src.find_individual_fitness import find_individual_fitness

def main():

    solution = generate_solution()
    population = generate_first_population()
    find_individual_fitness(solution, population)

if __name__ == "__main__":
    main()
