import scrapy


class MercadolivreSpiderSpider(scrapy.Spider):
    name = 'mercadolivre_spider'
    start_urls = "https://lista.mercadolivre.com.br/informatica/componentes-pc/processadores/"

    def start_requests(self):


    def parse(self, response):
        pass
