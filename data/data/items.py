# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.pipelines.files import FilesPipeline

# class DataItem(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     tmpurl = scrapy.Field()
#     file_urls = scrapy.Field()
#     file = scrapy.Field()
#     pass

class DataItem(scrapy.Item):#FilesPipeline):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #store_uri = scrapy.Field()
    collection = "ucidata"
    table = "data"
    tmpurl = scrapy.Field()
    file_urls = scrapy.Field()
    file = scrapy.Field()
