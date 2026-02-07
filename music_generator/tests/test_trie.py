import pytest
from src.trie import Trie

def test_trie_insert_and_find():
    trie = Trie(2)
    trie.insert(['c', 'd', 'e'])

    result = trie.find(['c', 'd'])
    assert result == (['e'], [1])

def test_trie_nonexistent_returns_none():
    trie = Trie(2)
    trie.insert(['c', 'd', 'e'])
    result = trie.find(['f', 'g'])
    assert result is None

def test_trie_counts():
    trie = Trie(2)
    trie.insert(['c', 'd', 'e'])
    trie.insert(['c', 'd', 'e'])
    trie.insert(['c', 'd', 'f'])
    result = trie.find(['c', 'd'])
    assert result == (['e', 'f'], [2, 1])

def test_trie_conversion():
    trie = Trie(2)
    melody = ['c', 'd', 'e']
    numeric = trie.convert_to_numeric(melody)
    notes = trie.convert_to_notes(numeric)
    assert melody == notes

def test_too_high_degree_search():
    trie = Trie(2)
    result = trie.find(['c', 'd', 'e'])
    assert result is None

