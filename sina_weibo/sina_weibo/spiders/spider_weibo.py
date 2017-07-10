# -*- coding: utf-8 -*-
import scrapy
import json
import re
from sina_weibo.items import SinaWeiboItem
from scrapy.http import HtmlResponse


class SpiderWeiboSpider(scrapy.Spider):
    name = 'spider_weibo'
    allowed_domains = ['weibo.cn']
    start_urls = ['https://passport.weibo.cn/signin/login']

    def parse(self, response):
        #第一种方法，使用json数据
        content_select = re.compile(r'&lt;.*?&gt;')
        response_list = json.loads(response.text)
        #循环多少页
        for item_list in response_list:
            redis_item = {}
            #循环每个页面内容
            for item_card_group in range(len(item_list[0]['card_group'])):
                item = SinaWeiboItem()
                try:
                    item['nick_name'] = item_list[0]['card_group'][item_card_group]['mblog']['user']['screen_name']
                    content_result = item_list[0]['card_group'][item_card_group]['mblog']['text']
                    item['weibo_content'] = content_select.sub("",content_result)
                    item['weibo_device'] = item_list[0]['card_group'][item_card_group]['mblog']['source']
                    item['weibo_time'] = item_list[0]['card_group'][item_card_group]['mblog']['created_at']
                    item['weibo_forward'] = str(item_list[0]['card_group'][item_card_group]['mblog']['reposts_count'])
                    item['weibo_yes'] = str(item_list[0]['card_group'][item_card_group]['mblog']['attitudes_count'])
                    redis_item['item']=item
                    yield redis_item
                except:
                    pass

        #第二种方法，页面解析
        # weibo_select = response.xpath('//div[@class="card-main"]')
        # for item in weibo_select:
        #     item_weibo = SinaWeiboItem()
        #     if len(item.xpath('header/div[@class="m-box-col m-box-dir m-box-center"]/div/a/h3/text()').extract()) == 0:
        #         item_weibo['nick_name'] = "无昵称"
        #     else:
        #         item_weibo['nick_name'] = item.xpath('header/div[@class="m-box-col m-box-dir m-box-center"]/div/a/h3/text()').extract()[0].strip()
        #     if len(item.xpath('article/div[@class="weibo-og"]/div[@class="weibo-text"]/text()').extract()) == 0:
        #         item_weibo['weibo_content'] = "微博无内容"
        #     else:
        #         item_weibo['weibo_content'] = item.xpath('article/div[@class="weibo-og"]/div[@class="weibo-text"]/text()').extract()[0]
        #     if len(item.xpath('header/div[@class="m-box-col m-box-dir m-box-center"]/div/h4/span[@class="from"]/text()').extract()) == 0:
        #         item_weibo['weibo_device'] = "微博网页"
        #     else:
        #         item_weibo['weibo_device'] = item.xpath('header/div[@class="m-box-col m-box-dir m-box-center"]/div/h4/span[@class="from"]/text()').extract()[0]
        #     if len(item.xpath('header/div[@class="m-box-col m-box-dir m-box-center"]/div/h4/span[@class="time"]/text()').extract()) == 0:
        #         item_weibo['weibo_time'] = "无时间项"
        #     else:
        #         item_weibo['weibo_time'] = item.xpath('header/div[@class="m-box-col m-box-dir m-box-center"]/div/h4/span[@class="time"]/text()').extract()[0]
        #     if len(item.xpath('footer/div[1]/h4/text()').extract()) == 0:
        #         item_weibo['weibo_forward'] = "无转发项"
        #     else:
        #         item_weibo['weibo_forward'] = item.xpath('footer/div[1]/h4/text()').extract()[0]
        #     if len(item.xpath('footer/div[3]/h4/text()').extract()) == 0:
        #         item_weibo['weibo_yes'] = "无点赞项"
        #     else:
        #         item_weibo['weibo_yes'] = item.xpath('footer/div[3]/h4/text()').extract()[0]

            #将数据提交给管道
            # yield item_weibo

