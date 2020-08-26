# -*- coding: utf-8 -*-
import scrapy


class SmzdmSpider(scrapy.Spider):
    name = 'smzdm'
    allowed_domains = ['smzdm.com']
    start_urls = ['http://smzdm.com/']

    def parse(self, response):
        pass
