import histogram as h
import cleanup as c
import random, sys, re
import markov as m
from pprint import pprint
from collections import deque
# import sys, string, re, time coming from the histogram file


def create_dict_from_list(clean_list):
    '''Take a clean list, return dictionary structure.
    Each unique ('word', 'second_wrd') stored as key : frequency of the tuple stored as value.'''
    list_of_pairs = []

    for index in range(0, len(clean_list)-1):
        cur = clean_list[index]
        nxt = clean_list[index+1]
        # print("iterator: {}".format(index))
        list_of_pairs.append((cur, nxt))
    dictionary = h.histogram_dict(list_of_pairs)
    # print(dictionary)
    return dictionary


def get_random_wrd(dictionary):
    '''Return a random tuple from a dictionary.'''
    rand_index = random.randint(0, len(dictionary) - 1)
    # Convert dictionary into list of unique words with indecies
    key_list = list(dictionary)
    rand_wrd = key_list[rand_index]
    return rand_wrd


def calculate_probability(dictionary):
    '''Take a random word and a dictionary, return a new dictionary.
    Convert the values from frequencies, to weights.'''
    total_tokens = sum(dictionary.values())
    dict_w_weights = {}

    for (wrd, value) in dictionary.items():
        weight = float(value / total_tokens)
        # Set the value to the weight
        dict_w_weights[wrd] = weight
    del dict_w_weights[('fish', 'STOP')]
    return dict_w_weights


def get_random_tuple_prob(dict_w_weights):
    '''Take a dictionary, select random word based on its probability.'''
    rand_float = random.random()
    probability = 0.0
    for tpl, wrd_weight in dict_w_weights.items():
        probability += wrd_weight
        if rand_float < probability:
            break
    # print(dict_w_weights)
    return tpl


def get_many_rand_wrds(dictionary, num):
    '''Create a dictionary with the random word, and num of times selected.'''
    rand_dict = {}
    while sum(rand_dict.values()) < int(num):
        rand_wrd = get_random_wrd_prob(dictionary)
        if rand_wrd not in rand_dict:
            rand_dict[rand_wrd] = 1
        else:
            rand_dict[rand_wrd] += 1
    return rand_dict


def find_wrd_after_tuple_key(tuple_key, markov_dict):
    # print("USE THIS Tuple: {}\n".format(tuple_key))
    # print("SECOND ORDER markov: {}\n".format(markov_dict))
    histogram = markov_dict.get(tuple_key)
    # print("histogram matching the tuple: {}\n".format(histogram))
    nxt_rand_wrd = get_random_wrd(histogram)
    # print("line 96 {}".format(nxt_rand_wrd))
    return nxt_rand_wrd


def find_word_after_rand_wrd(rand_wrd, markov_dict):
    # locate a histogram within the markov dict by the key
    # once the key is located, access the value(a dict) and return THAT key
    for (types, histogram) in markov_dict.items():
        if types == rand_wrd:
            histogram = markov_dict[types]
            if len(histogram) > 1:
                # for (k, v) in histogram.items():
                nxt_rand_wrd = get_random_wrd(histogram)
                return nxt_rand_wrd
            else:
                for (k, v) in histogram.items():
                    nxt_rand_wrd = k
                    return nxt_rand_wrd


def create_sentence(wrd_num, dict_w_weights, markov_dict):
    '''Create a sentence using stocastic sampling.
    Take in num of words in sentence, and histogram. Return a sentence.'''
    sentence = []
    rand_tuple = get_random_tuple_prob(dict_w_weights)
    print('rand_tuple:', rand_tuple)
    second_to_last = rand_tuple[0]
    last_wrd = rand_tuple[1]
    sentence.append(second_to_last)
    sentence.append(last_wrd)
    nxt_nxt_wrd = find_wrd_after_tuple_key(rand_tuple, markov_dict)

    while len(sentence) < wrd_num:
        print('sentence:', sentence)
        last_wrd = nxt_nxt_wrd
        # if nxt_nxt_wrd is None:
        print('nxt_nxt_wrd:', nxt_nxt_wrd)
        if nxt_nxt_wrd != 'STOP':
            sentence.append(nxt_nxt_wrd)

            rand_tuple = (last_wrd, nxt_nxt_wrd)
            print('rand_tuple:', rand_tuple)
        else:
            break

    joined = " ".join(sentence) + "."
    return joined


def construct_sentence(wrd_num):
    clean_list = c.clean_txt('bluefish.txt')
    clean_list.append("STOP")

    markov_dict = m.second_order_markov_chain(clean_list)
    print("Second order markov chain:")
    pprint(markov_dict)

    dictionary = create_dict_from_list(clean_list)
    print("Dictionary of tuples:")
    pprint(dictionary)

    dict_w_weights = calculate_probability(dictionary)
    print("Dictionary with weights:")
    pprint(dict_w_weights)

    rand_sentence = create_sentence(wrd_num, dict_w_weights, markov_dict)
    print("This is my sentence: {}".format(rand_sentence))
    # # tweet = limit_140_chars(rand_sentence)
    # return rand_sentence
    # return tweet


def limit_140_chars(rand_sentence):
    '''Take in a string, return the first 140 characters only with first letter capitalized.'''
    tweet = rand_sentence[0:140]
    tweet = re.sub('([a-zA-Z])', lambda x: x.groups()[0].upper(), tweet, 1)
    tweet = re.sub(' i ', ' I ', tweet)
    tweet = re.sub("i'm", "I'm", tweet)
    tweet = re.sub("i s", "is", tweet)
    tweet = re.sub("i'd", "I'd", tweet)
    tweet = re.sub("does n", "doesn't", tweet)
    tweet = re.sub("doesn t", "doesn't", tweet)
    # print(tweet)
    return tweet


if __name__ == '__main__':
    construct_sentence(10)
    clean_list = c.clean_txt('bluefish.txt')



    # Proof that many random words returns each word within the desired range
    # get_many_rand_wrds(dict_w_weights, usr_input_count)
