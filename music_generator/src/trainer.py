import trie

def train(data, degree):
    new_trie = trie.Trie(degree)
    for melody in data:
        for i in range(len(melody)-degree):
            sublist = melody[i:(i+(degree+1))]
            new_trie.insert(sublist)
    return new_trie

