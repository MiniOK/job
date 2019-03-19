# -*- coding: utf-8 -*-
import pymysql
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class JobPipeline(object):
    def __init__(self):
        # 建立数据库连接
        self.connect = pymysql.connect(
            host="localhost", # 数据库地址
            port=3306,  # 数据库端口
            db='jobdb',  # 数据库名
            user="root",  # 用户名
            passwd="",  # 密码
            charset="utf8",  # 编码方式，如果不注意就会乱码
            use_unicode=True,
        )
        # 创建操作游标
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        self.cursor.execute(
            """insert into 51job(name,title,site,wage,expert,edu)
            values (%s,%s,%s,%s,%s,%s)""",
            (
                item["name"],
                item["title"],
                item["site"],
                item["wage"],
                item["expert"],
                item["edu"],
            )
        )

        # 提交sql语句
        self.connect.commit()
        return item


