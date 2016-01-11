from sqlite3 import *
from db_config import *

class Article(object):
    def __init__(self, num):
        self.hydrate(num)

    def hydrate(self, num):
        r = sqlite3.connect(db_name).execute(query_select_article, [num]).fetchone()
        for i in range(len(r)):
            self.__setattr__(article_schema[i], r[i])
        return self


class ArticlesListe(object):
    def __init__(self, num):
        self.hydrate(num)
        self.liste = []

    def hydrate(self, num):
        db = sqlite3.connect(db_name)
        rows = db.execute(query_list_articles)
        row = rows.fetchone()
        while row:
            self.liste.append(Article(tuple(rows)[0]))
            row = rows.fetchone()
        return self

    def get(self):
        return self.liste