import pytest
from src.find_individual_fitness import find_individual_fitness


@pytest.mark.fitness
def test_fitness_value_not_duplicated():
    """Verifica que un mismo alelo repetido en el individuo no se cuente varias veces
    en el fitness (no debe duplicarse la puntuación por la misma letra en la solución).
    """
    solution = ["R", "G", "B", "Y"]
    population = [["R", "R", "R", "R"],  # solo el primer R debe contar como match exacto
]

    fitness = find_individual_fitness(solution, population)

    # Cálculo esperado: 4 (base) +1 (posición 0 exacta) -1 -1 -1 = 2
    assert fitness[0] == 2
