import sys, string, re


def handle_input():
    '''Imput the file to read from the command line, read file.'''
    usr_input = sys.argv[1]
    with open(usr_input, 'r') as f:
        # Convert file to list
        raw_txt = f.readlines()
        return raw_txt


def clean_source_txt(raw_txt_lst):
    '''Take list as argument, return a cleaned list of individual words.'''
    # Removes punctuation from text, returns a string
    for char in raw_txt_lst:
        if char not in string.punctuation:
            no_punc = ''.join(char.lower())
    # cleans all new lines and special chars from string, returns a list
    clean_txt = re.split('\s*\W+', no_punc)[:-1]
    print(clean_txt)
    return clean_txt


def histogram_dict(txt_list):
    '''Take a list argument, return a histogram dictionary structure.
    Store each unique word as the key and frequency of the word as value.'''
    onefish_dict = {}
    get = onefish_dict.get
    for word in txt_list:
        onefish_dict[word] = get(word, 0) + 1
    return onefish_dict


if __name__ == '__main__':
    raw_txt_lst = handle_input()
    clean_source_txt(raw_txt_lst)
