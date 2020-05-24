import time
import requests
import pymongo


import feedparser

MONGO_HOST = "127.0.0.1"
MONGO_DB = "scrapper"
MONGO_USER = "scrapper"
MONGO_PASS = "dxlejavl"

EXIT_CODE_ERROR = 1
EXIT_CODE_OK = 0

class Scrapper:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
    }
    collect_news = []

    def __init__(self, url):
        self.url = url
        self.news_add = 0
        try:
            self.connect_to_db()
        except Exception as ex:
            print(f"DB problem: {ex}")
            exit(EXIT_CODE_ERROR)


    def running(self):
        self.get_and_parce_rss()
        self.load_news()

        return f"News ADD: {self.news_add}"

    def get_and_parce_rss(self):
        try:
            r = requests.get(self.url, headers=self.headers)
        except Exception as ex:
            print(f'Can`t GET URL: {self.url}, {ex}')
            exit(EXIT_CODE_ERROR)

        d = feedparser.parse(r.text)

        for i, aticle in enumerate(d.entries):
            _data = {
                'publised'  : aticle.published,
                'mktime'    : time.mktime(aticle.published_parsed),
                'title'     : aticle.title,
                'summary'   : aticle.summary,
                'link'      : aticle.feedburner_origlink,
            }
            self.collect_news.append(_data)


    def connect_to_db(self):
        self.client = pymongo.MongoClient(MONGO_HOST, 27017)
        self.db = self.client[MONGO_DB]
        self.db.authenticate(MONGO_USER, MONGO_PASS)


    def check_news(self, news_dict):
        pymongo_cursor  = self.db.newsList.find({"mktime": news_dict['mktime'], "title": news_dict['title']})
        all_data = list(pymongo_cursor)
        if all_data.__len__() > 0:
            return False
        else:
            return True

    def load_news(self):
        for news in self.collect_news:
            if self.check_news(news):
                self.db.newsList.insert(news)
                self.news_add += 1



    def __del__(self):
        self.client.close()

if __name__ == '__main__':
    obj = Scrapper("http://feeds.reuters.com/reuters/topNews")
    print(obj.running())
