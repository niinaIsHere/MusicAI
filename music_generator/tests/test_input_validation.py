import pytest
from src.input_validation import validate_degree, validate_length, validate_seed

SEED_LENGTH = 3
DEGREE = 3

def test_valid_degree():
    result = validate_degree('3')
    assert result == 3

def test_invalid_degree_type():
    with pytest.raises(ValueError):
        validate_degree('kolme')
    
def test_invalid_degree_amount():
    with pytest.raises(ValueError):
        validate_degree('-1')

def test_valid_length():
    result = validate_length('5', SEED_LENGTH)
    assert result == 5

def test_invalid_length_type():
    with pytest.raises(ValueError):
        validate_length('viisi', SEED_LENGTH)

def test_invalid_length_amount():
    with pytest.raises(ValueError):
        validate_length('-1', SEED_LENGTH)

def test_length_shorter_than_seed():
    with pytest.raises(ValueError):
        validate_length('2', SEED_LENGTH)

def test_valid_seed():
    degree = 4
    seed = "^c' a _b c'"
    result = validate_seed(seed, degree)
    assert result == ["^c'", 'a', '_b', "c'"]

def test_invalid_seed_note_names():
    seed = "f t a"
    with pytest.raises(ValueError):
        validate_seed(seed, DEGREE)

def test_invalid_seed_length():
    seed = "a b c d"
    with pytest.raises(ValueError):
        validate_seed(seed, DEGREE)

