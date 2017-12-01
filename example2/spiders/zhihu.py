#-*- coding:utf-8 -*-
import scrapy
from scrapy.linkextractors import  LinkExtractor
from scrapy import Request
from scrapy import FormRequest
class zhihuSpider(scrapy.Spider):
    name = 'zhihu'
    start_url = ['https://www.zhihu.com']

    def start_requests(self):  # 登陆
        print '******************************************'
        yield scrapy.Request('https://www.zhihu.com', meta={'cookiejar':'chrome'},callback=self.onetwo)
        print 'ffffffffff'
    def onetwo(self, response):
        print '####################################info###########'
        #print response.body
        print response.xpath('.//*[@id="root"]/div/main/div/div/div[1]/div[2]/div/div[1]/div/div[3]').extract()