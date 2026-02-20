import trie

def train(data, degree):
    """Feeds the data into the trie and build n-grams of the given degree.
    Parameters are the data to be inserted and the degree of the trie.
    Returns the trained trie."""
    new_trie = trie.Trie(degree)
    for melody in data:
        for i in range(len(melody)-degree):
            sublist = melody[i:(i+(degree+1))]
            new_trie.insert(sublist)
    return new_trie

