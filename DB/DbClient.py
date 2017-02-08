# -*- coding: utf-8 -*-
# !/usr/bin/env python


from pymongo import MongoClient
import requests
import random

from Config.config import DATABASE

class MongoDBClient(object):

    def __init__(self, name, host, port):
        self.__conn = MongoClient(host, int(port))
        self.name = name                            #collection
        self.db = self.__conn[DATABASE]


    def get(self):
        '''
        从useful_proxy中随机抽取一个可用的代理 使用前需要切换表 changeTable('useful_proxy')
        :return:
        '''
        cursor = self.db[self.name].find()
        rint = random.randint(1,cursor.count()-1) if cursor.count() > 2 else 0 #随机抽取一个int值
        skip = cursor.skip(rint) #跳过rint条数据
        return cursor.next()['key'] if skip else None #返回一条数据对象

    def delete(self, key):
        self.db[self.name].remove({'key':key})

    def put(self,key):
        data = {
            'key':key,
            'value':None
        }
        return self.db[self.name].insert_one(data)


    def pop(self):
        '''
        弹出一个代理 并删除
        :return:
        '''
        key = self.get()
        if key:
            self.db[self.name].remove({'key':key})
            return key
        else:
            return None

    def changeTable(self, name):
        '''
        切换表
        :param name:
        :return:
        '''
        self.name = name


