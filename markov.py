#!python
from __future__ import division, print_function  # Python 2 and 3 compatibility


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
        # Retrieve word frequency count
        if word not in self:
            return 0
        return self[word]


def markov_chain(word_list):
    # Holds the Dictionary of dictograms
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


def second_order_markov_chain(word_list):
    # Holds the Dictionary of dictograms
    markov = {}
    index = 0
    # Search through the list of words
    while index < len(word_list)-2:
        curr_word = word_list[index]
        next_word = word_list[index+1]
        wrd_after_nxt = word_list[index+2]
        # Add the word to the dictionary if not in in there
        if (curr_word, next_word) not in markov.keys():
            # Set newly added word as a tuple[0] and next_word as tuple[1]
            # with the value of a dictionary object
            markov[(curr_word, next_word)] = Markov()
        # If the word is already in the dictionary, increase the count
        # print((curr_word, next_word), "word after next: {}".format(wrd_after_nxt))
        markov[(curr_word, next_word)].add_count(wrd_after_nxt)
        # if wrd_after_nxt == "STOP":
        #     print("None!!!")
        # Look at the next word, repeat the loop
        index+=1
    return markov


def print_histogram(word_list):
    print("print_function: is printing HERE!!!")
    print('word list: {}'.format(word_list))
    # Create a dictogram and display its contents
    histogram = Markov(word_list)
    print('dictogram: {}'.format(histogram))
    print('{} tokens, {} types'.format(histogram.tokens, histogram.types))
    for word in word_list[-2:]:
        freq = histogram.frequency(word)
        print('{!r} occurs {} times'.format(word, freq))


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
        onefish_list.append("STOP")
        # print(onefish_list)
        # Create the Dictionary of Histograms
        markov_dict = second_order_markov_chain(onefish_list)
        # print(markov_dict)
        # Test histogram on words in a long repetitive sentence
        # woodchuck_text = ('how much wood would a wood chuck chuck'
        #                   ' if a wood chuck could chuck wood')
        # print_histogram(woodchuck_text.split())
        # markov_chain("one fish two fish two fish red fish blue fish".split())


if __name__ == '__main__':
    main()
