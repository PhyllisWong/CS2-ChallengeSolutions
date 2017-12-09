import sys
import string
import re
"""Clean files for the raw text. Code Credit from Sam Galizia"""


def clean_txt(filename):
    '''Take file as argument, return a list of individual words.'''
    txt_file = open(filename, 'r')
    words_list = txt_file.read().lower()
    remove_punctuation(words_list)
    result_list = []

    items = re.findall("[A-z]+\'?[A-z]*|\$[0-9]*", words_list)
    for item in items:
        result_list.append(item)
    return result_list


def remove_punctuation(text):
    no_punc_txt = re.sub('[,.()]', '', text)
    no_punc_txt = re.sub('--', ' ', no_punc_txt)
    no_punc_txt = re.sub(':', ' ', no_punc_txt)
    no_punc_txt = re.sub('/(?<!\S).(?!\S)\s*/', '', no_punc_txt)
    return no_punc_txt


def main():
    user_arg_count = len(sys.argv)
    if user_arg_count == 1:
        print('Error: textfile not provided')
    else:
        txt_file = open(sys.argv[1], 'r')
        words_list = txt_file.read().lower()
        print(words_list)

        items = re.findall("[A-z]+\'?[A-z]*|\$[0-9]*", words_list)
        for item in items:
            print(item)


if __name__ == '__main__':
    main()
