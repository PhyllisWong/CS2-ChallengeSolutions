import sys, string, re, time
from operator import itemgetter


def clean_source_txt(raw_txt):
    '''Take a txt file as an argument, return a list of individual words.'''
    # Removes punctuation from text, returns a string
    no_punc = ''.join([char.lower() for char in raw_txt if char not in string.punctuation])
    # cleans all new lines and special chars from string, returns a list
    clean_txt = re.split('\s*\W+', no_punc)[:-1]
    return clean_txt


def histogram_dict(text_list):
    '''Take a source_text argument string, return a histogram data structure.
    Store each unique word as the key and frequency of the word as value.'''
    alice_dict = {}
    get = alice_dict.get
    for word in text_list:
        alice_dict[word] = get(word, 0) + 1
    return alice_dict


def histogram_list(txt_list):
    # Refactor using list comprehension
    '''Store each unique word and frequency of the word as a list of lists.'''
    word_freq = [[w, txt_list.count(w)] for w in txt_list]
    print(word_freq)
    return word_freq


def histogram_list_tuples(txt_list):
    # Refactor using list comprehension
    '''Store each unique word and frequency of the word as a list of lists.'''
    word_freq = [(w, txt_list.count(w)) for w in txt_list]
    sorted_lst = sorted(word_freq, key=itemgetter(1))
    print(sorted_lst)


def unique_words(alice_dict):
    '''Take a histogram argument and return the total count of unique words.
    Example: when given the histogram for The Adventures of Sherlock Holmes,
    returns the integer 8475.'''
    num_of_keys = len(alice_dict.keys())
    print(num_of_keys)


def frequency(alice_dict, word):
    '''Take a word and a histogram as arguments and return the number of times
    the word appears. Ex: given the word "mystery" and the Holmes histogram,
    returns the integer 20.'''
    # print(alice_dict[word])
    return alice_dict[word]


def main():
    '''
    Read the source text, run the helper functions.
    perform the clean_data function.
    '''
    time1 = time.time()
    print(time.time())

    with open("alice-in-wonderland.txt", "rt") as f:
        raw_txt = f.readlines()
        f.close()
    text_list = clean_source_txt(raw_txt)
    # alice_dict = histogram_dict(text_list)
    # print(alice_dict)
    # unique_words(alice_dict)
    # frequency(alice_dict, "alice")
    # histogram_list(text_list)
    histogram_list_tuples(text_list)
    time2 = time.time()
    print(time1-time2)


if __name__ == '__main__':
    main()
