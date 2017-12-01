# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class Example2Pipeline(object):
    def process_item(self, item, spider):
        return item

#爬取文件，解析文件路径的pipelines
from scrapy.pipelines.files import FilesPipeline

#下面是对下载文件的路径进行解析
import urllib
from os.path import *
from urlparse import urlparse
class MyFilesPipeline(FilesPipeline): #继承自FilesPipeline
    def file_path(self,request,response=None,info=None):
        path=urlparse(request.url).path
        return join(basename(dirname(path)),basename(path))