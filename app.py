
# DELCARATIONS
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
import os

import sample as s
# import histogram as h

app = Flask(__name__)

# MIDDLEWARE
if os.environ.get('DATABASE_URL'):
    db_url = os.environ.get('DATABASE_URL')
else:
    db_url = 'postgresql://localhost/TweetGenerator'

app.config['SQLALCHEMY_DATABASE_URI'] = db_url

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

engine = create_engine('postgresql://localhost/TweetGenerator')

# ROUTES


@app.route('/')
def hello():
    dictionary = s.create_dict_from_file()
    # rand_wrd = get_random_wrd(dictionary)
    dict_w_weights = s.calculate_probability(dictionary)
    # Get random word using probability
    # s.get_random_wrd_prob(dict_w_weights)
    # usr_input_count = int(sys.argv[-1])
    rand_sentence = s.create_sentence(10, dict_w_weights)

    return rand_sentence

# def print_to_web():
#     my_dict = s.create_dict_from_file()
#     return my_dict

if __name__ == '__main__':
    app.run()
