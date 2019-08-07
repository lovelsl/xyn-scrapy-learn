
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline

class ImagePipeline(ImagesPipeline):


    def file_path(self, request, response=None, info=None):
        item = request.meta.get('item')
        print("item ---------->",item)
        name = item["name"]
        url = request.url
        file_name = url.split("/")[-1]

        path = "./"+name+"/"+file_name
        return path

    def item_completed(self, results, item, info):
        # 获取图片地址path
        # 图片下载完成后，执行该方法
        image_paths = [x["path"] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("图片下载失败！！")
        return item

    def get_media_requests(self, item, info):
        # 获取item文件里的url字段并加入队列等待被调用进行下载图片
        # 这些请求将被管道处理，当它们完成下载后，结果将以2-元素的元组形式传送到item_completed作为results的一部分
        # results=[(success, image_info_or_error),....]
        # success 图片下载成功为True，下载失败为False
        # image_info_or_error  时为一个字典{“url”:"图片下载的url，get_media_requests返回的","path":"图片在本机的存储路径","checksum":"图片内容的MD5 hash"}
        print("get_media_requests-------", item)
        yield scrapy.Request(item["url"], meta={"item": item})