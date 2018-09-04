# -*- coding: utf-8 -*-
import scrapy


class OnbetSpider(scrapy.Spider):
    name = 'onBet'
    allowed_domains = ['live.titan007.com']
    start_urls = ['http://live.titan007.com/']

    def parse(self, response):
        pass
