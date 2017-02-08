# -*- coding: utf-8 -*-
# !/usr/bin/env python

from apscheduler.schedulers.blocking import BlockingScheduler
from DB.ProxyClient import ProxyClient
from multiprocessing import Process
import requests
import time
import sys


class ProxyRefreshSchedule(ProxyClient):
    '''
    定时更新代理
    '''
    def __init__(self):
        ProxyClient.__init__(self)

    def validProxy(self):
        raw_proxy = self.db.pop()
        while raw_proxy:
            proxies = {'http':'http://{proxy}'.format(proxy=raw_proxy),
                       'https':'https://{proxy}'.format(proxy=raw_proxy)
                       }
            try:
                response = requests.get('http://ip.chinaz.com/getip.aspx', proxies=proxies, timeout=50, verify=False)
                if response.status_code == 200:
                    self.db.changeTable(self.useful_proxy_collection)
                    self.db.put(raw_proxy)
            except Exception as e:
                pass
            self.db.changeTable(self.raw_proxy_collection)
            raw_proxy = self.db.pop()


def refreshPool():
    p = ProxyRefreshSchedule()
    p.validProxy()


def main(process_num=100):
    refreshPool()

    for num in range(process_num):
        P = Process(target=refreshPool, args=())
        P.start()

    print '{time}: refresh complete!'.format(time=time.ctime())


if __name__ == '__main__':
    main()
    sche = BlockingScheduler()
    sche.add_job(main, 'interval', minutes=20)
    sche.start()



