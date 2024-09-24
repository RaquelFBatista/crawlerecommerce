import pdb

import scrapy
from scrapy import Request


class MercadolivreSpiderSpider(scrapy.Spider):
    name = 'mercadolivre_spider'
    base_url = "https://lista.mercadolivre.com.br"
    search_url = "/informatica/componentes-pc/processadores/"
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'DOWNLOAD_DELAY': 2,
        'COOKIES_ENABLED': True
    }

    def start_requests(self):
        url = self.base_url + self.search_url
        yield Request(url=url,
                      callback=self.parse_products_list)

    def parse_products_list(self, response):
        list_products = response.xpath('//div[@class="ui-search-layout--grid__grid"]/div')
        for products in list_products:
            import pdb;pdb.set_trace()
            name = products.xpath ('.//a/text()').get(),
            url = products.xpath ('.//a/@href').get()
            currency = products.xpath('.//div[@class="ui-recommendations-card__price-block"]//span/span[1]/text()').get()
            price = products.xpath('.//div[@class="ui-recommendations-card__price-block"]//span/span[2]/text()').get()

    # continuar


    def next_page (self,response):
        pass
