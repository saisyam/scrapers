import scrapy
from scrapy.http.request import Request

class NykaaSpider(scrapy.Spider):
    name = "nykaa"

    def start_requests(self):
        url = getattr(self, 'url', 'https://www.nykaa.com/brands/lakme/c/604')
        urls = [
            url,
        ]   
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse_product(self, response):
        title = response.css("div.product-des__details-title h1::text").get()
        price_meta = response.css("div.price-info meta")
        price = price_meta[0].attrib['content']
        currency = price_meta[1].attrib['content']
        url_items = response.request.url.split("/p/")
        review_link = url_items[0]+"/reviews/"+url_items[1]+"?ptype=reviews&skuId="+url_items[1]
        yield {
            'url' : response.request.url,
            'title': title,
            'price': price,
            'currency': currency,
            'review_link': review_link,
        }
    def parse(self, response):
        main_div = response.css("div.main-product-listing-page")
        list_div = main_div.css("div.desktop")
        for item in list_div.css("div.card-wrapper-container"):
            atag = item.css("div.product-list-box a")
            link = "https://nykaa.com"+atag.attrib['href']
            yield Request(url = link, callback=self.parse_product, priority=1)