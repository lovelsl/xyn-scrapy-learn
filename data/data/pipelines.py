# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
import scrapy

import pymongo

class DataPipeline( ):
    def __init__(self, mongodb_url, mongodb_db, mongodb_collection):
        self.mongodb_url = mongodb_url
        self.mongodb_db = mongodb_db
        self.mongodb_collection = mongodb_collection

    @classmethod
    def from_crawler(cls, crawler):
        """
        crawler 提供了访问Scrapy的核心组件的方法  如settings, singals
        也可以用于hook
        获取配置文件中的 MONGODB_DB 与 MONGODB_URL 设置
        :param crawler:
        :return:
        """
        return cls(
            mongodb_url=crawler.settings.get("MONGODB_URL"),
            mongodb_db=crawler.settings.get("MONGODB_DB"),
            mongodb_collection=crawler.settings.get("MONGODB_COLLECTION")
        )

    def open_spider(self, spider):
        """
        爬虫开启时执行的操作  ： 开始与mongodb的连接
        :param spider:
        :return:
        """
        self.client = pymongo.MongoClient(self.mongodb_url)
        self.db = self.client[self.mongodb_db][self.mongodb_collection]

    def process_item(self, item, spider):
        """

        :param item:
        :param spider:
        :return:     返回值为item或者字典类型
                      或者丢出DropItem
        """
        self.db.insert(dict(item))
        return item

    # 关闭爬虫时断开MongoDB数据库连接
    def close_spider(self,spider):
        self.client.close()
