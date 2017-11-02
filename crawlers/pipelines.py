# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class CrawlersPipeline(object):
    def process_item(self, item, spider):
        print("获取到数据，正在处理")
        with open("data","a") as f:
            t = [i for i in item.values()]
            f.write(''.join(t))
            f.write("\n")
            print("成功g--------------------------------------")

        return item
