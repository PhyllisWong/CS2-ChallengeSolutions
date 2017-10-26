import random, sys


def load_word():
    """Read the usr/shared/dict/words file to get a list of words."""
    with open("/usr/share/dict/words", "r") as f:
        words_list = f.readlines()
        striped_words = [item.strip() for item in words_list]
        random_word = random.choice(striped_words)
        return random_word


def construct_sentence(num):
    """Build a sentence with random words from load_word() func."""
    sentence = []
    while len(sentence) < num:
        word = load_word().lower()
        sentence.append(word)
    print(" ".join(sentence) + ".")


if __name__ == '__main__':
    params = sys.argv[1:]
    num = int(params[0])
    rand_sent = construct_sentence(num)
