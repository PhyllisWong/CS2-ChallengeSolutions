import random, sys


def load_word():
    '''Read the usr/shared/dict/words file to get a list of words.'''
    with open('randomWords.txt', 'r') as f:
        words_list = f.readlines()
        striped_words = [item.strip() for item in words_list]
        random_word = random.choice(striped_words)
        return random_word


def shuffle_letters(rand_word):
    '''Pass in a word, return a new word with the letters shuffled.'''
    shuffled = ''.join(random.sample(rand_word, len(rand_word)))
    print(shuffled)
    return shuffled


if __name__ == '__main__':
    params = sys.argv[1:]
    word = str(params[0])
    anagram = shuffle_letters(word)
