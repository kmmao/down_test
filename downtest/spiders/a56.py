# -*- coding: utf-8 -*-
from scrapy_redis.spiders import RedisSpider


class A56Spider(RedisSpider):
    name = "a56"
    allowed_domains = ["192.168.10.56"]
    ID = 0

    def parse(self, response):
        self.ID += 1
        self.logger.debug(self.ID)
        self.logger.debug(len(response.body))
        with open('www/{}.htm'.format(self.ID), 'w') as f:
            f.write(response.body)
