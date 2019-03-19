# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Mingyan2Item(scrapy.Item):
    # 定义要爬取的字段
    name = scrapy.Field()  # 公司名
    title = scrapy.Field()  # 岗位名
    site = scrapy.Field()  # 地点
    wage = scrapy.Field()  # 工资
    expert = scrapy.Field()  # 经验 experience
    edu = scrapy.Field()  # 学历 education background