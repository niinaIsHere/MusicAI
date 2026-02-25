import data, user_input, trainer, generator

def main():
    key = user_input.get_key()
    filtered_data = data.filter_with_key('melodies/ireland.txt', key)
    parsed_data = data.parse('melodies/gdata.txt')

    degree = user_input.get_degree()
    seed = user_input.get_seed(degree)
    length = user_input.get_length(len(seed))

    trained_trie = trainer.train(parsed_data, degree)
    generated_melody = generator.generate(trained_trie, seed, length, key)
    print(generated_melody)

if __name__ == main():
    main()
