import sys
import string
from collections import Counter


def load_data(filepath):
    with open(filepath) as file_handler:
        return file_handler.read()


def get_most_frequent_words(text):
    transtable = str.maketrans({symb: None for symb in string.punctuation})
    stripped = text.translate(transtable)
    words = (word.lower() for word in stripped.split())
    top = 10
    return Counter(words).most_common(top)


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
        print(get_most_frequent_words(text_from_file))
