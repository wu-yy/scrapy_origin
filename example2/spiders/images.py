#-*- coding:utf-8 -*-

#爬取image.so.com 的图片，并下载图片

import scrapy
from scrapy import Request
import  json


class ImageSpider(scrapy.Spider):

    name = 'images'
    BASE_URL='http://image.so.com/zj?ch=news&sn=%s&listtype=new&temp=1'
    start_index=1

    #下载的最大下载数量，防止磁盘用量过大
    MAX_DOWNLOAD_NUM=50
    start_urls=[BASE_URL% 0]

    def parse(self, response):
        #使用json 解析响应的结果
        infos=json.loads(response.body.decode('utf-8'))
        #提取所有图片的下载url到一个列表，赋值给item的image_urls 字段
        yield {'image_urls':[info['qhimg_url'] for info in infos['list']]}

        #如果count字段大于0 ，并且下载的数量不足MAX_DOWNLOAD_NUM
        self.start_index+=infos['count']
        if infos['count']>0 and self.start_index<self.MAX_DOWNLOAD_NUM:
            yield Request(self.BASE_URL%self.start_index)

