# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class ChinaairItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    """
    首先明确抓取目标，包括城市，日期，指标的值
    """
    # 城市
    city = scrapy.Field()
    # 日期
    date = scrapy.Field()
    # 空气质量指数
    AQI = scrapy.Field()
    # 空气质量等级
    level = scrapy.Field()
    # pm2.5的值
    PM2_5 = scrapy.Field()
    # pm10
    PM10 = scrapy.Field()
    # 二氧化硫
    SO2 = scrapy.Field()
    # 一氧化碳
    CO = scrapy.Field()
    # 二氧化氮
    NO2 = scrapy.Field()
    # 臭氧浓度
    O3_8h = scrapy.Field()

    # 数据源(数据来源)
    source = scrapy.Field()
    # 抓取时间
    utc_time = scrapy.Field()
