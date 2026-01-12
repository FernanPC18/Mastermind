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

@pytest.mark.fitness
def test_all_r_solution_and_individual():
    solution = ["R", "R", "R", "R"]
    population = [
        ["R", "R", "R", "R"],
    ]

    fitness = find_individual_fitness(solution, population)

    assert len(fitness) == 1
    assert fitness[0] == 8


@pytest.mark.fitness
def test_no_matches():
    """Sin colores compartidos -> fitness = 4 - 4 = 0"""
    solution = ["R", "G", "B", "Y"]
    population = [["w", "w", "w", "w"]]

    fitness = find_individual_fitness(solution, population)
    assert fitness[0] == 0


@pytest.mark.fitness
def test_color_only_swapped_positions():
    """Colores correctos pero en posiciones intercambiadas"""
    solution = ["R", "G", "B", "Y"]
    population = [["G", "R", "w", "w"]]

    fitness = find_individual_fitness(solution, population)
    # Dos coincidencias de color en distinta posición -> 4 +1 +1 -1 -1 = 4
    assert fitness[0] == 4

@pytest.mark.fitness
def test_multiple_individuals_results():
    """Varios individuos en la población -> comprobar índices y valores"""
    solution = ["R", "G", "B", "Y"]
    population = [
        ["G", "R", "w", "w"],  # 4
        ["R", "B", "G", "w"],  # 6
    ]

    fitness = find_individual_fitness(solution, population)
    assert len(fitness) == 2
    assert fitness[0] == 4
    assert fitness[1] == 6


@pytest.mark.fitness
def test_solution_with_repeated_values():
    """Solución con repeticiones: comprobar que no se puntúe más de una vez la misma instancia"""
    solution = ["R", "R", "B", "Y"]
    population = [["R", "R", "R", "R"]]

    fitness = find_individual_fitness(solution, population)
    # 2 exactos + 2 wrong = 4 +1 +1 -1 -1 = 4
    assert fitness[0] == 4
