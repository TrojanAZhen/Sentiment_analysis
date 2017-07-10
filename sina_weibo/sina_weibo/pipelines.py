# -*- coding: utf-8 -*-
import json
import redis

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class SinaWeiboPipeline(object):
    def __init__(self):
        self.file = open('weibo.json','w')

    def process_item(self, item, spider):
        content = json.dumps(dict(item),ensure_ascii=False)+",\n"
        self.file.write(content)
        return item

    def close_spider(self,spider):
        self.file.close()

class SinaWeibo_redis_Pipeline(object):
    def open_spider(self,spider):
        self.redis_cli = redis.Redis(host = "127.0.0.1",port = 6379)

    def process_item(self,item,spider):
        content = json.dumps(dict(item),ensure_ascii=False)
        self.redis_cli.lpush("sina_weibo",content)
        return item
