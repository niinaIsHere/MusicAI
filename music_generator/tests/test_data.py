"""Tests for data.py"""

from src.data import prep_file, filter_with_key, parse, write_into_file, clear_output_file

def test_prep_file():
    """Tests the returned list is of accurate size"""
    rows = prep_file('testdata/prep_file_test_data.txt')
    assert len(rows) == 11

def test_filter():
    """Tests the filter successfully filters the songs in the input key"""
    key = 'G'
    expected = ['K:'+key, 'g2| gfe deB|cdd cBA| BF2', '']
    dataset = 'test filter'
    rows = filter_with_key(dataset, key)
    assert rows == expected

def test_parse():
    """Tests the parser parses the file into accurate form"""
    expected = [['_A', "c'", 'B', '^G', 'G', 'B', 'G'], ['B', 'd', 'e', 'g', '_e', 'd', 'c', 'B', 'A', 'G', '^d', 'A', 'B']]
    songs = parse('testdata/parse_test_data.txt')
    assert songs == expected

def test_write_into_file():
    """Tests the write_into_file in data.py writes a melody correctly
    into the output file. Uses file meant for test output.
    """
    melody = ['c', 'd', 'e']
    expected = 'X:1\ncde|]\n\n'
    test_output_file = 'testdata/output_test.txt'
    clear_output_file(file=test_output_file)
    write_into_file(melody, 1, test_output_file)
    with open(test_output_file) as f:
        content = f.read()
    assert content == expected

def test_clear_output_file():
    """Tests the clear_output_file in data.py
    clears the output file.
    """
    writing = 'x'
    expected = ''
    test_output_file = 'testdata/output_test.txt'
    write_into_file(writing, 1, test_output_file)
    clear_output_file(test_output_file)
    with open(test_output_file) as f:
        content = f.read()
    assert content == expected
