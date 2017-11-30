# -*-coding:utf-8 -*-

import scrapy

from ..items import BookItem

from scrapy.linkextractors import LinkExtractor
class BooksSpider(scrapy.Spider):

    name = "books"

    allowed_domains=['books.toscrape.com']
    start_urls=['http://books.toscrape.com/']

    def parse(self, response):
        le=LinkExtractor(restrict_css='article.product_pod h3')
        for link in le.extract_links(response):
            yield scrapy.Request(link.url,callback=self.parse_book)

        le =LinkExtractor(restrict_css='url.pager li.next')
        links=le.extract_links(response)

        if links:
            next_url=links[0].url
            yield scrapy.Request(next_url,callback=self.parse)



    def parse_book(self,response):
        book=BookItem()

        sel=response.css('div.product_main')
        book['name']=sel.xpath('./h1/text()').extract_first()
        book['price']=sel.css('p.price_color::text').extract_first()
        book['review_rating']=sel.css('p.star-rating::attr(class)').re_first('star-rating ([A-Za-z]+)')

        sel=response.css('table.table.table-striped')  #含有两个class属性
        book['upc']=sel.xpath('(.//tr)[1]/td/text()').extract_first()
        book['stock']=sel.xpath('(.//tr)[6]/td/text()').re('\((\d+) available')
        book['review_num']=sel.xpath('(.//tr)[last()]/td/text()').extract_first()

        yield book


