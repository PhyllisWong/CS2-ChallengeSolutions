# DELCARATIONS
from flask import Flask
import cleanup as c
import os

import sentence_constructor as s
'''sentence_constructor methods generate random words and construct sentences.'''
# import histogram as h

app = Flask(__name__)


# ROUTES
@app.route('/')
def rand_sentence():
    clean_list = s.clean_text()
    clean_list.append("STOP")
    sentence = s.construct_sentence(18, clean_list)
    # print(sentence)
    return sentence

rand_sentence()

# if __name__ == '__main__':
#     app.run()

# interact with the twitter API
# make an account for the tweet gen
# set a timeout in the rand_sentence func
