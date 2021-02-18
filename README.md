# scrapers
Scrapers built using Python

## NYTimes Scrapper
[This](https://github.com/saisyam/scrapers/blob/main/news/nytimes.py) scraper extracts news from https://www.nytimes.com website. Currently it pulls highligts of the given section. The below example pulls highlights from `politics` and `business` sections.

```python
nyt = NYTimes("politics")
for post in nyt.scrape_highlights():
    print(post)
nyt = NYTimes("business")
for post in nyt.scrape_highlights():
    print(post)
```

# DISCLAIMER
These scrapers are for educational or research purposes only. Any commerical use of this code is not entertained or recommended.

