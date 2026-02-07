from input_validation import validate_degree, validate_length, validate_seed

def get_degree():
    while True:
        input_degree = input("Degree: ")
        try:
            degree = validate_degree(input_degree)
        except:
            continue
        break
    return degree

def get_seed(degree):
    seed_set = None

    while seed_set == None:
        input_seed_set = input("Do you want to compose the beginnning? y/n: ")
        if input_seed_set == 'y':
            seed_set = True
        elif input_seed_set == 'n':
            seed_set = False

    seed = []
    if seed_set:
        while len(seed) == 0:
            input_seed = input(f"Give your notes (maximum of {degree} notes): ")
            try:
                seed = validate_seed(input_seed, degree)
            except:
                continue
    return seed

def get_length(seed_length):
    while True:
        input_length = input("How long should the generated melody be?: ")
        try:
            length = validate_length(input_length, seed_length)
        except:
            continue
        break
    length -= seed_length
    return length
