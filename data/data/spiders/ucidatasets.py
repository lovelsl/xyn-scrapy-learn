#coding=utf-8

import os
import scrapy

from data.items import DataItem

FILENAME = "url.txt"

class UciDatasetsSpider(scrapy.Spider):
    name = "ucidatasets"
    #start_urls = [
    #    'http://archive.ics.uci.edu/ml/datasets.php'
    #]

    def _getRootPath(self):
        comroot = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        return comroot

    def _readUrlFromFile(self):
        comroot = self._getRootPath()
        urltxt = os.path.join(comroot,FILENAME)
        with open(urltxt,'r') as f:
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
            if url!= None and url != '':
                yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        """
        xpath 的绝对路径定位法
        :param response:
        :return:
        """
        #self._getNewFile( )
        xpath = "//p//b//a//@href"
        subSelector = response.xpath(xpath)
        #print subSelector
        for sub in subSelector:
            item = sub.get()
            """
           get  一次返回一个，
           getall  一次返回全部
           如： subSelector.getall()  则返回所有的
                 subSelector.get（）  一次返回一个 
           """
            itemstr = item
            url =  'http://archive.ics.uci.edu/ml/' + itemstr

            yield scrapy.Request( url, callback=self.parse_datasets)

    def parse_datasets(self, response):
        xpath = "//td[1]/p[1]/span[2]/a[1]/@href"
        subSelector = response.xpath(xpath)
        preurl = "http://archive.ics.uci.edu/ml"
        for sub in subSelector:
            item = sub.get()
            url = preurl + item.replace("..","")
            ditem = DataItem()
            ditem["tmpurl"] = url
            yield scrapy.Request(url, meta={"dataitem":ditem}, callback=self.parse_downloads)

    def parse_downloads(self, response):
        ditem = response.meta["dataitem"]
        baseurl = ditem["tmpurl"]
        xpath = "//ul/li[3]/a/@href"
        subSelector = response.xpath(xpath)
        for sub in subSelector:
            item = sub.get()
            url = baseurl + item
            ditem["file_urls"] = url
            yield ditem

    def _downloadFile(self):
        comroot = self._getRootPath()





