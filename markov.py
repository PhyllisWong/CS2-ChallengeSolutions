#!python
from __future__ import division, print_function  # Python 2 and 3 compatibility
import random


class Dictogram(dict):
    """Dictogram is a histogram implemented as a subclass of the dict type."""

    def __init__(self, word_list=None):
        """Initialize this histogram as a new dict and count given words."""
        super(Dictogram, self).__init__()  # Initialize this as a new dict

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
    markov = {}
    index = 0
    while index < len(word_list)-1:
        current = word_list[index]
        next_word = word_list[index+1]
        if current not in markov.keys():
            markov[current] = Dictogram() # {} Dictogram is empty array
            print(markov)
        markov[current].add_count(next_word)
        index+=1
    print(markov)
    print('this shit')


def print_histogram(word_list):
    print('word list: {}'.format(word_list))
    # Create a dictogram and display its contents
    histogram = Dictogram(word_list)
    print('dictogram: {}'.format(histogram))
    print('{} tokens, {} types'.format(histogram.tokens, histogram.types))
    for word in word_list[-2:]:
        freq = histogram.frequency(word)
        print('{!r} occurs {} times'.format(word, freq))
    print()


def main():
    import sys
    arguments = sys.argv[1:]  # Exclude script name in first argument
    if len(arguments) >= 1:
        # Test histogram on given arguments
        print_histogram(arguments)
    else:
        # Test histogram on letters in a word
        word = 'abracadabra'
        print_histogram(list(word))
        # Test histogram on words in a classic book title
        fish_text = 'one fish two fish red fish blue fish'
        print_histogram(fish_text.split())
        # Test histogram on words in a long repetitive sentence
        woodchuck_text = ('how much wood would a wood chuck chuck'
                          ' if a wood chuck could chuck wood')
        print_histogram(woodchuck_text.split())
        markov_chain("one fish two fish two fish red fish blue fish".split())


if __name__ == '__main__':
    main()
