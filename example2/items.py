# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BookItem(scrapy.Item):

    name=scrapy.Field()
    price=scrapy.Field()

#爬取文件的Item
class ExampleItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    file_urls=scrapy.Field()
    files=scrapy.Field()

