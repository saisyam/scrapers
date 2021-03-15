from bs4 import BeautifulSoup
import requests
import unicodedata

class NYTimes:
    name = "nytimes"

    def __init__(self, url, category):
        self.url = url
        self.category = category
        
    def scrape(self):
        r = requests.get(self.url)
        self.soup = BeautifulSoup(r.text, "html5lib")
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


nyt = NYTimes("https://www.nytimes.com/section/politics")
for i in nyt.scrape():
    print(i)