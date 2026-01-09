from src.mutation import mutation
import pytest

@pytest.mark.mutation
def check_mutation():
    offspring =  [["R", "G", "B", "Y"],["R", "G", "B", "Y"],["R", "G", "B", "Y"]]
    original_offspring = [["R", "G", "B", "Y"],["R", "G", "B", "Y"],["R", "G", "B", "Y"]]
    mutation(offspring)
    assert offspring != original_offspring