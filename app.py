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
def rand_sentence(clean_list):
    sentence = s.construct_sentence(18, clean_list)
    # print(sentence)
    return sentence

clean_list = s.clean_text()
clean_list.append("STOP")
rand_sentence(clean_list)
# if __name__ == '__main__':
#     app.run()
