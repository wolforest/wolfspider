import scrapy

from pywolf.lang import fileutils


class GdpSpider(scrapy.Spider):
    name = "gdp"

    def start_requests(self):
        urls = [
            'https://quotes.toscrape.com/page/1/',
            'https://quotes.toscrape.com/page/2/',
            'https://quotes.toscrape.com/page/3/',
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split('/')[-2]
        file_path = '/Users/wingle/code/github/wolfspider/data'
        filename = f'{file_path}/hello-{page}.html'

        fileutils.write_contents(filename, response.body)
