import pytest
from src.generator import generate, apply_key
from src.trie import Trie

TEST_SET = set({'c', 'd', 'e'})
KEY = 'G'

def construct_test_trie():
    """Construct trie to be used in generation tests"""
    trie = Trie(2)
    trie.insert(['c', 'd', 'e'])
    trie.insert(['d', 'e', 'c'])
    trie.insert(['e', 'c', 'd'])
    return trie

def test_generated_melody_starts_with_seed():
    trie = construct_test_trie()
    seed = ['c', 'd']
    song = generate(trie, seed, 3, KEY)
    assert song[:2] == ['c', 'd']

def test_generator_without_seed():
    trie = construct_test_trie()
    seed = []
    song = generate(trie, seed, 3, KEY)
    assert len(song) == 3

def test_generated_melody_length():
    trie = construct_test_trie()
    seed = []
    song = generate(trie, seed, 10, KEY)
    assert len(song) == 10

def test_generated_notes_are_in_trie():
    trie = construct_test_trie()
    seed = []
    song = generate(trie, seed, 5, KEY)
    valid_notes = True
    for note in song:
        if note not in TEST_SET:
            valid_notes = False
    assert valid_notes

def test_transitions_are_allowed():
    trie = construct_test_trie()
    seed = ['c']
    song1 = generate(trie, seed, 3, KEY)
    seed = ['d']
    song2 = generate(trie, seed, 3, KEY)
    assert song1 != song2

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
