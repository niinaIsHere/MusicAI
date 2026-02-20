import data, input, trainer, generator
import time

def main():
    key = input.get_key()
    filtered_data = data.filter('melodies/ireland.txt', key)
    parsed_data = data.parse('melodies/gdata.txt')

    degree = input.get_degree()
    seed = input.get_seed(degree)
    length = input.get_length(len(seed))

    trained_trie = trainer.train(parsed_data, degree)
    generated_melody = generator.generate(trained_trie, seed, length, key)
    print(generated_melody)

if __name__ == main():
    main()
