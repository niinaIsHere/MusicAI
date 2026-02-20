
VALID_NOTE_NAMES = set({'C', 'D', 'E', 'F', 'G', 'A', 'B', 'c', 'd', 'e' ,'f', 'g', 'a', 'b'})
VALID_HIGHER_OCTAVE_NOTES = set({'c', 'd', 'e', 'f', 'g', 'a', 'b'})
OCTAVE_JUMP = "'"
SHARP = '^'
FLAT = '_'
ACCIDENTALS = set({'^', '_'})
NEW_SONG = 'K:'
CHORD_OR_QUOTE = '"'

def prep_file(file):
    """Preps a file into a list of rows for further use.
    Takes a file of abc-notation songs and returns a list of the rows.
    """
    with open(file, "r", encoding="latin-1", errors="replace") as f:
        data = f.read()

    rows = data.split('\n')
    return rows

def filter(file, key):
    """Filters songs in given key from original dataset into the output file.
    Takes a file with abc-notation songs and the key to filter into the output file and returned output.
    Returns a list with the rows in the output file for testing.
    """
    rows = prep_file(file)

    correct = NEW_SONG+key
    new_song = 'X:'
    found = False
    output = []

    with open('melodies/gdata.txt', 'w') as outfile:
        for row in rows:
            if row == correct:
                found = True
            if new_song in row:
                found = False
            if found:
                outfile.write(row + '\n')
                output.append(row)
    return output

def parse(file):
    """Parses the filtered data into a format that is easily convertable and only holds needed information.
    Takes a file of abc notation songs as input and returns a list of lists. Each list is a melody composed of note names.
    """
    rows = prep_file(file)
    testlist = []

    chord_or_comment = False
    new_note = None
    previous = None
    for row in rows:
        if NEW_SONG in row:
            # start new melody and reset variables
            if previous:
                testlist.append(new_melody)
                previous = None
            new_melody = []
            continue
        for symbol in row:
            # skip over chord notation and possible written comments
            if symbol == CHORD_OR_QUOTE:
                if not chord_or_comment:
                    chord_or_comment = True
                else:
                    chord_or_comment = False
            if chord_or_comment:
                continue
            if symbol in VALID_NOTE_NAMES:
                # build regular notes
                if previous not in ACCIDENTALS:
                    if new_note:
                        new_melody.append(new_note)
                    new_note = symbol
                # build sharp and flat notes
                elif previous == SHARP:
                    new_note = SHARP+symbol
                elif previous == FLAT:
                    new_note = FLAT+symbol
            elif symbol == OCTAVE_JUMP and previous in VALID_HIGHER_OCTAVE_NOTES:
                # build notes in highest octave
                if new_note:
                    new_note += symbol
                    new_melody.append(new_note)
                    new_note = None
            else:
                # add previously built note to list in case of non-tracked symbol
                if new_note:
                    new_melody.append(new_note)
                    new_note = None

            # update variable 'previous'
            previous = symbol
    return testlist
