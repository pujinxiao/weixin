# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from weixin.items import WeixinItem
class WeixinSpider(scrapy.Spider):
    name = "WeiXin"
    allowed_domains = ["sogou.com"]
    start_urls = ['http://sogou.com/']

    def parse(self, response):
        '''建立循环页'''
        key='python'
        for i in range(1,11):
            url='http://weixin.sogou.com/weixin?query='+key+'&type=2&page='+str(i)
            yield Request(url=url,callback=self.get_content)
    def get_content(self,response):
        '''获取相关信息'''
        item=WeixinItem()
        item['title']=response.xpath('//div[@class="txt-box"]/h3/a').extract() #一页的全部标题,10条包含html标签
        item['link']=response.xpath('//div[@class="txt-box"]/h3/a/@href').extract() #一页的全部标题链接 10条
        item['dec']=response.xpath('//p[@class="txt-info"]').extract() #一页的全部描述,10条包含html标签
        yield item