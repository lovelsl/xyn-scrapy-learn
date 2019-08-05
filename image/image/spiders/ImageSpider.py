#coding=utf-8

import os
import scrapy

from  ..items import ImageItem

FILENAME = "url.txt"

class ImageSpider(scrapy.Spider):
    name = "image"

    def _getRootPath(self):
        comroot = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        return comroot

    def _readUrlFromFile(self):
        comroot = self._getRootPath()
        urltxt = os.path.join(comroot, FILENAME)
        with open(urltxt, 'r') as f:
            line = f.readline()
            while line:
                yield line
                line = f.readline()

    def start_requests(self):
        """
        配置 start_requests后start_urls不必使用了，url全部从这里获取
        spider启动后，仅仅调用一次
        :return:
        """
        for u in self._readUrlFromFile():
            url = u
            if url != None and url != '':
                yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        """
        xpath 的绝对路径定位法
        :param response:
        :return:
        """

        #第一个for循环获取本网页种所有的图片
        imagepath = "//img[@src]"
        selector = response.xpath(imagepath)
        for sub in selector:
            jpgurl = sub.xpath('@src').extract()
            imageitem = ImageItem()
            imageitem["url"] = jpgurl
            yield imageitem

        #第二个for循环，打开本页面的子页面，形成递归打开页面
        subpath = "//a[@href]"
        selector = response.xpath(subpath)
        for sub in selector:
            item = sub.get()
            suburl = sub.xpath('@href').extract()[0]
            yield scrapy.Request(suburl, callback=self.parse)
