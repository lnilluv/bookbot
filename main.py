from stats import get_num_words
from stats import count_characters
from stats import pretty_print
import sys


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    filepath = 'books/frankenstein.txt'
    text = get_book_text(filepath)
    words = get_num_words(text)
    dict = count_characters(words)
    pretty_print(dict, filepath)

main()

