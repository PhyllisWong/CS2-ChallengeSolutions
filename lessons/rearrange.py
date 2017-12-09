import random,sys


def rearrange_sentence(my_list):
    '''Take in an array, rearrange into new array, return as a joined str.'''
    new_list = []
    index = 0
    while index < len(my_list):
        rand_num = random.randint(0, len(my_list)-1)
        to_append = my_list.pop(rand_num)
        new_list.append(to_append)
    # Join the array of rearranged words into a string with punctuation
    joined = " ".join(new_list) + "."
    return joined


def main():
    # collect command line arguments into a list and return list
    arguments = []
    for arg in sys.argv[1:]:
        arguments.append(arg)
    return arguments


if __name__ == '__main__':
    my_list = main()
    new_sentence = rearrange_sentence(my_list)
    print(new_sentence)
