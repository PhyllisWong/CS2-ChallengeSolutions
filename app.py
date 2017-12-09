# DELCARATIONS
from flask import Flask
import os

import sentence_constructor as s
'''sentence_constructor methods generate random words and construct sentences.'''
# import histogram as h

app = Flask(__name__)

# ROUTES
@app.route('/')
def rand_sentence():
    sentence = s.construct_sentence(18)
    # print(sentence)
    return sentence


rand_sentence()
# if __name__ == '__main__':
#     app.run()
