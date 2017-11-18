#!python
from __future__ import division, print_function  # Python 2 and 3 compatibility
import random


class Markov(dict):
    """Dictogram is a histogram implemented as a subclass of the dict type."""

    def __init__(self, word_list=None):
        """Initialize this histogram as a new dict and count given words."""
        super(Markov, self).__init__()  # Initialize this as a new dict

        self.types = 0
        self.tokens = 0
        # Count words in given list, if any
        if word_list is not None:
            for word in word_list:
                self.add_count(word)

    def add_count(self, word, count=1):
        """Increase frequency count of given word by given count amount."""
        # self refers to the object which is an instance of dictionary
        if word in self:
            self[word] += count
        else:
            self.types += 1
            self[word] = count
        self.tokens += count

    def frequency(self, word):
        """Return frequency count of given word, or 0 if word is not found."""
        # TODO: Retrieve word frequency count
        if word not in self:
            return 0
        return self[word]


def markov_chain(word_list):
    # Holds the Dictionary of histograms
    markov = {}
    index = 0
    # Search through the list of words
    while index < len(word_list)-1:
        curr_word = word_list[index]
        next_word = word_list[index+1]
        # Add the word to the dictionary if not in in there
        if curr_word not in markov.keys():
            # Set newly added word with the value of a dictionary object
            markov[curr_word] = Markov()
        # If the word is already in the dictionary, increase the count
        markov[curr_word].add_count(next_word)
        # Look at the next word, repeat the loop
        index+=1
    return markov


def print_histogram(word_list):
    print('word list: {}'.format(word_list))
    # Create a dictogram and display its contents
    histogram = Markov(word_list)
    print('dictogram: {}'.format(histogram))
    print('{} tokens, {} types'.format(histogram.tokens, histogram.types))
    for word in word_list[-2:]:
        freq = histogram.frequency(word)
        print('{!r} occurs {} times'.format(word, freq))
    print()


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


def main():
    import sys
    # Import the module to clean text
    import cleanup as clean
    arguments = sys.argv[1:]  # Exclude script name in first argument
    if len(arguments) >= 1:
        # Test histogram on given arguments
        print_histogram(arguments)
    else:
        onefish_list = clean.clean_txt('onefish.txt')
        print(onefish_list)
        # Create the Dictionary of Histograms
        markov_dict = markov_chain(onefish_list)
        print(markov_dict)
        rand_wrd = get_random_wrd(markov_dict)
        print(rand_wrd)
        # Test histogram on words in a long repetitive sentence
        # woodchuck_text = ('how much wood would a wood chuck chuck'
        #                   ' if a wood chuck could chuck wood')
        # print_histogram(woodchuck_text.split())
        # markov_chain("one fish two fish two fish red fish blue fish".split())


if __name__ == '__main__':
    main()
