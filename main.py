#import requests
#from bs4 import BeautifulSoup
import csv
import scrapy

class BotSpider(scrapy.Spider):
     name = 'bot'
#     allowed_domains = ['https://socks-proxy.net/']
     start_urls = ['http://socks-proxy.net//']

     def parse(self, response):
         for row in response.xpath('//*[@class="table table-striped table-bordered"]//tbody//tr'):
            yield {
                    "proto" :       row.xpath('td[5]//text()').extract_first(),
                    "IP"    :       row.xpath('td[1]//text()').extract_first(),
                    "PORT"  :       row.xpath('td[2]//text()').extract_first(),
                    }

