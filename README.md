# scrapers
Scrapers built using Python Scrapy

## News Scrapper
[News scraper](https://github.com/saisyam/scrapers/tree/main/news) will scrape news websites.

* [NYTimes](https://github.com/saisyam/scrapers/blob/main/news/news/spiders/nytimes_spider.py) scraper to extract latest news from sections like Politics, Business etc.

## Skincare Products and Reviews Scrapper
[Skincare scraper](https://github.com/saisyam/scrapers/tree/main/skincare) will scrape websites that sell various skincare products.

* [Nykaa](https://github.com/saisyam/scrapers/blob/main/skincare/derma/spiders/nykaa_spider.py) scraper to extract product information and review URL. You can send URL of the brand page as command line argument while running the scraper. If no URL is sent it will take a default URL. For example, the below command will scrape the products related to Biotique.

```shell
~$ scrapy crawl nykaa -a url=https://www.nykaa.com/brands/biotique/c/923
```

# DISCLAIMER
These scrapers are for educational or research purposes only. Any commerical use of this code is not entertained or recommended.

