import scrapy
from douban_spider.items import DoubanSpiderItem

class Douban250SpiderSpider(scrapy.Spider):
    # 这是爬虫的名字
    name = 'douban_250_spider'
    # 允许的域名
    allowed_domains = ['movie.douban.com']
    # 入口url，扔给调度器
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        # print(response.text)
        movie_list = response.xpath('//div[@id="content"]//ol/li')
        print("电影个数", len(movie_list))
        for i_item in movie_list:
            doubanSpiderItem = DoubanSpiderItem()
            # serial_number = i_item.xpath()
            # 序号
            doubanSpiderItem['serial_number'] = i_item.xpath('./div[@class="item"]/div[@class="pic"]/em/text()').extract_first()

            # 电影名
            doubanSpiderItem['movie_name'] = i_item.xpath('./div[@class="item"]/div[@class="info"]/div[@class="hd"]/a/span[1]/text()').extract_first()

            # 电影介绍
            content = i_item.xpath('.//div[@class="bd"]/p[1]/text()').extract()
            for i_content in content:
                doubanSpiderItem['introduce'] = "".join(i_content.split())

            # 电影评价

            # 电影描述

            # 电影星级
            print(doubanSpiderItem)
            # 不进行yield 无法进入pipline
            yield doubanSpiderItem

        # 解析下一页
        next_link = response.xpath('//span[@class="next"]/link/@href').extract()
        if next_link:
            # 进行回调
            next_link = next_link[0]
            # https://movie.douban.com/top250
            # next_link= ?start=175&filter=
            yield scrapy.Request('https://movie.douban.com/top250'+next_link, callback=self.parse)
