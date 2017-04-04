# -*- coding: utf-8 -*-
import random
from scrapy.downloadermiddlewares.httpproxy import HttpProxyMiddleware #代理ip，这是固定的导入
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware #代理UA，固定导入
class IPPOOLS(HttpProxyMiddleware):
    def __init__(self,ip=''):
        '''初始化'''
        self.ip=ip
    def process_request(self, request, spider):
        '''使用代理ip，随机选用'''
        ip=random.choice(self.ip_pools) #随机选择一个ip
        print '当前使用的IP是'+ip['ip']
        try:
            request.meta["proxy"]="http://"+ip['ip']
        except Exception,e:
            print e
            pass
    ip_pools=[
        {'ip': '124.65.238.166:80'},
        # {'ip':''},
    ]
class UAPOOLS(UserAgentMiddleware):
    def __init__(self,user_agent=''):
        self.user_agent=user_agent
    def process_request(self, request, spider):
        '''使用代理UA，随机选用'''
        ua=random.choice(self.user_agent_pools)
        print '当前使用的user-agent是'+ua
        try:
            request.headers.setdefault('User-Agent',ua)
        except Exception,e:
            print e
            pass
    user_agent_pools=[
        'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3',
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36',
    ]