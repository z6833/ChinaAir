# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from datetime import datetime

class ChinaAirPipeline(object):
    def process_item(self, item, spider):
        item["source"] = spider.name
        item['utc_time'] = str(datetime.utcnow())
        return item

class ChinaAirJsonPipeline(object):
    def open_spider(self, spider):
        self.file = open('air.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        content = json.dumps(dict(item), ensure_ascii=False) + '\n'
        self.file.write(content)

    def close_spider(self, spider):
        self.file.close()