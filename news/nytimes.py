import sys
sys.path.append("../")

from bs4 import BeautifulSoup
import unicodedata
from utils import htmlutils
from utils.base import BaseScraper

class NYTimes(BaseScraper):
    name = "nytimes"

    def __init__(self, url, category):
        self.category = category
        super().__init__(url) 
        
    def scrape(self):
        html = htmlutils.get_html(self.url)
        if html == None:
            return {}
        self.soup = BeautifulSoup(html, "html5lib")
        return self.scrape_highlights()

    def scrape_highlights(self):
        articles = self.soup.findAll("article")
        for item in articles:
            title = item.find("h2").find("a").get_text()
            url = "https://www.nytimes.com"+item.find("h2").find("a")['href']
            items = url.split("/")
            date = items[3]+"-"+items[4]+"-"+items[5]
            summary = item.findAll("p")[0].get_text()
            author = item.findAll("p")[1].find("span",{"itemprop":"name"}).get_text()
            author = unicodedata.normalize("NFKD", author).strip()
            yield {
                "title": title,
                "url": url,
                "date": date,
                "summary": summary,
                "author": author,
                "category": self.category,
                "source": "nytimes"
            }


arguments = len(sys.argv)
if arguments < 3:
    print("Usage: python3 nytimes.py <URL> <Category>")
    exit()
else:
    nyt = NYTimes(sys.argv[1], sys.argv[2])
    for i in nyt.scrape():
        print(i)