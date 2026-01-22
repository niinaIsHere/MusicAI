"""
Generates the final output from user input and the calculated probabilities.
"""

import random

def generate_melody_n_1(seed, length, probabilities):
    # generates a melody with input and probabilities calculated earlier. Generates based on one preceding note.
    generated_melody = [seed]

    for i in range(length):
        if seed not in probabilities:
            print('unknown note')
            break

        notes = list(probabilities[seed].keys())
        p_list = list(probabilities[seed].values())
        prediction = random.choices(notes, weights=p_list)
        generated_melody.append(prediction[0])
        seed = prediction[0]
    return generated_melody
