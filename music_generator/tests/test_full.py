import pytest, copy
import src.data as data, src.trie as trie, src.trainer as trainer, src.generator as generator

KEY = 'G'
DEGREE = 3
INPUT_SEED = ['c']
INPUT_LENGTH = 5
test_data = "testdata/full_test_data.txt"
filtered_data = "melodies/gdata.txt"

def test_pipeline():
    """Tests whole pipeline from data parsing to training to generation.
    Uses a small training dataset and trains trie with it. Generates a melody
    and tests that it has the correct length, beginning and valid transitions.
    """
    length = INPUT_LENGTH-len(INPUT_SEED)
    seed = copy.deepcopy(INPUT_SEED)
    songs_in_key = data.filter(test_data, KEY)
    melodies = data.parse(filtered_data)
    test_trie = trainer.train(melodies, DEGREE)
    gen = generator.generate(test_trie, seed, length, KEY)

    assert len(gen) == INPUT_LENGTH
    assert gen[:len(INPUT_SEED)] == INPUT_SEED

    for i in range(len(gen)-DEGREE):
        n_gram_start = gen[i:i+DEGREE]
        to_be_found = gen[i+DEGREE]
        followers = test_trie.find(n_gram_start)[0]
        assert to_be_found in followers
