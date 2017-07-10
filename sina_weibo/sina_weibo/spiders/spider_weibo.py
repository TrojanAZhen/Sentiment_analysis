# -*- coding: utf-8 -*-
import scrapy
import json
from sina_weibo.items import SinaWeiboItem


class SpiderWeiboSpider(scrapy.Spider):
    name = 'spider_weibo'
    allowed_domains = ['weibo.cn']
    start_urls = ['https://passport.weibo.cn/signin/login']

    def parse(self, response):
        response_list = json.loads(response.text)
        for item_list in response_list:
            for item_card_group in range(len(item_list[0]['card_group'])):
                result = item_list[0]['card_group'][item_card_group]['mblog']['text']
                print(result)
        # with open("weibo.html","w") as file:
        #     file.write(response.text)
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


