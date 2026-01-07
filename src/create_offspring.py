import random
from src.find_individual_fitness import find_individual_fitness
from src.generate_solution import generate_solution
def create_first_offspring(parents, population, solution):
    offsprings = []
    # Emparejar padres (0 con 1, 2 con 3, etc.)
    for selected_parents in range(0, len(parents), 2):
        if selected_parents + 1 < len(parents):
            parent1 = parents[selected_parents]
            parent2 = parents[selected_parents + 1]
            
            # Mitades de cada padre
            parent1_left_half = parent1[:2]
            parent1_right_half = parent1[2:]
            parent2_left_half = parent2[:2]
            parent2_right_half = parent2[2:]

            # Crear descendientes combinando mitades
            offspring1 = parent1_left_half + parent2_right_half  # izquierda de parent1 + derecha de parent2
            offspring2 = parent2_left_half + parent1_right_half  # izquierda de parent2 + derecha de parent1
            
            population.append(offspring1)
            population.append(offspring2)

    # Calcular new_fitness para la población actualizada
        new_fitness = find_individual_fitness(solution, population)

    return population, new_fitness

def create_new_population(population, new_fitness):
    new_population = []
    for veces in range(80):
        individuals_added = random.choices(population, weights = new_fitness.values(),k=1)
        for i, j in enumerate(individuals_added):
            new_population.append(j)

    return new_population