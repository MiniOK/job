#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import scrapy

class mingyan(scrapy.Spider): # 需要继承scrapy.Spider类

    name = 'mingyan2' # 定义蜘蛛的名字

    def start_requests(self):  # 由此方法通过下面连接爬取页面

        # 定义爬取的链接
        urls = [
            'http://lab.scrapyd.cn/page/1/',
            'http://lab.scrapyd.cn/page/2/'
        ]

        for url in urls:
            yield scrapy.Request(url=url ,callback=self.parse)

    def parse(self, response):
        """
        x这个例子只是看看爬虫运行的流程：
        1、定义链接
        2、通过链接爬去（下载）页面
        3、定义规则，然后提取数据
        :param response:
        :return:
        """
        page = response.url.split("/")[-2] # 根据连接提取分页
        filename = 'mignyan - %s.html'% page # 拼接文件名
        with open(filename,'wb') as f:
            f.write(response.body)  # response.body就代表刚才的页面
        self.log('保存文件： %s' % filename)
