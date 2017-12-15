import sys, string, re, time
from operator import itemgetter
import cleanup as c
'''Cleanup has .clean_txt() method that reads a text file, removes all punctuation, and returns a list of individual words.'''

def histogram_dict(text_list):
    '''Take a list argument, return a histogram dictionary structure.
    Store each unique word as the key and frequency of the word as value.'''
    dictogram = {}
    get = dictogram.get
    for word in text_list:
        dictogram[word] = get(word, 0) + 1
    # print(alice_dict)
    return dictogram


def histogram_list(clean_txt):
    # Refactor using list comprehension resulted in duplicates
    # Refactor without using the itemgetter library
    '''Store each unique word and frequency of the word as a list of lists.'''
    word_freq = []
    for word in range(0, len(clean_txt)-1):
        wrd = clean_txt[word]
        freq = clean_txt.count(wrd)
        first_list = [wrd, freq]
        if first_list not in word_freq:
            word_freq.append(first_list)
    # Sort the list by frequency of word
    word_freq = sorted(word_freq, key=itemgetter(1))
    print(word_freq)
    return word_freq


def histogram_list_tuples(txt_list):
    # Refactor using list comprehension
    '''Store each unique word and frequency of the word as a list of tuples.'''
    # word_freq = [(w, txt_list.count(w)) for w in txt_list]
    word_freq = []
    for word in range(0, len(txt_list)-1):
        wrd = txt_list[word]
        freq = txt_list.count(wrd)
        first_tpl = (wrd, freq)
        # prevent adding duplicated item to the list
        if first_tpl not in word_freq:
            word_freq.append(first_tpl)
    return word_freq


def unique_words(alice_dict):
    '''Take a histogram argument and return the total count of unique words.
    Example: when given the histogram for The Adventures of Sherlock Holmes,
    returns the integer 8475.'''
    num_of_keys = len(alice_dict.keys())
    return num_of_keys


def frequency(alice_dict, word):
    '''Take a word and a histogram as arguments and return the number of times
    the word appears. Ex: given the word "mystery" and the Holmes histogram,
    returns the integer 20.'''
    # print(alice_dict[word])
    return alice_dict[word]


def write_to_file(alice_dict):
    with open('histogram_dict.txt', 'w') as f:
        for k, v in alice_dict.items():
            f.write(str(k) + ' : ' + str(v) + '\n\n')


def run_histogram():
    '''
    Read the source text, run the helper functions.
    perform the clean_data function.
    '''
    start_time = time.time()
    print(start_time)
    # Takes in a text file, cleans it, and returns a list of words.
    text_list = c.clean_txt('onefish.txt')
    # print(text_list)
    onefish_dict = histogram_dict(text_list)
    # write_to_file(alice_dict)
    print(onefish_dict)
    print(list(onefish_dict.items()))
    # unique_words(alice_dict)
    # print(frequency(alice_dict, "alice"))
    # histogram_list(text_list)
    # histogram_list_tuples(text_list)
    end_time = time.time()
    print(abs(start_time-end_time))


if __name__ == '__main__':
    run_histogram()
