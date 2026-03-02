"""Validates all user inputs from user_input.py."""

VALID_NOTES = ({'a', 'b', 'c', 'd', 'e', 'f', 'g'})
VALID_KEYS = ({'C', 'Cm', 'D', 'Dm', 'E', 'Em', 'F', 'Fm', 'G', 'Gm', 'A', 'Am', 'B', 'Bm', 'Ador', 'Ddor'})
VALID_DATASETS = ({'folk', 'bach'})

def validate_dataset(dataset):
    """Checks the dataset choice is valid"""
    if dataset in VALID_DATASETS:
        return dataset
    raise ValueError

def validate_key(key):
    """Checks if input key is in the set of valid keys and returns it if is,
    else returns ValueError.
    """
    if key in VALID_KEYS:
        return key
    raise ValueError

def validate_degree(input_degree):
    """Takes the user input degree as parameter and checks whether it's valid.
    If the degree is valid it's returned as an integer, if it's not valid a value error is raised.
    """
    if not input_degree.isnumeric():
        raise ValueError
    degree = int(input_degree)
    if degree < 0:
        raise ValueError
    return degree

def validate_seed(input_seed):
    """Takes the user input seed and degree as parameter. Checks whether the seed is valid.
    If the seed is valid it's returned as a list of notes. If it's not valid raises value error.
    """
    seed = input_seed.split()
    for note in seed:
        if len(note) == 1:
            if note.lower() not in VALID_NOTES:
                raise ValueError
        elif len(note) == 2 or len(note) == 3:
            if note[0].lower() in VALID_NOTES:
                if note[1] != "'":
                    raise ValueError
            else:
                if note[1].lower() in VALID_NOTES:
                    if note[0] != '^' and note[0] != '_':
                        raise ValueError
                    if len(note) == 3:
                        if note[2] != "'":
                            raise ValueError
                else:
                    raise ValueError
        else:
            raise ValueError
    return seed

def validate_length(input_length, seed_length):
    """Validates user's chosen melody length. Takes the length and the seed length as parameter.
    If the length is valid it gets returned as an interger. If not valid it raises value error.
    """
    if not input_length.isnumeric():
        raise ValueError
    length = int(input_length)
    if length < seed_length:
        raise ValueError
    if length < 0:
        raise ValueError
    return length

def validate_amount(amount):
    """Checks the input amount is an integer and larger than 0"""
    try:
        amount = int(amount)
    except:
        raise ValueError
    if amount < 1 or amount > 100:
        raise ValueError
    return amount

def validate_output_choice(choice, length):
    """Validates the user choice for melodies to be written into output.txt.
    If invalid choice, raises value error.
    """
    if choice == 'all':
        return list(range(length))
    if choice == '0':
        return None
    
    numbers = choice.split()
    takeout = []
    for num in numbers:
        try:
            value = int(num)
            if value < 1:
                raise ValueError
            if value > length:
                raise ValueError
            takeout.append(value-1)
        except:
            raise ValueError
    return takeout
