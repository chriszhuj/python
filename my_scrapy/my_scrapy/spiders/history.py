# -*- coding: utf-8 -*-
import scrapy
import socket
import datetime
from my_scrapy.items import BetScrapyItem
from requests import Request
from scrapy.loader.processors import MapCompose, Join
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Spider, Rule
from scrapy.loader import ItemLoader


class HistorySpider(Spider):
    name = 'history'
    allowed_domains = ['op1.win007.com']
    start_urls = ['http://op1.win007.com/Companyhistory.aspx?id=281&matchdate=2018-06-08']

    def parse(self, response):
        detail_url = response.xpath('//*[contains(@class,"gocheck")]/a/@href').extract()
        for url in detail_url:
            match_id = url[str.rindex(url, "/") + 1:str.rindex(url, ".htm")]
            asia_data_url = "http://vip.win007.com/AsianOdds_n.aspx?id=!matchid&l=0"
            asia_data_url = str.replace(asia_data_url, "!matchid", str(match_id))
            self.log('url is : %s' % asia_data_url)
            yield Request(asia_data_url)

    def parse_item(self, response):
        # define contract to check spider is ok
        # use scrapy check history
        """
        @url http://op1.win007.com/Companyhistory.aspx?id=281
        @returns items 1
        @scrapes match_type
        @scrapes url project spider server date
        """
        item = BetScrapyItem()
        itemLoader = ItemLoader(item=item, response=response)
        # self.log('match_type: %s' % response.xpath('//*[@id="tr_1"]/td[1]/text()').extract())
        # response_arr = response.xpath('//*[contains(@id,"tr_") or contains(@id,"tr2_")]//child::*/text()').extract()
        # self.log('response_arr: %s' % response_arr)
        itemLoader.add_xpath('match_type', '//*[contains(@id,"tr_") or contains(@id,"tr2_")]//child::*/text()')

        itemLoader.add_value('url', response.url)
        itemLoader.add_value('project', self.settings.get('BOT_NAME'))
        itemLoader.add_value('spider', self.name)
        itemLoader.add_value('server', socket.gethostname())
        itemLoader.add_value('date', datetime.datetime.now())
        return itemLoader.load_item()
