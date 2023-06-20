#!/usr/bin/env python3

from flask import Flask,logging

app = Flask(__name__)
@app.route('/')
def index():
    return f'<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<name>')
def print_string(name):
   return f'hello'

@app.route('/print/<text>')
def print_text(text):
    app.logger.info(text)
    return 'Text printed successfully'

if __name__ == '__main__':
    app.run(port=5555, debug=True)
