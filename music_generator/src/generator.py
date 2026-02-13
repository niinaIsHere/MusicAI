import trie, random

TRANSPOSITION = {
    'C': {},
    'D': {'f': '^f', 'g': '^g'},
    'Dm': {'e': '_e'},
    'E': {},
    'Em': {},
    'F': {},
    'Fm': {},
    'G': {},
    'Gm': {},
    'A': {},
    'Am': {},
    'B': {},
    'Bm': {}
}

def generate(trained_trie, seed, length, key):
    generated_melody = [note for note in seed]
    # generation
    for i in range(length):
        result = trained_trie.find(seed)
        if result == None:
            print('Nothing like this has ever existed')
            break
        candidates, frequencies = result
        if i == 0 and len(candidates) == 0:
            print('Try another key')
            break
        chosen = random.choices(candidates, frequencies)[0]
        generated_melody.append(chosen)
        seed.append(chosen)
        if len(seed) > trained_trie.degree:
            seed.pop(0)
    return generated_melody

def apply_key(key):
    pass
