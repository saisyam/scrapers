# scrapers
Scrapers built using Python

## NYTimes Scrapper
[This](https://github.com/saisyam/scrapers/blob/main/news/nytimes.py) scraper extracts news from https://www.nytimes.com website. Currently it pulls highligts of the given section and top 10 latest news items. The below example pulls highlights from `politics` and `business` sections.

```python
nyt = NYTimes("politics")
html = nyt.gethtml()
if html is not None:
    for post in nyt.scrape_latest(html):
        print(post)

nyt = NYTimes("business")
html = nyt.gethtml()
if html is not None:
    for post in nyt.scrape_latest(html):
        print(post)
```

# DISCLAIMER
These scrapers are for educational or research purposes only. Any commerical use of this code is not entertained or recommended.

