import trie, random

SHARP = '^'
FLAT = '_'

TRANSPOSITION = {
    'D': {'f': SHARP,
          'c': SHARP},
    'Dm': {'b': FLAT},
    'E': {'f': SHARP,
          'c': SHARP,
          'g': SHARP,
          'd': SHARP},
    'Em': {'f': SHARP},
    'F': {'b': FLAT},
    'Fm': {'b': FLAT,
           'e': FLAT,
           'a': FLAT,
           'd': FLAT},
    'G': {'f': SHARP},
    'Gm': {'b': FLAT,
           'e': FLAT},
    'A': {'f': SHARP,
          'c': SHARP,
          'g': SHARP},
    'B': {'f': SHARP,
          'c': SHARP,
          'g': SHARP,
          'd': SHARP,
          'a': SHARP},
    'Bm': {'f': SHARP,
          'c': SHARP}
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
    corrected = apply_key(key, generated_melody)
    return corrected

def apply_key(key, melody):
    corrected_melody = []
    if key in TRANSPOSITION:
        for note in melody:
            note_name = note[0].lower()
            if note_name in TRANSPOSITION[key]:
                correct_note_name = TRANSPOSITION[key][note_name]+note
            else:
                correct_note_name = note
            corrected_melody.append(correct_note_name)
        return corrected_melody
    return melody
