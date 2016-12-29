# -*- coding: utf-8 -*-
import scrapy


class A56Spider(scrapy.Spider):
    name = "a56"
    allowed_domains = ["192.168.10.56"]
    ID = 0

    def start_requests(self):
        while True:
            yield scrapy.Request('http://192.168.10.56/3_319451102.htm', dont_filter=True)

    def parse(self, response):
        self.ID += 1
        self.logger.debug(self.ID)
        self.logger.debug(len(response.body))
        with open('{}.htm'.format(self.ID), 'w') as f:
            f.write(response.body)
