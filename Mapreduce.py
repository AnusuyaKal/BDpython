from multiprocessing import Pool
import os


def map_function(file_name):
    word_count = {}
    with open(file_name, 'r') as file:
        for line in file:
            words = line.strip().split()
            for word in words:
                if word not in word_count:
                    word_count[word] = 1
                else:
                    word_count[word] += 1
    return word_count.items()


def reduce_function(mapped_items):
    word_count = {}
    for item in mapped_items:
        word, count = item
        if word not in word_count:
            word_count[word] = count
        else:
            word_count[word] += count
    return word_count.items()


def main():
    input_files = [file for file in os.listdir('Documents/BDpython/example.txt') if file.endswith('.txt')]
    
    # Map phase
    pool = Pool()
    mapped_items = pool.map(map_function, [os.path.join('example.txt', file) for file in input_files])
    pool.close()
    pool.join()
    
    # Flatten mapped items
    mapped_items_flat = [item for sublist in mapped_items for item in sublist]
    
    # Reduce phase
    reduced_items = reduce_function(mapped_items_flat)
    
    # Write output
    with open('exampletxt', 'w') as output_file:
        for word, count in reduced_items:
            output_file.write(f'{word}: {count}\n')


if __name__ == "__main__":
    main()
