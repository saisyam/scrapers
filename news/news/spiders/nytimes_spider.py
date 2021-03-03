import scrapy

class NYTimesSpider(scrapy.Spider):
    name = "nytimes"

    def start_requests(self):
        urls = [
            "https://www.nytimes.com/section/business",
            "https://www.nytimes.com/section/politics",
        ]   
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        for article in response.css("article"):
            yield {
                'title': article.css("h2 a::text").get(),
                'url': "https://www.nytimes.com"+article.css("h2 a").attrib['href'],
            }
            