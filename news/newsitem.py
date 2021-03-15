
class NewsItem:

    def __init__(self, 
        date=None, source=None, url=None, img=None, title=None, summary=None, category=None, author=None):
        self.date = date
        self.source = source
        self.url = url
        self.img = img
        self.title = title
        self.summary = summary
        self.category = category
        self.author = author

    def getItem(self):
        return {
            "date" = self.date,
            "source" = self.source,
            "url" = self.url,
            "img" = self.img,
            "title" = self.title,
            "summary" = self.summary,
            "category" = self.category,
            "author" = self.author
        }

    def setDate(self, date):
        self.date = date
    
    def getDate(self):
        return self.date
    
    def setSource(self, source):
        self.source = source
    
    def getSource(self):
        return self.source
    
    def setUrl(self, url):
        self.url = url
    
    def getUrl(self):
        return self.url
    
    def setImg(self, img):
        self.img = img
    
    def getImg(self):
        return self.img
    
    def setTitle(self, title):
        self.title = title
    
    def getTitle(self):
        return self.title
    
    def setSummary(self, summary):
        self.summary = summary
    
    def getSummary(self):
        return self.summary
    
    def setCategory(self, category):
        self.category = category
    
    def getCategory(self):
        return self.category