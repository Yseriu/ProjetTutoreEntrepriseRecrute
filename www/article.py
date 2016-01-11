from sqlite3 import *
from db_config import *

class Article(object):
    def __init__(self, num):
        self.hydrate(num)

    def hydrate(self, num):
        r = sqlite3.connect(db_name).execute(query_select_article, [num]).fetchone()
        for i in range(len(r)):
            self.__setattr__(article_schema[i], r[i])
        limite = 200
        while limite < len(self.content) and self.content[limite] != ' ':
            limite += 1
        self.resume = self.content[:limite] +' ...'
        return self


class ArticlesListe(object):
    def __init__(self):
        self.liste = []
        self.hydrate()

    def hydrate(self):
        db = sqlite3.connect(db_name)
        rows = db.execute(query_list_articles)
        row = rows.fetchone()
        while row:
            n = tuple(rows)[0][0]
            self.liste.append(Article(n))
            row = rows.fetchone()
        return self

    def get(self):
        print(self.liste)
        return self.liste