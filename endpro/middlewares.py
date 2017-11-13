# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import random
from scrapy.downloadermiddlewares.httpproxy import HttpProxyMiddleware


class EndproSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class HTTPPROXY(HttpProxyMiddleware):
    def __init__(self,ip=' '):
        self.ip=ip

    def process_request(self,request,spider):
        item=random.choice(IPPOOL)
        try:
            print('当前ip是：'+item['ipaddr'])
            request.meta['proxy']='http://'+item['ipaddr']
        except Exception as e:
            print(e)
            pass

IPPOOL=[  
    {"ipaddr":"121.232.145.247:9000"},  
    {"ipaddr":"59.62.27.129:808"},  
    {"ipaddr":"121.232.144.39:9000"},  
    {"ipaddr":"121.232.148.83:9000"},  
    {"ipaddr":"117.90.0.155:9000"},  
    {"ipaddr":"111.155.124.81:8123"},  
    {"ipaddr":"106.120.78.129:80"}  
]  





