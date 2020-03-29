# -*- coding: utf-8 -*-
import scrapy


class CountriesSpider(scrapy.Spider):
    name = 'countries'
    allowed_domains = ['https://www.worldometers.info/']
    start_urls = ['https://www.worldometers.info/world-population/population-by-country/']

    def parse(self, response):
        # title = response.xpath("//h1//text()").get()
        # countries = response.xpath("//td/a/text()").getall()
        countries = response.xpath("//td/a") 
        for country in countries:
            name  = country.xpath(".//text()").get()
            link  = country.xpath(".//@href").get()

            yield{
                # 'title' : title,
                'name' : name,
                'link' : link
            }
