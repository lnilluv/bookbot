from stats import get_num_words
from stats import count_characters
from stats import pretty_print
import sys


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    text = get_book_text(filepath)
    words = get_num_words(text)
    dict = count_characters(words)
    pretty_print(dict, filepath)

main()

