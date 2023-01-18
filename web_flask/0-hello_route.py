#!/usr/bin/python3
"""starts a Flask web application:"""


from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_hbnb():
    """ return  “Hello HBNB!” string when route quired"""
    return "Hello HBNB!"


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
