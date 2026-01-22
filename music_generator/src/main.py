import data, probabilities, generator

DATA_FILE = 'melodies/melodies.txt'

raw = data.read_data(DATA_FILE)
melodies = data.parse_txt_data(raw)

probs = probabilities.calculate_probabilities(melodies)

seed = input('Give starting note: ')
input_length_of_melody = input('Length of generated melody: ')
length_of_melody = int(input_length_of_melody)

generated_melody = generator.generate_melody_n_1(seed, length_of_melody, probs)

print(generated_melody)