# -*- coding: utf-8 -*-
import time
import scrapy
from scrapy_redis import get_redis
from scrapy.conf import settings


class AlistSpider(scrapy.Spider):
    name = "alist"
    allowed_domains = ["192.168.10.56"]


    def __init__(self, *args, **kwargs):
        super(AlistSpider, self).__init__(*args, **kwargs)
        self.conn = get_redis(url=settings.get('REDIS_URL'))


    def start_requests(self):
        url = 'http://192.168.10.56/house_i33.htm'
        while True:
            if self.conn.llen('a56:start_urls') > 5000:
                time.sleep(1)
            else:
                yield scrapy.Request(url, dont_filter=True)

    def parse(self, response):
        lst = response.css('.houseList dl')
        for sel in lst:
            href = sel.xpath('dd/p[1]/a/@href').extract_first()
            source_url = response.urljoin(href)
            source_url = 'http://192.168.10.56/1.htm'
            self.conn.lpush('a56:start_urls', source_url)
