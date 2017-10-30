import sys, string, re, nltk
from urllib import request


def clean_source_txt(raw_txt):
    '''Take a txt file as an argument, return a list of individual words.'''
    # Removes punctuation from text, returns a string
    no_punc = ''.join([char.lower() for char in raw_txt if char not in string.punctuation])
    # cleans all new lines and special chars from string, returns a list
    clean_txt = re.split('\s*\W+', no_punc)[:-1]
    return clean_txt
    # print(clean_txt)


# def source_text_arr(txt_str):
#     '''Takes in a string with no puncuation, returns a list of .'''
#     no_punc = clean_source_txt(txt_str)
#     # Splits text based on ANY whitespace character (SPACE,TAB,FORMFEED,etc.)
#
#     print(clean_data)


def histogram(text_list):
    '''Take a source_text argument string, return a histogram data structure.
    Store each unique word as the key and frequency of the word as value.'''
    histogram = {}
    for word in text_list:
        if word not in histogram:
            histogram[word] = 1
        else:
            histogram[word] += 1
    return histogram


def unique_words():
    '''Take a histogram argument and return the total count of unique words.
    Example: when given the histogram for The Adventures of Sherlock Holmes,
    returns the integer 8475.'''
    pass


def frequency():
    '''Take a word and histogram argument and returns the number of times that
    word appears in a text. For example, when given the word "mystery" and the
    Holmes histogram, it will return the integer 20.'''
    pass


def main():
    '''Read the source text, perform the clean_data function.'''
    with open("alice-in-wonderland.txt", "rt") as f:
        raw_txt = f.readlines()
        f.close()
    text_list = clean_source_txt(raw_txt)
    histogram(text_list)


if __name__ == '__main__':
    # print(__name__)
    main()
