# -*- coding: utf-8 -*-
# !/usr/bin/env python

from bs4 import BeautifulSoup
import requests
import sys
import re

from Config.config import HEADERS


reload(sys)
sys.setdefaultencoding('utf-8')

proxies = []
class getFreeProxy(object):

    global proxies
    def __init__(self):
        pass

    def proxyOne(self, page=10):
        '''
        抓取快代理IP http://www.kuaidaili.com/proxylist/1/
        :param page: 翻页数
        :return:
        '''

        urls = ('http://www.kuaidaili.com/proxylist/{page}/'.format(page=page) for page in range(1,page+1))
        for url in urls:
            response = requests.get(url, headers=HEADERS)
            soup = BeautifulSoup(response.content, 'lxml')
            trs = soup.findAll('tr')
            for i in range(1, len(trs)):
                tds = trs[i].findAll('td')
                ip = tds[0].contents[0]
                port = tds[1].contents[0]
                proxies.append(ip+':'+port)

    def proxyTwo(self, page=10):
        '''
        抓取66ip代理 http://m.66ip.cn/1.html
        :param page: 翻页数
        :return:
        '''

        urls = ('http://m.66ip.cn/{page}.html'.format(page=page) for page in range(1,page+1))
        for url in urls:
            response = requests.get(url, headers=HEADERS)
            soup = BeautifulSoup(response.content, 'lxml')
            trs = soup.findAll('tr')
            for i in range(1, len(trs)):
                tds = trs[i].findAll('td')
                ip = tds[0].contents[0]
                port = tds[1].contents[0]
                proxies.append(ip+':'+port)


    def proxyThree(self, page=10):
        '''
        guobanjia代理 http://www.goubanjia.com/free/gngn/index1.shtml
        :param page: 翻页数
        :return:
        '''

        ip = ''
        urls = ('http://www.goubanjia.com/free/gngn/index{page}.shtml'.format(page=page) for page in range(1,page+1))
        for url in urls:
            response = requests.get(url, headers=HEADERS)
            tds = re.findall(r'<td class="ip">(.*?)</td>', response.content, re.DOTALL)
            for td in tds:
                temps = re.findall(r'<span.*?>(.*?)</span>|<div.*?>(.*?)</div>|</span>(.*?)<span class="port', td, re.DOTALL)
                length = len(temps)
                for j in range(length-1):
                    for i in range(3):
                        if temps[j][i] != '':
                            ip = ip + str(temps[j][i])
                proxies.append(ip+':'+temps[length-1][0])
                ip = ''



    def proxyFour(self, page=10):
        '''
        西刺代理 http://www.xicidaili.com/nn/1
        :param page: 翻页数
        :return:
        '''

        urls = ('http://www.xicidaili.com/nn/{page}'.format(page=page) for page in range(page+1))
        for url in urls:
            response = requests.get(url, headers=HEADERS)
            soup = BeautifulSoup(response.content, 'lxml')
            trs = soup.findAll('tr')
            for i in range(1, len(trs)):
                td = trs[i].findAll('td')
                port = td[2].contents[0]
                ip = td[1].contents[0]
                proxies.append(ip+':'+port)

    def allproxy(self):
        self.proxyOne()
        self.proxyTwo()
        self.proxyThree()
        self.proxyFour()
        return proxies






