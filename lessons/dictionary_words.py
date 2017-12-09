import random, sys, time


# V1
def load_word_list(file_name):
    """Read the usr/shared/dict/words file to get a list of words."""
    with open("/usr/share/dict/words", "r") as f:
        words_list = f.readlines()
        random_word = random.choice(words_list)
        return random_word.strip()


# V2
def random_word():
    # create a random number for each index
    random_index = random.randint(0, len(dict_words) - 1)
    return dict_words[random_index].rstrip('\n')


def multiple_rand_words(number_of_words):
    list_of_words = ''
    for i in range(0, number_of_words):
        list_of_words += (random_word() + ' ')
    return list_of_words
# multiple_rand_words(number_of_words)


timestamp1 = time.time()
print(timestamp1)


if __name__ == '__main__':
    dict_words = open("/usr/share/dict/words").readlines()
    # dict_words = load_word_list(file_name)
    input = int(sys.argv[1])
    print(multiple_rand_words(input))
    timestamp2 = time.time()
    print(timestamp2)
    print(timestamp2 - timestamp1)
# if __name__ == '__main__':
#     time1 = time.time()
#     # print("load time: " + str(time1))
#     words = open("/usr/share/dict/words", "r").readlines()
#     params = sys.argv[1]
#     num = int(params)
#     print(construct_sentence(num))
#     time2 = time.time()
#     # print("run program time: " + str(time2))
#     print(time1 - time2)
