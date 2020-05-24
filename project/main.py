import time


class Scrapper:

    def __init__(self):
        self.d = time()

    def running(self):
        return self.d

    def check_news(self):
        pass

    def load_news(self):
        pass


obj = Scrapper()
print(obj.running())
