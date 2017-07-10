# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from selenium import webdriver
import time
from scrapy.http import HtmlResponse
import urllib.parse
import json
import re

# class SinaWeiboSpiderMiddleware(object):
#     # Not all methods need to be defined. If a method is not defined,
#     # scrapy acts as if the spider middleware does not modify the
#     # passed objects.
#
#     @classmethod
#     def from_crawler(cls, crawler):
#         # This method is used by Scrapy to create your spiders.
#         s = cls()
#         crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
#         return s
#
#     def process_spider_input(self, response, spider):
#         # Called for each response that goes through the spider
#         # middleware and into the spider.
#
#         # Should return None or raise an exception.
#         return None
#
#     def process_spider_output(self, response, result, spider):
#         # Called with the results returned from the Spider, after
#         # it has processed the response.
#
#         # Must return an iterable of Request, dict or Item objects.
#         for i in result:
#             yield i
#
#     def process_spider_exception(self, response, exception, spider):
#         # Called when a spider or process_spider_input() method
#         # (from other spider middleware) raises an exception.
#
#         # Should return either None or an iterable of Response, dict
#         # or Item objects.
#         pass
#
#     def process_start_requests(self, start_requests, spider):
#         # Called with the start requests of the spider, and works
#         # similarly to the process_spider_output() method, except
#         # that it doesn’t have a response associated.
#
#         # Must return only requests (not items).
#         for r in start_requests:
#             yield r
#
#     def spider_opened(self, spider):
#         spider.logger.info('Spider opened: %s' % spider.name)

#调用中间件
class MySelenium_PhantomJS_Middleware(object):
    def process_request(self,request,spider):
        kw = input("请输入要查询的字符串:")
        u_kw = urllib.parse.quote(kw)
        #调用selenium的phantomjs浏览器进行渲染
        driver = webdriver.PhantomJS()
        # driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(request.url)
        time.sleep(2)
        #登录
        driver.find_element_by_id("loginName").send_keys("你的用户名")
        driver.find_element_by_id("loginPassword").send_keys("你的密码")
        driver.find_element_by_id("loginAction").click()
        print("正在登录")
        time.sleep(2)
        offset = 1
        flag = [1,]
        body_list = []
        while len(flag) == 1:
            start_url = "https://m.weibo.cn/api/container/getIndex?type=all&queryVal="+u_kw+"&featurecode=20000320&luicode=10000011&lfid=106003type%3D1&title="+u_kw+"&containerid=100103type%3D1%26q%3D"+u_kw+"&page="+str(offset)
            driver.get(start_url)
            time.sleep(2)
            body = driver.page_source
            body_select = re.compile(r'<html><head></head><body><pre.*;">(.*?)</pre></body></html>')
            body_result = body_select.match(body).group(1)
            data_list = json.loads(body_result)['cards']
            if len(data_list) == 0:
                print("获取到末页")
                flag = []
            else:
                offset = offset + 1
                body_list.append(data_list)
        #返回数据
        body_json = json.dumps(body_list)
        return HtmlResponse(driver.current_url, body=body_json, encoding='utf-8', request=request)

