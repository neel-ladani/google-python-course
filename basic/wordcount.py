import sys

def read_file_and_count_words(filename):
    """Reads a file and returns a word/count dictionary."""
    word_count = {}
    with open(filename, 'r') as file:
        for line in file:
            words = line.lower().split()
            for word in words:
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1
    return word_count

def print_words(filename):
    """Prints words and their counts from the file, sorted by word."""
    word_count = read_file_and_count_words(filename)
    for word in sorted(word_count.keys()):
        print(f"{word} {word_count[word]}")

def print_top(filename):
    """Prints the top 20 most common words from the file."""
    word_count = read_file_and_count_words(filename)
    sorted_words = sorted(word_count.items(), key=lambda item: item[1], reverse=True)
    for word, count in sorted_words[:20]:
        print(f"{word} {count}")

def main():
    if len(sys.argv) != 3:
        print('Usage: ./wordcount.py {--count | --topcount} file')
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print('Unknown option:', option)
        sys.exit(1)

if __name__ == '__main__':
    main()
