import histogram as h
# import sys, string, re, time coming from the histogram file


def create_dict_from_file():
    '''Take a user input, convert to a clean list, return dictionary structure.
    Each unique wrd stored as key : frequency of the word stored as value.'''
    raw_txt_lst = h.take_usr_input()
    txt_list = h.clean_source_txt(raw_txt_lst)
    onefish_dict = h.histogram_dict(txt_list)
    return onefish_dict


if __name__ == '__main__':
    create_dict_from_file()
