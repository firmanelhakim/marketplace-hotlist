# -*- coding: utf-8 -*-
import scrapy


class TokopediaSpider(scrapy.Spider):
    name = 'tokopedia'
    allowed_domains = ['tokopedia.com']
    start_urls = ['http://tokopedia.com/']

    def parse(self, response):
        pass
