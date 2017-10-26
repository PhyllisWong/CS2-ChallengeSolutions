import random, sys


def load_word():
    """Read a text file with a list of words."""
    f = open('randomWords.txt', 'r')
    words_list = f.readlines()
    f.close()
    words_list = words_list[0].split(' ')
    random_word = random.choice(words_list)
    return random_word


def construct_sentence(num):
    sentence = []
    while len(sentence) < num:
        word = load_word().lower()
        sentence.append(word.strip())
    print(" ".join(sentence) + ".")


if __name__ == '__main__':
    params = sys.argv[1:]
    num = int(params[0])
    rand_sent = construct_sentence(num)
