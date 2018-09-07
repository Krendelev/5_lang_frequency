import sys
import string
from collections import Counter


def load_data(filepath):
    with open(filepath) as file_handler:
        return file_handler.read()


def get_most_frequent_words(text):
    transtable = str.maketrans({s: None for s in string.punctuation})
    stripped = text.translate(transtable)
    words = (w.lower() for w in stripped.split())
    return Counter(words).most_common(10)


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
