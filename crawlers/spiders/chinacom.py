# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class ChinacomSpider(CrawlSpider):
    name = 'chinacom'
    allowed_domains = ['china.com.cn']
    start_urls = ['http://china.com.cn/']

    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )



    def __init__(self):
        url_t = "http://www.china.com.cn/news/weather/node_5863791_%s.htm"

        self.start_urls = [url_t % str(i) for i in range(10000)]
        print(self.start_urls)

    def parse_item(self, response):
        i = {}
        # i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        # i['name'] = response.xpath('//div[@id="name"]').extract()
        # i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
