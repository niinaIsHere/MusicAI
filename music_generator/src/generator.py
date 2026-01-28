import trie, random

def generate(trained_trie, seed, length):
    generated_melody = [note for note in seed]
    # generation
    for i in range(length):
        result = trained_trie.find(trained_trie.root, seed)
        if result == None:
            print('Nothing like this has ever existed')
            break
        candidates, frequencies = result
        chosen = random.choices(candidates, frequencies)[0]
        generated_melody.append(chosen)
        seed.append(chosen)
        if len(seed) > trained_trie.degree:
            seed.pop(0)
    return generated_melody
