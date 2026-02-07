import pytest
from src.generator import generate
from src.trie import Trie

TEST_SET = set({'c', 'd', 'e'})

def construct_test_trie():
    trie = Trie(2)
    trie.insert(['c', 'd', 'e'])
    trie.insert(['d', 'e', 'c'])
    trie.insert(['e', 'c', 'd'])
    return trie

def test_generated_melody_starts_with_seed():
    trie = construct_test_trie()
    seed = ['c', 'd']
    song = generate(trie, seed, 3)
    assert song[:2] == ['c', 'd']

def test_generator_without_seed():
    trie = construct_test_trie()
    seed = []
    song = generate(trie, seed, 3)
    assert len(song) == 3

def test_generated_melody_length():
    trie = construct_test_trie()
    seed = []
    song = generate(trie, seed, 10)
    assert len(song) == 10

def test_generated_notes_are_in_trie():
    trie = construct_test_trie()
    seed = []
    song = generate(trie, seed, 5)
    valid_notes = True
    for note in song:
        if note not in TEST_SET:
            valid_notes = False
    assert valid_notes

def test_transitions_are_allowed():
    trie = construct_test_trie()
    seed = ['c']
    song1 = generate(trie, seed, 3)
    seed = ['d']
    song2 = generate(trie, seed, 3)
    assert song1 != song2
