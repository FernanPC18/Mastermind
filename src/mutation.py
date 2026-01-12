from src.constants import COLOR_LIST
from src.constants import MUTATED_RATE
import random

def mutation (mutated_individual):
    if random.random() < MUTATED_RATE:
        gene_index = random.randint(0, 3)  # Seleccionar un gen al azar
        new_allele = random.choice(COLOR_LIST)  # Nuevo alelo
        mutated_individual[gene_index] = new_allele  # Mutar el gen seleccionado
    return mutated_individual