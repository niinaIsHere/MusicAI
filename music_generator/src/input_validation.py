VALID_NOTES = ({'a', 'b', 'c', 'd', 'e', 'f', 'g'})

def validate_degree(input_degree):
    if not input_degree.isnumeric():
        raise ValueError
    degree = int(input_degree)
    if degree < 0:
        raise ValueError
    return degree

def validate_seed(input_seed, degree):
    seed = input_seed.split()
    if len(seed) > degree:
        raise ValueError
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
    if not input_length.isnumeric():
        raise ValueError
    length = int(input_length)
    if length < seed_length:
        raise ValueError
    if length < 0:
        raise ValueError
    return length
