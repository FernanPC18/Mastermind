import pytest
from src.generate_solution import generate_solution, COLOR_LIST


@pytest.mark.solution
def test_solution_length():
    solution = generate_solution()
    assert len(solution) == 4


@pytest.mark.solution
def test_solution_colors_valid():
    solution = generate_solution()
    for color in solution:
        assert color in COLOR_LIST
