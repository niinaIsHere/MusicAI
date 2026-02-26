"""Tests for input_validation.py"""

import pytest
from src.input_validation import validate_degree, validate_length, validate_seed, validate_key, validate_amount

SEED_LENGTH = 3
DEGREE = 3

def test_valid_key():
    """Tests a valid key gets returned as valid"""
    key = "Am"
    result = validate_key(key)
    assert key == result

def test_invalid_key():
    """Tests an invalid key raises value error"""
    key = "Xm"
    with pytest.raises(ValueError):
        validate_key(key)

def test_valid_degree():
    """Tests a valid degree gets returned as valid"""
    result = validate_degree('3')
    assert result == 3

def test_invalid_degree_type():
    """Tests a degree in invalid format returns value error"""
    with pytest.raises(ValueError):
        validate_degree('kolme')

def test_invalid_degree_amount():
    """Tests an invalid degree amount returns value error"""
    with pytest.raises(ValueError):
        validate_degree('-1')

def test_valid_length():
    """Tests a valid length gets returned as valid"""
    result = validate_length('5', SEED_LENGTH)
    assert result == 5

def test_invalid_length_type():
    """Tests an invalid length format raises value error"""
    with pytest.raises(ValueError):
        validate_length('viisi', SEED_LENGTH)

def test_invalid_length_amount():
    """Tests invalid length amount raises value error"""
    with pytest.raises(ValueError):
        validate_length('-1', SEED_LENGTH)

def test_length_shorter_than_seed():
    """Tests a length that's shorter than the seed
    returns value error"""
    with pytest.raises(ValueError):
        validate_length('2', SEED_LENGTH)

def test_valid_seed():
    """Tests a valid seed gets returned as valid"""
    degree = 4
    seed = "^c' a _b c'"
    result = validate_seed(seed)
    assert result == ["^c'", 'a', '_b', "c'"]

def test_invalid_seed_note_names():
    """Tests an invalid seed raises value error"""
    seed = "f t a"
    with pytest.raises(ValueError):
        validate_seed(seed)

def test_seed_longer_than_degree_passes():
    """Tests a seed that's longer than the degree
    passes validation check"""
    seed = "c d e c d e"
    result = validate_seed(seed)
    assert result == ['c', 'd', 'e', 'c', 'd', 'e']

def test_valid_amount():
    """Tests a valid amount input passes"""
    amount = "3"
    result = validate_amount(amount)
    assert result == int(amount)

def test_amount_not_integer():
    """Checks a non-integer amount doesn't pass"""
    with pytest.raises(ValueError):
        validate_amount('three')    

def test_amount_too_small():
    """Checks an amount less than 1 doesn't pass"""
    with pytest.raises(ValueError):
        validate_amount('0')

def test_amount_too_large():
    """Tests an amount larger than 100 doesn't pass"""
    with pytest.raises(ValueError):
        validate_amount('101')
