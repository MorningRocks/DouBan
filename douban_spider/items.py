# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 序号
    serial_number = scrapy.Field()
    # 电影名
    movie_name = scrapy.Field()
    # 电影介绍
    introduce = scrapy.Field()

    # 电影评价
    evalute = scrapy.Field()

    # 电影描述
    describe = scrapy.Field()
    # 电影星级
    star = scrapy.Field()

