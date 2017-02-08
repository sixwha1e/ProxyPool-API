# -*- coding: utf-8 -*-
# !/usr/bin/env python

from ProxyGetter.getFreeProxy import getFreeProxy
from DbClient import MongoDBClient

from Config.config import HOST,PORT,RAW_PROXY_COLLECTION,USEFUL_PROXY_COLLECTION

class ProxyClient(object):
    def __init__(self):
        self.raw_proxy_collection = RAW_PROXY_COLLECTION
        self.useful_proxy_collection = USEFUL_PROXY_COLLECTION
        self.db = MongoDBClient(self.raw_proxy_collection, HOST, PORT)

    def refresh(self):
        proxy_set = set()
        for proxy in getFreeProxy().allproxy():
            proxy_set.add(proxy)

        for proxy in proxy_set:
            self.db.changeTable(self.raw_proxy_collection)
            self.db.put(proxy)

    def get(self):
        self.db.changeTable(self.useful_proxy_collection)
        return self.db.pop()

    def delete(self, proxy):
        self.db.changeTable(self.useful_proxy_collection)
        self.db.delete(proxy)

if __name__ == '__main__':
    pc = ProxyClient()
    pc.refresh()





