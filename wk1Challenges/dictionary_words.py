import random, sys, time


def load_word():
    """Read the usr/shared/dict/words file to get a list of words."""
    with open("/usr/share/dict/words", "r") as f:
        words_list = f.readlines()
        # striped_words = [item.strip() for item in words_list]
        random_word = random.choice(words_list)
        return random_word.strip()


def construct_sentence(num):
    """Build a sentence with random words from load_word() func."""
    sentence = ""
    while len(sentence) < num:
        sentence += (load_word() + " ")
    print(sentence)


time2 = time.time()
print("construct time: " + str(time2))


if __name__ == '__main__':
    time1 = time.time()
    print("load time: " + str(time1))
    words = open("/usr/share/dict/words", "r").readlines()
    params = sys.argv[1:]
    num = int(params[0])
    print(construct_sentence(num))
    time2 = time.time()
    print("run program time: " + str(time2))
    print(time1 - time2)
