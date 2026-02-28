"""Takes inputs from user"""

from input_validation import validate_degree, validate_length, validate_seed, validate_key, validate_amount, validate_dataset

def get_dataset():
    """Takes the user input for dataset, meaning the genre of generation"""
    while True:
        input_dataset = input("Choose genre ('folk' or 'bach'): ")
        try:
            dataset = validate_dataset(input_dataset)
        except ValueError:
            print("Invalid dataset name. Options: 'folk', 'bach'")
            continue
        break
    return dataset

def get_key():
    """Takes the user input for key and returns it if valid"""
    while True:
        input_key = input('Key: ')
        try:
            key = validate_key(input_key)
        except ValueError:
            print("Invalid key")
            continue
        break
    return key

def get_degree():
    """Takes the user input for degree and returns it as integer if valid."""
    while True:
        input_degree = input("Degree: ")
        try:
            degree = validate_degree(input_degree)
        except ValueError:
            print("Invalid degree")
            continue
        break
    return degree

def get_seed():
    """Takes the user input for seed and returns it as list if valid"""
    seed_set = None

    while seed_set is None:
        input_seed_set = input("Do you want to compose the beginnning? y/n: ")
        if input_seed_set == 'y':
            seed_set = True
        elif input_seed_set == 'n':
            seed_set = False

    seed = []
    if seed_set:
        while len(seed) == 0:
            input_seed = input(f"Give your notes in the form (note1 note2). Include sharps and flats only for notes outside of the key: ")
            try:
                seed = validate_seed(input_seed)
            except ValueError:
                print("Invalid seed. Seed format: (note1 note2 note3)")
                continue
    return seed

def get_length(seed_length):
    """Takes the user input for length and returns it as integer if valid"""
    while True:
        input_length = input("How long should the generated melody be?: ")
        try:
            length = validate_length(input_length, seed_length)
        except ValueError:
            print("Invalid length")
            continue
        break
    length -= seed_length
    return length

def get_amount():
    """Takes the user input for how many songs to be generated"""
    while True:
        input_amount = input("How many songs do you want to generate?: ")
        try:
            amount = validate_amount(input_amount)
        except ValueError:
            print("Invalid song amount")
            continue
        break
    return amount
