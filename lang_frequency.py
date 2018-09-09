import sys
import string
import collections


def load_data(filepath):
    with open(filepath) as file_handler:
        return file_handler.read()


def get_most_frequent_words(text):
    words_to_show = 10
    transtable = str.maketrans({symb: None for symb in string.punctuation})
    words = text.translate(transtable).lower().split()
    return collections.Counter(words).most_common(words_to_show)


def print_list(wordlist):
    for word, count in wordlist:
        print('{1:>5} {0}'.format(word, count))
    return None


if __name__ == '__main__':
    try:
        text_from_file = load_data(sys.argv[1])
    except IndexError:
        print('Please specify path to text file')
    except FileNotFoundError:
        print('File not found')
    except ValueError:
        print('Not a valid text file')
    else:
        print_list(get_most_frequent_words(text_from_file))
