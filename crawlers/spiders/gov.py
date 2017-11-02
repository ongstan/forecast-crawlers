# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class SpiderSpider(CrawlSpider):
    name = 'gov'
    allowed_domains = ['cma.gov.cn']
    start_urls = ['http://www.cma.gov.cn/','http://www.cma.gov.cn/2011xwzx/2011xqxkj/','http://www.cma.gov.cn/2011xwzx/2011xqhbh/','http://www.cma.gov.cn/2011xwzx/2011xfzjz/','http://www.cma.gov.cn/2011xwzx/2011xgzdt/','http://www.cma.gov.cn/2011xwzx/2011xqxxw/2011xqxyw/']

    rules = (
        Rule(LinkExtractor(allow=r'2011xzytq/'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'\.html$'), callback='parse_item'),
    )

    def parse_item(self, response):
        i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()

        # title = scrapy.Field()
        # date = scrapy.Field()
        # classification = scrapy.Field()
        # content = scrapy.Field()
        # source = scrapy.Field()
        # url = scrapy.Field

        print("解析中")

        i['url'] = response.url
        i['title'] = ''.join(response.css('title::text').extract())
        try:
            date_array = response.xpath('//div[@class="news_textspan"]//div//span//text()').extract()
            i['source'] = date_array[0]
            i['date'] = date_array[1]
        except:
            pass
        i['content'] = ''.join(response.css('div.TRS_Editor p::text').extract()).replace("\u3000",'')

        i['url'] = i['url']

        return i
