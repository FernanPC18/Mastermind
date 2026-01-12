from random import choices
from src.constants import COLOR_LIST

def generate_solution():
    color_numbers = choices(range(0, 6), k=4)  # Genera 4 números aleatorios del 0 al 5
    solution = []

    for i, number in enumerate(color_numbers):
        solution.append(COLOR_LIST[color_numbers[i]])
    return solution
