#-*- coding:utf-8 -*-

#爬取html 文本信息
import scrapy
class BooksSpider(scrapy.Spider):
    #每一个爬虫的唯一标识,告诉scrapy 使用哪个spider进行爬取
    name = "books"

    allowed_domains=["books.toscrape.com"]
    #定义爬虫的爬取的起始点，起始点可以是多个，这里只有一个,由Spider内部函数start_request进行调用
    start_urls=['http://books.toscrape.com/']

    def parse(self,resposne):
        #提取数据
        #每一本书的信息在<article claoss="product_pod">中，我们使用css()方法找到所有的article元素，并以此迭代
        for book in resposne.css('article.product_pod'):
            #书名的信息在 article >h3  >a 元素的title  属性里面
            name=book.xpath('./h3/a/@title').extract_first()

            #书价的信息在 <p class="price_color">的Text里面
            price=book.css('p.price_color::text').extract_first()

            yield {
                'name':name,
                'price':price
            }

            #提取链接
            #下去一页的链接在 ul.paper > li.next > a里面8
            #找到的url  为 catalogue/page-2.html
            next_url=resposne.css('ul.paper li.next a::attr(href)').extract_first()

            if next_url:
                #如果找到下一页的URL,得到的是绝对路径，构造新的Request 对象
                next_url=resposne.urljoin(next_url)
                yield scrapy.Request(next_url,callback=self.parse)