import pytest
from src.constants import COLOR_LIST
from src.generate_solution import generate_solution


@pytest.mark.solution
def test_solution_length():
    solution = generate_solution()
    assert len(solution) == 4


@pytest.mark.solution
def test_solution_colors_valid():
    solution = generate_solution()
    for color in solution:
        assert color in COLOR_LIST
