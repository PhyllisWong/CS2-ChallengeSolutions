import sys, string, re, nltk
from urllib import request


def clean_source_txt(raw_txt):
    '''Takes a txt file as an argument, returns a string with all puncuation
    removed.'''
    # Removes punctuation from text
    no_punc = ''.join([char.lower() for char in raw_txt if char not in string.punctuation])
    # # cleans all new lines and special chars from list
    clean_txt = re.split('\s*\W+', no_punc)[:-1]
    print(clean_txt)

# def source_text_arr(txt_str):
#     '''Takes in a string with no puncuation, returns a list of .'''
#     no_punc = clean_source_txt(txt_str)
#     # Splits text based on ANY whitespace character (SPACE,TAB,FORMFEED,etc.)
#
#     print(clean_data)


def histogram(source_text_str):
    '''Takes a source_text argument string, and returns a histogram data
    structure that stores each unique word as the key, with frequency the word
    appears in the text as the value.'''
    pass


def unique_words():
    '''Takes a histogram argument and returns the total count of unique words
    in the histogram. For example, when given the histogram for The Adventures
    of Sherlock Holmes, returns the integer 8475.'''
    pass


def frequency():
    '''Takes a word and histogram argument and returns the number of times that
    word appears in a text. For example, when given the word "mystery" and the
    Holmes histogram, it will return the integer 20.'''
    pass


def main():
    '''Reads the source text, perform the clean_data function.'''
    with open("alice-in-wonderland.txt", "rt") as f:
        raw_txt = f.readlines()
        f.close()
    clean_source_txt(raw_txt)


if __name__ == '__main__':
    # print(__name__)
    main()
