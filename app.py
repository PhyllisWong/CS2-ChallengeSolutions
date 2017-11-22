# DELCARATIONS
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
import os

import sentence_constructor as s
'''sentence_constructor methods generate random words and construct sentences.'''
# import histogram as h

app = Flask(__name__)

# MIDDLEWARE
# if os.environ.get('DATABASE_URL'):
#     db_url = os.environ.get('DATABASE_URL')
# else:
#     db_url = 'postgresql://localhost/TweetGenerator'
#
# app.config['SQLALCHEMY_DATABASE_URI'] = db_url
#
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)
#
# engine = create_engine('postgresql://localhost/TweetGenerator')


# ROUTES
@app.route('/')
def rand_sentence():
    sentence = s.construct_sentence(10)
    # rand_sentence = s.create_sentence(10, dict_w_weights)
    return sentence


rand_sentence()
# if __name__ == '__main__':
#     app.run()
