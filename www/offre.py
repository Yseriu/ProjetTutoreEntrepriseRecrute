from sqlite3 import *
from site_config import *
from db_config import *

class offre(object):
    def __init__(self, id):
        self.hydrate(id)

    def hydrate(self, id):
        r = sqlite3.connect(db_name).execute(query_select_offre, [id]).fetchone()
        for i in range(len(r)):
            self.__setattr__(table_list[i], r[i])
        print(self.image)
        self.image = self.image.replace('//', '://')
        self.sources = self.sources.replace('//', '://')
        return self