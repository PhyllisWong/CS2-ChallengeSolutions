import random, sys

quotes = ("It's just a flesh wound.",
          "He's not the Messiah. He's a very naughty boy!",
          "THIS IS AN EX-PARROT!!")


def random_python_quote():
    rand_index = random.randint(0, len(quotes) - 1)
    return quotes[rand_index]


def reverse_word(word):
    reversed_word = word[::-1]
    # print(reversed_word)
    return reversed_word


def madlib(noun1, adj, noun2, verb1, verb2):
    constructed_sentence = "The {} {} to the {} {} all while {}.".format(noun1, verb1,
                            adj, noun2, verb2)
    print(constructed_sentence)


if __name__ == '__main__':
    params = sys.argv[1:]
    noun1 = str(params[0])
    verb1 = str(params[1])
    adj = str(params[2])
    noun2 = str(params[3])
    verb2 = str(params[4])
    my_lib = madlib(noun1, adj, noun2, verb1, verb2)
    # quote = random_python_quote()
    # new_word = reverse_word("python is rad")
    # print(quote)
    # print(new_word)
