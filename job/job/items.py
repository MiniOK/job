# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JobItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 定义爬取的字段
    name = scrapy.Field()  # 公司名
    title = scrapy.Field()  # 岗位名
    site = scrapy.Field()  # 地点
    wage = scrapy.Field()  # 工资
    expert = scrapy.Field()  # 经验
    edu = scrapy.Field()  # 受教育程度

