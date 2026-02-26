"""Tests for generator.py"""

from src.generator import generate, apply_key
from src.trie import Trie

TEST_SET = set({'c', 'd', 'e'})
KEY = 'G'
DEGREE = 3

def construct_test_trie():
    """Construct trie to be used in generation tests"""
    trie = Trie()
    trie.insert(['c', 'd', 'e', 'c'])
    trie.insert(['d', 'e', 'c', 'd'])
    trie.insert(['e', 'c', 'd', 'e'])
    return trie

def test_end_to_end():
    """Tests all generated transitions are valid."""
    trie = construct_test_trie()
    seed = []
    length = 6
    song = generate(trie, seed, length, KEY, DEGREE)

    for i in range(len(song)-DEGREE):
        to_be_found = song[i:i+DEGREE]
        followers = trie.find(to_be_found)[0]
        assert song[i+DEGREE] in followers

def test_generated_melody_starts_with_seed():
    """Defines a seed and generates with it.
    Checks that the generated melody starts with the given seed."""
    trie = construct_test_trie()
    seed = ['c', 'd']
    length = 3
    song = generate(trie, seed, length, KEY, DEGREE)
    assert song[:2] == ['c', 'd']

def test_generator_without_seed():
    """Tests the generation works without an input seed"""
    trie = construct_test_trie()
    seed = []
    length = 3
    song = generate(trie, seed, length, KEY, DEGREE)
    assert len(song) == 3

def test_seed_longer_than_degree():
    """Tests the generation works with a seed that's longer than the degree"""
    trie = construct_test_trie()
    seed = ['c', 'd', 'e', 'c', 'd', 'e']
    length = 10
    song = generate(trie, seed, length, KEY, DEGREE)
    assert song[:len(seed)] == seed

def test_generated_melody_length():
    """Tests the generated melody length is the same as the length
    given as parameter"""
    trie = construct_test_trie()
    seed = []
    length = 10
    song = generate(trie, seed, length, KEY, DEGREE)
    assert len(song) == length

def test_apply_key_sharp():
    """Tests the apply_key method successfully corrects the sharp notes"""
    key = 'A'
    melody = ['a', 'c', 'C', 'f', 'd', 'G']
    expected = ['a', '^c', '^C', '^f', 'd', '^G']
    result = apply_key(key, melody)
    assert result == expected

def test_apply_key_flat():
    """Tests the apply_key method successfully corrects the flat notes"""
    key = 'Gm'
    melody = ['g', 'b', 'E', 'd', 'a', 'e']
    expected = ['g', '_b', '_E', 'd', 'a', '_e']
    result = apply_key(key, melody)
    assert result == expected
