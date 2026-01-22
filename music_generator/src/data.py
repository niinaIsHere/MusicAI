"""
Reads and parses data into the current appropriate format.
"""

def read_data(file):
    # reads data given as parameter.
    with open(file) as f:
        return f.read()

def parse_txt_data(data):
    # parses the read data into the appropriate format and returns it.
    melodies = data.split('\n')
    melodies_in_notes = []
    for melody in melodies:
        melody = [note for note in melody if note != ' ']
        melodies_in_notes.append(melody)
    return melodies_in_notes

