

def get_degree():
    input_degree = input("Degree: ")
    degree = int(input_degree)
    if degree < 0:
        return "Degree can't be less than 0"
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
            notes = input_seed.split()
            if len(notes) > degree:
                print("Too many notes")
                continue
            seed = [note for note in notes]
    return seed

def get_length(seed_length):
    input_length = input("How long should the generated melody be?: ")
    length = int(input_length)
    length -= seed_length
    return length
