#-*- coding:utf-8 -*-

import scrapy
from scrapy.linkextractors import  LinkExtractor
from scrapy import Request
from scrapy import FormRequest
#这里是登录验证爬取程序，没有验证码
class LoginSpider(scrapy.Spider):

    name='login'
    allowed_domains=['example.webscraping.com']
    start_urls=['http://example.webscraping.com/user/profile']

    def parse(self, response):
        #解析登陆成功之后的页面，此处页面是用户的个人信息页面
        keys=response.css('table label::text').re('(.+):')
        values=response.css('table td.w2p_fw::text').extract()
        yield  dict(zip(keys,values))


    #下面是登录

    login_url='http://example.webscraping.com/places/default/user/login?_next=/places/default/index'

    #这是继承基类的登录页面
    def start_requests(self):
        yield Request(self.login_url,callback=self.login)

    def login(self,response):
        #登录页面的解析函数，构造FormRequest对象的提交表单
        fd={'email':'wuyongyu13@126.com','password':'wuyongyu13'}
        yield FormRequest.from_response(response,formdata=fd,callback=self.parse_login)

    def parse_login(self,response):
        if 'Welcome' in response.text:
            print u"############登录成功########################"
            #yield from  super().start_requests()
