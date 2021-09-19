import scrapy


class BillboardSpider(scrapy.Spider):
    name = 'billboard'
    allowed_domains = ['https://www.billboard.com/charts/billboard-200']
    start_urls = ['http://https://www.billboard.com/charts/billboard-200/']

    def parse(self, response):
        pass
