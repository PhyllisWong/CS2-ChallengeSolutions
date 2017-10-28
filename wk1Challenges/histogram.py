import sys, string, re


def clean_source_txt(raw_data):
    # Removes punctuation from text
    no_punc = ''.join([char for char in raw_data if char not in
                       string.punctuation])
    # Splits text based on match zero or more of ANY whitespace character (SPACE, TAB, FORMFEED, etc.)
    clean_data = re.split('\s*', no_punc)[:-1]
    print(clean_data)


def histogram():
    '''
    function which takes a source_text argument (can be either a filename or the contents of the file as a string, your choice) and return a histogram data structure that stores each unique word along with the number of times the word appears in the source text
    '''
    pass


def unique_words():
    '''
    function that takes a histogram argument and returns the total count of unique words in the histogram. For example, when given the histogram for The Adventures of Sherlock Holmes, it returns the integer 8475
    '''
    pass


def frequency():
    '''
    function that takes a word and histogram argument and returns the number of times that word appears in a text. For example, when given the word "mystery" and the Holmes histogram, it will return the integer 20
    '''
    pass


def main():
    '''Read the source text, perform the clean_data function.'''
    with open("alice-in-wonderland.txt", "r") as f:
        raw_data = f.read()
        clean_source_txt(raw_data)


if __name__ == '__main__':
    # print(__name__)
    main()
