# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item,Field


class BetScrapyItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # project use fields
    company = Field()
    match_id = Field()
    match_level = Field()
    match_type = Field()
    date = Field()
    time = Field()
    home_team = Field()
    away_team = Field()
    home_win_begin = Field()
    draw_begin = Field()
    away_win_begin = Field()
    home_win_end = Field()
    draw_end = Field()
    away_win_end = Field()
    home_win_per_begin = Field()
    draw_per_begin = Field()
    away_win_per_begin = Field()
    rebate_per_begin = Field()
    home_win_per_end = Field()
    draw_per_end = Field()
    away_win_per_end = Field()
    rebate_per_end = Field()
    asia_bit_begin = Field()
    asia_up_begin = Field()
    asia_down_begin = Field()
    asia_bit_end = Field()
    asia_up_end = Field()
    asia_down_end = Field()
    result = Field()
    half = Field()
    finish = Field()
    half_result = Field()
    finish_result = Field()
    asia_result = Field()
    inserttime = Field()
    match_status = Field()
    # log fields
    url = Field()   # response.url
    project = Field()   # self.settings.get('BOT_NAME')
    spider = Field()    # self.name
    server = Field()    # socket.gethostname()
    date = Field()  # datetime.datetime.now()
