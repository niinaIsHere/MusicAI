# parsing the filtered data into format that is easily convertable and only holds needed information

VALID_NOTE_NAMES = set({'C', 'D', 'E', 'F', 'G', 'A', 'B', 'c', 'd', 'e' ,'f', 'g', 'a', 'b'})
VALID_HIGHER_OCTAVE_NOTES = set({'c', 'd', 'e', 'f', 'g', 'a', 'b'})
OCTAVE_JUMP = "'"
SHARP = '^'
FLAT = '_'
ACCIDENTALS = set({'^', '_'})
NEW_SONG = 'K:'

testlist = []

with open("gdata.txt", encoding="latin-1") as f:
    file = f.read()

rows = file.split('\n')

new_note = None
previous = None
for row in rows:
    if NEW_SONG in row:
        if previous:
            testlist.append(new_melody)
        new_melody = []
        previous = None
    for symbol in row:
        if symbol in VALID_NOTE_NAMES:
            if previous not in ACCIDENTALS:
                if new_note:
                    new_melody.append(new_note)
                new_note = symbol
            elif previous == SHARP:
                new_note = SHARP+symbol
            elif previous == FLAT:
                new_note = FLAT+symbol
        elif symbol == OCTAVE_JUMP and previous in VALID_HIGHER_OCTAVE_NOTES:
            if new_note:
                new_note += symbol
                new_melody.append(new_note)
                new_note = None
        else:
            if new_note:
                new_melody.append(new_note)
                new_note = None

        previous = symbol

print(testlist)