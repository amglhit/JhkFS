#!/usr/bin/env python
# coding=utf-8

from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World'

@app.route('/name')
def name():
    return 'Hi!'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
