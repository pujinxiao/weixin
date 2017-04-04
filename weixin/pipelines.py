# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import re
class WeixinPipeline(object):
    def process_item(self, item, spider):
        for i in range(len(item['title'])):
            html=item['title'][i]
            reg=re.compile(r'<[^>]+>') #去html标签
            title=reg.sub('',html)
            print title
            print item['link'][i]
            html_1=item['dec'][i]
            reg_1=re.compile(r'<[^>]+>')
            dec=reg_1.sub('',html_1)
            print dec
        return item
