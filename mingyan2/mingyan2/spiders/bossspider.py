# -*- coding: utf-8 -*-

import scrapy
from mingyan2.items import Mingyan2Item
from urllib import parse


class JobSpider(scrapy.Spider):
    name = 'job'
    allowed_domains = ['www.zhipin.com']
    # xx = parse.unquote("%E7%88%AC%E8%99%AB") # 解码为爬虫二字
    # start_urls = ['https://www.zhipin.com/c101010100/?query=python'+x
    # x+'&page=1']
    start_urls = ['https://www.zhipin.com/c101010100/?query=go&page=1']

    def parse(self, response):
        body = response.css(".job-primary")
        for head in body:
            item = Mingyan2Item()
            item["title"] = head.css(".job-title::text").extract()[0]
            item["wage"] = head.css(".red::text").extract()[0]
            item['site'] = head.css(".info-primary p::text").extract_first().strip()
            item['name'] = head.css(".company-text .name a::text").extract_first()
            item['expert'] = head.css(".info-primary p::text").extract()[1].strip()
            item['edu'] = head.css(".info-primary p::text").extract()[2].strip()
            yield item
        # 翻页
        next_page = response.css(".page .next::attr(href)").extract()[0]
        if next_page is not None:
            yield response.follow('https://www.zhipin.com' + next_page, callback=self.parse)  # 从上图中可以看的出链接并不完全，需要我们补充。














