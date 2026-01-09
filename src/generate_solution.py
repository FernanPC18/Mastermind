from random import choices


COLOR_LIST = [
    "R", # Red
    "G", # Green
    "B", # Blue
    "Y", # Yellow
    "P", # Pink
    "W", # White
]  # Lista de todos los colores posibles a  usar en el juego


def generate_solution():
    color_numbers = choices(range(0, 6), k=4)  # Genera 4 números aleatorios del 0 al 5
    solution = []

    for i, number in enumerate(color_numbers):
        solution.append(COLOR_LIST[color_numbers[i]])
    return solution
