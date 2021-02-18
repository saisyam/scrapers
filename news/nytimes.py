import requests
import unicodedata
from bs4 import BeautifulSoup
from datetime import datetime


headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
}

class NYTimes:
    def __init__(self, section):
        self.url = "https://www.nytimes.com/section/"+section
    
    def scrape_highlights(self):
        response = requests.get(self.url, headers=headers)
        html = ""
        post = {}
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html5lib")
            section = soup.find("section", {"id": "collection-highlights-container"})
            articles = section.find_all("article")
            for item in articles:
                post['title'] = item.find("h2").text
                post_url = item.find("h2").find("a")['href']
                url_items = post_url.split("/")
                if "live" in post_url:
                    post['date'] = url_items[4]+"-"+url_items[5]+"-"+url_items[6]
                    post['link'] = post_url
                else:
                    post['date'] = url_items[1]+"-"+url_items[2]+"-"+url_items[3]
                    post['link'] = "https://www.nytimes.com"+ post_url
                ptags = item.find_all("p")
                post['summary'] = ptags[0].text
                spans = ptags[1].find_all("span")
                post['by'] = ''
                if len(spans) > 1:
                    post['by'] = unicodedata.normalize("NFKD", spans[2].text.replace("By", '').strip())
                yield post


# Getting posts related to politics and Business
'''
nyt = NYTimes("politics")
for post in nyt.scrape_highlights():
    print(post)

nyt = NYTimes("business")
for post in nyt.scrape_highlights():
    print(post)
'''