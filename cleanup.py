import sys
import string
import re


def take_usr_input(file_name):
    # User intputs the file to read, returns file
    # usr_input = sys.argv[1]
    with open(file_name, 'r') as f:
        raw_txt = f.readlines()
        return raw_txt


def clean_source_txt(raw_txt_lst):
    '''Take list as argument, return a cleaned list of individual words.'''
    # Removes punctuation from text, returns a string
    no_punc = ''.join([char.lower() for char in raw_txt_lst if char not in string.punctuation])
    # cleans all new lines and special chars from string, returns a list
    clean_txt = re.split('\s*\W+', no_punc)[:-1]
    return clean_txt


def main():
    file_name = sys.argv[1]
    raw_txt_lst = take_usr_input(file_name)
    clean_source_txt(raw_txt_lst)


if __name__ == '__main__':
    main()
