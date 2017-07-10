# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SinaWeiboItem(scrapy.Item):
    key_word = scrapy.Field()
    nick_name = scrapy.Field()
    weibo_content = scrapy.Field()
    weibo_device = scrapy.Field()
    weibo_time = scrapy.Field()
    weibo_forward = scrapy.Field()
    weibo_yes = scrapy.Field()
