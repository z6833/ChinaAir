# -*- coding: utf-8 -*-
import scrapy
from ChinaAir.items import ChinaairItem

class AirchinaSpider(scrapy.Spider):
    name = 'airChina'
    allowed_domains = ['aqistudy.cn']
    base_url = "https://www.aqistudy.cn/historydata/"
    # 抓取首页
    start_urls = [base_url]

    def parse(self, response):

        # 拿到页面的所有城市名称链接
        url_list = response.xpath('//div[@class="all"]/div[@class="bottom"]//a/@href').extract()[:1]
        # 拿到页面的所有城市名
        city_list = response.xpath('//div[@class="all"]/div[@class="bottom"]//a/text()').extract()[:1]

        # 将城市名及其对应的链接，进行一一对应
        for city, url in zip(city_list, url_list):

            # 拼接该城市的链接
            link = self.base_url + url
            yield scrapy.Request(url=link, callback=self.parse_month, meta={"city": city})

    def parse_month(self, response):
        """
        拿到每个城市的，每个月份的数据
        此页面为动态页面，这里利用selenium结合浏览器获取动态数据
        因此在下载中间件中添加中间件代码
        :param response:
        :return:
        """
        # 获取城市每个月份的链接
        url_list = response.xpath('//tr/td/a/@href').extract()[:1]

        for url in url_list:
            url = self.base_url + url  # 构造该url
            yield scrapy.Request(url=url, meta={'city': response.meta['city']}, callback=self.parse_day)

    def parse_day(self, response):
        """
        获取每一天的数据
        :param response:
        :return:
        """
        node_list = response.xpath('//tr')

        node_list.pop(0)
        for node in node_list:
            # 解析目标数据
            item = ChinaairItem()
            item['city'] = response.meta['city']
            item['date'] = node.xpath('./td[1]/text()').extract_first()
            item['AQI'] = node.xpath('./td[2]/text()').extract_first()
            item['level'] = node.xpath('./td[3]/text()').extract_first()
            item['PM2_5'] = node.xpath('./td[4]/text()').extract_first()
            item['PM10'] = node.xpath('./td[5]/text()').extract_first()
            item['SO2'] = node.xpath('./td[6]/text()').extract_first()
            item['CO'] = node.xpath('./td[7]/text()').extract_first()
            item['NO2'] = node.xpath('./td[8]/text()').extract_first()
            item['O3_8h'] = node.xpath('./td[9]/text()').extract_first()
            yield item
