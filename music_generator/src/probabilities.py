"""
Calculates the needed information for the generation like the transition counts and the probabilities.
"""

def create_transitions_dictionary(melodies_in_notes):
    # Creates the dictionary for the transition counts and counts the transitions from one note to another from the parsed data.
    transitions = {}
    for melody in melodies_in_notes:
        last_note = None
        for note in melody:
            if last_note:
                if last_note not in transitions:
                    transitions[last_note] = {'total': 0}
                if note not in transitions[last_note]:
                    transitions[last_note][note] = 1
                else:
                    transitions[last_note][note] += 1
                transitions[last_note]['total'] += 1
            last_note = note
    return transitions

def create_probabilities_dictionary(transitions):
    """
    Creates the dictionary that stores the probabilities of the next note from a given note
    and calculates the probabilities from the transtions.
    """
    probabilities = {}
    for note in transitions:
        if note not in probabilities:
            probabilities[note] = {}
        for next_note in transitions[note]:
            if next_note == 'total':
                continue
            probabilities[note][next_note] = transitions[note][next_note]/transitions[note]['total']
    return probabilities

def calculate_probabilities(melodies):
    # Calls transition creation and probability creation functions. Called from main.py and gets only the parsed data as parameter.
    transitions = create_transitions_dictionary(melodies)
    probabilities = create_probabilities_dictionary(transitions)
    return probabilities
