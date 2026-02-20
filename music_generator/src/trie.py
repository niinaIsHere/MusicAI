"""
Methods for creating a node into the trie, inserting a melody into the trie and finding possible followers for input from the trie.
"""

CONVERT_TO_NUMBERS = {
    'C': 2,
    'D': 5,
    'E': 8,
    'F': 9,
    'G': 12,
    'A': 15,
    'B': 18,
    'c': 19,
    'd': 22,
    'e': 25,
    'f': 26,
    'g': 29,
    'a': 32,
    'b': 35,
    "c'": 36,
    "d'": 39,
    "e'": 42,
    "f'": 43,
    "g'": 46,
    "a'": 49,
    "b'": 52
}

CONVERT_TO_NOTES = {
    2: 'C',
    5: 'D',
    8: 'E',
    9: 'F',
    12: 'G',
    15: 'A',
    18: 'B',
    19: 'c',
    22: 'd',
    25: 'e',
    26: 'f',
    29: 'g',
    32: 'a',
    35: 'b',
    36: "c'",
    39: "d'",
    42: "e'",
    43: "f'",
    46: "g'",
    49: "a'",
    52: "b'"
}

SHARP = "^"
FLAT = "_"

class Trie():
    def __init__(self, degree):
        self.root = Node(None)
        self.degree = degree

    def convert_to_numeric(self, key):
        """Converts note sequence into number sequence.
        Takes the note sequence as parameter.
        Returns the sequence as numeric values
        """
        numeric_key = []
        for i in range(len(key)):
            note_value = key[i]
            if SHARP in note_value:
                note_name = note_value[1:]
                numeric_value = CONVERT_TO_NUMBERS[note_name] + 1
            elif FLAT in note_value:
                note_name = note_value[1:]
                numeric_value = CONVERT_TO_NUMBERS[note_name] - 1
            else:
                numeric_value = CONVERT_TO_NUMBERS[note_value]
            numeric_key.append(numeric_value)
        return numeric_key

    def convert_to_notes(self, key):
        """Converts number sequence into note sequence.
        Takes the number sequence as parameter and returns the note sequence.
        """
        note_sequence = []
        for i in range(len(key)):
            if key[i] not in CONVERT_TO_NOTES:
                if (key[i] + 1) in CONVERT_TO_NOTES:
                    note_value = FLAT + CONVERT_TO_NOTES[key[i] + 1]
                elif (key[i] - 1) in CONVERT_TO_NOTES:
                    note_value = SHARP + CONVERT_TO_NOTES[key[i] - 1]
            else:
                note_value = CONVERT_TO_NOTES[key[i]]
            note_sequence.append(note_value)
        return note_sequence

    def insert(self, key):
        """Inserts a melody given as parameter into the trie.
        Doesn't return anything.
        """
        x = self.root
        num_key = self.convert_to_numeric(key)
        for i in range(len(num_key)):
            if x.children[num_key[i]] == None:
                x.children[num_key[i]] = Node(num_key[i])
            x.children[num_key[i]].count += 1
            x = x.children[num_key[i]]

    def find(self, key):
        """Finds a sequence of notes given as parameter from the trie.
        Returns the possible followers and their frequencies as a tuple of two lists.
        """
        x = self.root
        num_key = self.convert_to_numeric(key)
        for i in range(len(num_key)):
            if x.children[num_key[i]] == None:
                return None
            x = x.children[num_key[i]]
        
        candidates = []
        frequencies = []
        max_count = 0
        for child in x.children:
            node = x.children[child]
            if node != None:
                if node.count > max_count:
                    max_count = node.count
                candidates.append(child)
                frequencies.append(node.count)
        candidates = self.convert_to_notes(candidates)
        return (candidates, frequencies)
        

class Node():
    def __init__(self, value):
        self.value = value
        self.children = {i: None for i in range(1, 53)}
        self.count = 0

