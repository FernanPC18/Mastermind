from src.generate_solution import COLOR_LIST
import random

def mutation (mutated_individual):
    MUTATED_RATE = 0.1  # 10% de probabilidad de mutación
    if random.random() < MUTATED_RATE:
        gene_index = random.randint(0, 3)  # Seleccionar un gen al azar
        new_allele = random.choice(COLOR_LIST)  # Nuevo alelo
        mutated_individual[gene_index] = new_allele  # Mutar el gen seleccionado
    return mutated_individual