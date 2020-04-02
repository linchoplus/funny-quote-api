#!/usr/bin/env python3

"""Get random funny quote"""

import flask
import json
import random

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.
quotes_file = 'funny.json'

with open(quotes_file) as json_file:
    quotes = json.load(json_file)


@app.route('/', methods=['GET'])
def home():
    """API 'home' page with example"""
    return '''<h1> Funny Quotes API</h1>
<p> http://127.0.0.1:5000/api/v1/quote</p>'''


@app.route('/api/v1/quote', methods=['GET'])
def api_random():
    """GET random quote"""
    return random.choice(quotes)


app.run()
