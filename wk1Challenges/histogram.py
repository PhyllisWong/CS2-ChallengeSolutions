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
    alice_histogram = {}
    for word in text_list:
        if word not in alice_histogram:
            alice_histogram[word] = 1
        else:
            alice_histogram[word] += 1
    return alice_histogram


def unique_words(alice_dict):
    '''Take a histogram argument and return the total count of unique words.
    Example: when given the histogram for The Adventures of Sherlock Holmes,
    returns the integer 8475.'''
    num_of_keys = len(alice_dict.keys())
    print(num_of_keys)


def frequency(alice_dict, word):
    '''Take a word and histogram argument and returns the number of times that
    word appears in a text. For example, when given the word "mystery" and the
    Holmes histogram, it will return the integer 20.'''
    print(alice_dict[word])
    return alice_dict[word]


def main():
    '''Read the source text, perform the clean_data function.'''
    with open("alice-in-wonderland.txt", "rt") as f:
        raw_txt = f.readlines()
        f.close()
    text_list = clean_source_txt(raw_txt)
    alice_dict = histogram(text_list)
    unique_words(alice_dict)
    frequency(alice_dict, "alice")


if __name__ == '__main__':
    # print(__name__)
    main()
