# -*- coding: utf-8 -*-
#请注意使用
import scrapy,re,os
import pkgutil
from mySpider.items import mySpiderItem
from scrapinghub import ScrapinghubClient
from contextlib import closing

project_id = '380804'
apikey = '8539b30bdb8f49a4814b12435fa343f0'
client = ScrapinghubClient(apikey)
store = client.get_project(project_id).collections.get_store('mystuff')

class StockinfoSpider(scrapy.Spider):
    name = 'stockInfo'
    allowed_domains = ['163.com']
    data = pkgutil.get_data("mySpider", "resources/codes.txt")
    data = data.decode()
    codes = data.split("\r\n")
    start_urls = [ r"http://quotes.money.163.com/f10/gszl_" + code +  ".html#01f02"   for code in codes]


    def parse(self, response):
        company = re.findall("[0-9]{6}",response.url)[0]
        with closing(store.create_writer()) as writer:
            writer.write({
                '_key': company, 
                'body': response.body}
            ) 




