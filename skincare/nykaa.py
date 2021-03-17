import sys
sys.path.append("../")

from bs4 import BeautifulSoup
import unicodedata
from utils import htmlutils
from utils.base import BaseScraper

class Nykaa(BaseScraper):
    name = "nykaa"

    def __init__(self, url, brand):
        self.brand = brand
        super().__init__(url) 
        
    def scrape(self):
        html = htmlutils.get_html_with_js(self.url)
        if html == None:
            return {}      
        self.soup = BeautifulSoup(html, "html5lib")
        return self.scrape_highlights()

    def scrape_highlights(self):
        main_div = self.soup.find('div', {'class':'main-product-listing-page'}).findAll("div", {'class':'card-wrapper-container'})
        for item in main_div:
            prod_tag = item.find('div',{'class':'product-list-box'}).find("a")
            prod_url = prod_tag['href']
            if "https://www.nykaa.com" in prod_url:
                continue
            prod_url = "https://www.nykaa.com"+prod_url
            title = prod_tag.find("div", {'class':'m-content__product-list__title'}).find("h2")['title']
            yield {
                "title": title,
                "url": prod_url,
                "brand": self.brand,
                "source": "nykaa"
            }



nyk = Nykaa("https://www.nykaa.com/brands/biotique/c/923", "Biotique")
for i in nyk.scrape():
    print(i)