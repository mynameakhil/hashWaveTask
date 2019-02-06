import scrapy

class SpiderTask(scrapy.Spider):
    name ='event'
    start_urls=[
        'https://allevents.in/events#'
    ]

    def parse(self,response):
        for h3 in response.xpath('//h3//text()').extract():
            yield{'events':h3}