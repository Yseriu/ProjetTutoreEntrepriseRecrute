from sqlite3 import *
from site_config import *
from db_config import *

class offre(object):
    def __init__(self, id):
        self.db = sqlite3.connect(db_name)
        self.hydrate(id)

    def hydrate(self, id):
        r = self.db.execute(query_select_offre, [id]).fetchone()
        for i in range(len(r)):
            self.__setattr__(table_list[i], r[i])
        return self