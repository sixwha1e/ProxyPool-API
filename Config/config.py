# -*- coding: utf-8 -*-
# !/usr/bin/env python

'''Mongo Config'''
HOST = '127.0.0.1'
PORT = 27017
DATABASE = 'proxypool'
RAW_PROXY_COLLECTION = 'raw_proxy'
USEFUL_PROXY_COLLECTION = 'useful_proxy'

'''Request Headers'''
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Upgrade-Insecure-Requests': '1',
    'Connection': 'keep-alive'
}