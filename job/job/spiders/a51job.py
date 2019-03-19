# -*- coding: utf-8 -*-
import scrapy
from job.items import JobItem

class A51jobSpider(scrapy.Spider):
    name = '51job'
    allowed_domains = ['zhipin.com']
    start_urls = ['https://www.zhipin.com/c101010100/?query=python&page=1']

    def parse(self, response):
        body = response.css(".job-primary")
        for head in body:
            item = JobItem()
            item["title"] = head.css(".job-title::text").extract()[0]
            item["wage"] = head.css(".red::text").extract()[0]
            item["site"] = head.css(".info-primary p::text").extract()[0]
            item["name"] = head.css(".company-text .name a::text").extract()[0]
            item["expert"] = head.css(".info-primary p::text").extract()[1]
            item["edu"] = head.css(".info-primary p::text").extract()[2]
            yield item

        # 翻页
        next_page = response.css(".page .next::attr(href)").extract()[0]
        if next_page is not None:
            yield response.follow("https://www.zhipin.com" + next_page,callback=self.parse)






