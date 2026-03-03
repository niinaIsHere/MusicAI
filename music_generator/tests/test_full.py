"""Tests whole program action"""

import copy
from src import data, trainer, generator

KEY = 'C'
DEGREE = 3
INPUT_SEED = ['c']
INPUT_LENGTH = 5
FILTERED_DATA = "melodies/gdata.txt"

def check_note(gen, melody, g_i, m_i, limit, count):
    """Checks if a sequence exists in data. If not returns false,
    if does returns true."""
    if melody[m_i] == gen[g_i]:
        g_i += 1
        m_i += 1
        count += 1
        if count == limit:
            return True
        return check_note(gen, melody, g_i, m_i, limit, count)
    return False

def test_pipeline():
    """Tests whole pipeline from data parsing to training to generation.
    Uses a small training dataset and trains trie with it. Generates a melody
    and tests that it has the correct length, beginning and valid transitions.
    """
    dataset = 'test full'
    length = INPUT_LENGTH-len(INPUT_SEED)
    seed = copy.deepcopy(INPUT_SEED)
    songs_in_key = data.filter_with_key(dataset, KEY)
    melodies = data.parse(FILTERED_DATA)
    test_trie = trainer.train(melodies, DEGREE)
    gen = generator.generate(test_trie, seed, length, KEY, DEGREE)

    assert len(gen) == INPUT_LENGTH
    assert gen[:len(INPUT_SEED)] == INPUT_SEED

    for i in range(len(gen)-DEGREE):
        n_gram_start = gen[i:i+DEGREE]
        to_be_found = gen[i+DEGREE]
        followers = test_trie.find(n_gram_start)[0]
        assert to_be_found in followers

def test_pipeline_to_data():
    """Tests whole pipeline from data parsing to training to generation.
    Uses the full training data and trains trie with it. Generates a melody
    and tests it's transitions correspond to the training data.
    """
    dataset = 'folk'
    length = INPUT_LENGTH-len(INPUT_SEED)
    seed = copy.deepcopy(INPUT_SEED)
    songs_in_key = data.filter_with_key(dataset, KEY)
    melodies = data.parse(FILTERED_DATA)
    test_trie = trainer.train(melodies, DEGREE)
    gen = generator.generate(test_trie, seed, length, KEY, DEGREE)

    assert len(gen) == INPUT_LENGTH
    assert gen[:len(INPUT_SEED)] == INPUT_SEED

    for i in range(len(gen)-DEGREE):
        found = False
        melody_index = 0
        for melody in melodies:
            if found:
                break
            for m in range(len(melody)-DEGREE):
                if check_note(gen, melody, i, m, DEGREE+1, 0):
                    found = True
                    break
            melody_index += 1
        assert found
