import histogram as h
import random, sys
# import sys, string, re, time coming from the histogram file


def create_dict_from_file():
    '''Take a user input, convert to a clean list, return dictionary structure.
    Each unique wrd stored as key : frequency of the word stored as value.'''
    raw_txt_lst = h.take_usr_input('alice-in-wonderland.txt')
    txt_list = h.clean_source_txt(raw_txt_lst)
    dictionary = h.histogram_dict(txt_list)
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
        # print(wrd_weight, rand_float, probability)
        probability += wrd_weight
        if rand_float < probability:
            break
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


def create_sentence(wrd_num, dict_w_weights):
    '''Create a sentence using stocastic sampling.
    Take in num of words in sentence, and histogram. Return a sentence.'''
    sentence = []
    while len(sentence) < wrd_num:
        rand_wrd = get_random_wrd_prob(dict_w_weights)
        sentence.append(rand_wrd)
    joined = " ".join(sentence) + "."
    # print(joined)
    return joined


if __name__ == '__main__':
    dictionary = create_dict_from_file()
    # rand_wrd = get_random_wrd(dictionary)
    dict_w_weights = calculate_probability(dictionary)
    # Get random word using probability
    get_random_wrd_prob(dict_w_weights)
    usr_input_count = int(sys.argv[-1])
    rand_sentence = create_sentence(usr_input_count, dict_w_weights)
    print(rand_sentence)
    # Proof that many random words returns each word within the desired range
    # get_many_rand_wrds(dict_w_weights, usr_input_count)
