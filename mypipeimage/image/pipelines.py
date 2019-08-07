# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo

import scrapy
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline

class ImagePipeline(object):
    pass