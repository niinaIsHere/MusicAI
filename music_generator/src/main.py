import data, input, trainer, generator

def main():
    filtered_data = data.filter('melodies/ireland.txt')
    parsed_data = data.parse('melodies/gdata.txt')

    # take inputs
    degree = input.get_degree()
    seed = input.get_seed(degree)
    length = input.get_length(len(seed))

    trained_trie = trainer.train(parsed_data, degree)

    generated_melody = generator.generate(trained_trie, seed, length)
    print(generated_melody)

if __name__ == main():
    main()
