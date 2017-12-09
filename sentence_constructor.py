import histogram as h
import cleanup as c
import random, sys, re
import markov as m
# import sys, string, re, time coming from the histogram file


def create_dict_from_list(clean_list):
    '''Take a user input, convert to a clean list, return dictionary structure.
    Each unique wrd stored as key : frequency of the word stored as value.'''
    # raw_txt_lst = h.take_usr_input('alice-in-wonderland.txt')
    # txt_list = h.clean_source_txt(raw_txt_lst)
    dictionary = h.histogram_dict(clean_list)
    # print(dictionary)
    return dictionary


def get_random_wrd(dictionary):
    '''Return a random word from a dictionary.'''
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
    return dict_w_weights


def get_random_wrd_prob(dict_w_weights):
    '''Take a dictionary, select random word based on its probability.'''
    rand_float = random.random()
    probability = 0.0
    for wrd, wrd_weight in dict_w_weights.items():
        probability += wrd_weight
        if rand_float < probability:
            break
    # print(dict_w_weights)
    return wrd


def get_many_rand_wrds(dictionary, num):
    '''Create a dictionary with the random word, and num of times selected.'''
    rand_dict = {}
    while sum(rand_dict.values()) < int(num):
        rand_wrd = get_random_wrd_prob(dictionary)
        if rand_wrd not in rand_dict:
            rand_dict[rand_wrd] = 1
        else:
            rand_dict[rand_wrd] += 1
    # print(rand_dict)
    return rand_dict


def create_sentence(wrd_num, dict_w_weights, markov_dict):
    '''Create a sentence using stocastic sampling.
    Take in num of words in sentence, and histogram. Return a sentence.'''
    sentence = []
    while len(sentence) < wrd_num:
        rand_wrd = get_random_wrd_prob(dict_w_weights)

        pair_wrds = find_pair_of_words(rand_wrd, markov_dict)
        # print(pair_wrds)
        sentence.append(pair_wrds[0])
        sentence.append(pair_wrds[1])
        # nxt_wrd = find_word_after_rand_wrd(rand_wrd, markov_dict)
        # sentence.append(nxt_wrd)
    # joined = " ".join(sentence) + "."
    # print(joined)
    return pair_wrds

def find_pair_of_words(rand_wrd, markov_dict):
    print("THIS RANDOM WORD: {}".format(rand_wrd))
    for (tuple_key, dictogram) in markov_dict.items():
        if tuple_key[0] == rand_wrd:
            print(tuple_key)
            return tuple_key

def find_wrd_after_tuple_key(tuple_key, markov_dict):
    # print("USE THIS Tuple: {}\n".format(tuple_key))
    print("SECOND ORDER markov: {}\n".format(markov_dict))
    return tuple_key

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


def construct_sentence(wrd_num):
    clean_list = c.clean_txt('onefish.txt')
    clean_list.append("STOP")

    dictionary = create_dict_from_list(clean_list)
    # print(dictionary)
    dict_w_weights = calculate_probability(dictionary)
    rand_wrd = get_random_wrd_prob(dict_w_weights)
    markov_dict = m.second_order_markov_chain(clean_list)

    # print("SECOND ORDER markov: {}\n".format(markov_dict))

    tuple_key = find_pair_of_words(rand_wrd, markov_dict)
    nxt_wrd = find_wrd_after_tuple_key(tuple_key, markov_dict)
    rand_sentence = create_sentence(wrd_num, dict_w_weights, markov_dict)

    # tweet = limit_140_chars(rand_sentence)
    return rand_sentence
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
    # clean_list = c.clean_txt('onefish.txt')
    # # print(clean_list)
    # clean_list.append("STOP")
    # print(clean_list)
    # dictionary = create_dict_from_list(clean_list)

    construct_sentence(8)

    # Proof that many random words returns each word within the desired range
    # get_many_rand_wrds(dict_w_weights, usr_input_count)
