import random

def select_first_parents(fitness, population):
    parents = random.choices(population, weights = fitness.values(),k=20)
   # Obtener el fitness de cada padre seleccionado
    return parents
