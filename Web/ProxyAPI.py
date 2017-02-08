# -*- coding: utf-8 -*-
# !/usr/bin/env python

from DB.ProxyClient import ProxyClient
from flask import Flask, jsonify
import sys


sys.path.append('../')

app = Flask(__name__)

list = {
    'get': 'get an enable proxy',
    'refresh': 'refresh proxy pool',
    'delete/<proxy>': 'delete an unable proxy'
}

@app.route('/')
def index():
    return jsonify(list)

@app.route('/get/')
def get():
    proxy = ProxyClient().get()
    return proxy

@app.route('/refresh/')
def refresh():
    ProxyClient().refresh()
    return 'success'

@app.route('/delete/<proxy>')
def delete(proxy):
    ProxyClient().delete(proxy)
    return 'success'


if __name__ == '__main__':
    app.run()
