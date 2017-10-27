import sys, string


def clean_source_txt():
    with open("alice-in-wonderland.txt", "r") as f:
        # store the text in an array, each index is a line of text
        text = f.readlines()
        f.close()
        # cleans all new lines and special chars from list
        stripped = [line.strip() for line in text]
        # splits each index into single words
        word_list = [words for segment in stripped for words in segment.split()]
        lowered = [word.lower() for word in word_list]
        no_punc = [punc.strip("():?;,.!/") for punc in lowered]
        print(no_punc)


def histogram():
    '''
    function which takes a source_text argument (can be either a filename or the contents of the file as a string, your choice) and return a histogram data structure that stores each unique word along with the number of times the word appears in the source text
    '''
    pass


def unique_words():
    '''
    function that takes a histogram argument and returns the total count of unique words in the histogram. For example, when given the histogram for The Adventures of Sherlock Holmes, it returns the integer 8475
    '''
    pass


def frequency():
    '''
    function that takes a word and histogram argument and returns the number of times that word appears in a text. For example, when given the word "mystery" and the Holmes histogram, it will return the integer 20
    '''
    pass


def main():
    # collect command line arguments into a list and return list
    arguments = []
    for arg in sys.argv[1:]:
        arguments.append(arg)
        print(arguments)
    # return arguments
    pass


if __name__ == '__main__':
    print(__name__)
    main()
    clean_source_txt()
