import data, user_input, trainer, generator
import copy

def main():
    dataset = user_input.get_dataset()
    key = user_input.get_key()
    filtered_data = data.filter_with_key(dataset, key)
    parsed_data = data.parse('melodies/gdata.txt')

    degree = user_input.get_degree()
    seed = user_input.get_seed()
    length = user_input.get_length(len(seed))
    amount = user_input.get_amount()

    trained_trie = trainer.train(parsed_data, degree)
    melodies = []
    for i in range(amount):
        original_seed = copy.deepcopy(seed)
        generated_melody = generator.generate(trained_trie, original_seed, length, key, degree)
        melodies.append(generated_melody)
    print(melodies)

if __name__ == main():
    main()
