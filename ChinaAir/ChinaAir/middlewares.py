# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

import random
# 导入User-Agent列表
from ChinaAir.settings import USER_AGENT as ua_list

# class UserAgentMiddlerware(object):
#     """
#     定义一个中间件，给每一个请求随机选择USER_AGENT
#     注意，不要忘了在setting文件中打开DOWNLOADER_MIDDLERWARE的注释
#     """
#     def process_request(self, request, spider):
#
#         # 从ua_list中随机选择一个User-Agent
#         user_agent = random.choice(ua_list)
#         # 给请求添加头信息
#         request.headers['User-Agent'] = user_agent
#         # 当然，也可以添加代理ip，方式如下，此处不用代理，仅说明代理使用方法
#         # request.meta['proxy'] = "..."
#         print(request.headers['User-Agent'])

import time
import scrapy
from selenium import webdriver

class SeleniumMiddlerware(object):
    """
    利用selenium，获取动态页面数据
    """
    def process_request(self, request, spider):

        # 判断请求是否来自第二个页面，只在第二个页面调用浏览器
        if not request.url == "https://www.aqistudy.cn/historydata/":
            # 实例化。selenium结合谷歌浏览器，
            self.driver = webdriver.PhantomJS()
            # 请求
            self.driver.get(request.url)
            time.sleep(2)

            # 获取请求后得到的源码
            html = self.driver.page_source
            # 关闭浏览器
            self.driver.quit()

            # 构造一个请求的结果，将谷歌浏览器访问得到的结果构造成response，并返回给引擎
            response = scrapy.http.HtmlResponse(url=request.url, body=html, request=request, encoding='utf-8')
            return response
