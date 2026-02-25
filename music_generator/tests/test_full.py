"""Tests whole program action"""

import copy
from src import data, trainer, generator

KEY = 'G'
DEGREE = 3
INPUT_SEED = ['c']
INPUT_LENGTH = 5
TEST_DATA = "testdata/full_test_data.txt"
FILTERED_DATA = "melodies/gdata.txt"

def test_pipeline():
    """Tests whole pipeline from data parsing to training to generation.
    Uses a small training dataset and trains trie with it. Generates a melody
    and tests that it has the correct length, beginning and valid transitions.
    """
    length = INPUT_LENGTH-len(INPUT_SEED)
    seed = copy.deepcopy(INPUT_SEED)
    songs_in_key = data.filter_with_key(TEST_DATA, KEY)
    melodies = data.parse(FILTERED_DATA)
    test_trie = trainer.train(melodies, DEGREE)
    gen = generator.generate(test_trie, seed, length, KEY)

    assert len(gen) == INPUT_LENGTH
    assert gen[:len(INPUT_SEED)] == INPUT_SEED

    for i in range(len(gen)-DEGREE):
        n_gram_start = gen[i:i+DEGREE]
        to_be_found = gen[i+DEGREE]
        followers = test_trie.find(n_gram_start)[0]
        assert to_be_found in followers
