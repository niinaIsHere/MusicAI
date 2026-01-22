"""
First prototype of the music generator. Only generates based on one previous note and has probabilities and transitions
stored in dictionaries. Gets the starting note and generated melody length as input.
"""

import random

TRANSITIONS = {}

with open("melodies/melodies.txt") as f:
    data = f.read()

melodies = data.split('\n')
melodies_in_notes = []
for melody in melodies:
    melody = [note for note in melody if note != ' ']
    melodies_in_notes.append(melody)

for melody in melodies_in_notes:
    last_note = None
    for note in melody:
        if last_note:
            if last_note not in TRANSITIONS:
                TRANSITIONS[last_note] = {'total': 0}
            if note not in TRANSITIONS[last_note]:
                TRANSITIONS[last_note][note] = 1
            else:
                TRANSITIONS[last_note][note] += 1
            TRANSITIONS[last_note]['total'] += 1
        last_note = note

PROBABILITIES = {}

for note in TRANSITIONS:
    if note not in PROBABILITIES:
        PROBABILITIES[note] = {}
    for next_note in TRANSITIONS[note]:
        if next_note == 'total':
            continue
        PROBABILITIES[note][next_note] = TRANSITIONS[note][next_note]/TRANSITIONS[note]['total']

seed = input('Give starting note: ')
input_length_of_melody = input('Length of generated melody: ')
length_of_melody = int(input_length_of_melody)

generated_melody = [seed]

for i in range(length_of_melody):
    if seed not in PROBABILITIES:
        print('unknown note')
        break

    notes = list(PROBABILITIES[seed].keys())
    p_list = list(PROBABILITIES[seed].values())
    prediction = random.choices(notes, weights=p_list)
    generated_melody.append(prediction[0])
    seed = prediction[0]

print(generated_melody)
