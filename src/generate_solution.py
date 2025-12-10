from random import choices

color_list = ['R', 'G', 'B', 'Y', 'P', 'W'] # Lista de todos los colores posibles a  usar en el juego


color_numbers = choices(range(0, 6), k=4)  # Genera 4 números aleatorios del 0 al 5
solution = []

for i, number in enumerate(color_numbers):
    solution.append(color_list[color_numbers[i]])