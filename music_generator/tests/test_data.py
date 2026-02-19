import pytest
from src.data import prep_file, filter, parse

def test_prep_file():
    rows = prep_file('testdata/prep_file_test_data.txt')
    assert len(rows) == 11

def test_filter():
    key = 'G'
    expected = ['K:'+key, 'g2| gfe deB|cdd cBA| BF2', '']
    rows = filter('testdata/filter_test_data.txt', key)
    assert rows == expected

def test_parse():
    expected = [['_A', "c'", 'B', '^G', 'G', 'B', 'G'], ['B', 'd', 'e', 'g', '_e', 'd', 'c', 'B', 'A', 'G', '^d', 'A', 'B']]
    songs = parse('testdata/parse_test_data.txt')
    assert songs == expected

