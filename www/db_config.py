import sqlite3

db_name = 'database'

query_select_offre = 'SELECT * FROM entreprises WHERE Nom=?'

query_select_article = 'SELECT * FROM articles WHERE id=?'

query_list_articles = 'SELECT id FROM articles'

table_list = ['titre', 'localisation', 'taille', 'poste', 'secteur_activite', 'salaire', 'niveau_etudes_requis', 'tags', 'sources', 'lien', 'image', 'description']

article_schema = ['id', 'titre', 'content']

domaines = {'ios' : ('ios', 'android'),
            'prog' : ('programmation', 'programmeur'),
            'bdd' : ('base de donnees',),
            'games' : ('jeu',)}

class list_offres(object):

    def __init__(self):
        self.ans = 'SELECT * FROM entreprises'
        self.dom = set()
        self.l = set()
        self.sal = 0
        self.loc = ''
        self.txt = ''

        self.condition = False

    def add_condition(self):
        if not self.condition:
            self.ans += ' WHERE '
            self.condition = True
        else:
            self.ans += ' AND '

    def add_domaine(self, domaine):
        if domaine in domaines:
            for d in domaines[domaine]:
                self.dom.add(d)
        else:
            self.dom.add(domaine)
        return self

    def remove_domaine(self, domaine):
        self.dom.discard(domaine)
        return self

    def add_level(self, level):
        self.l.add(level)
        return self

    def remove_level(self, level):
        self.l.discard(level)
        return self

    def set_salaire(self, salaire):
        self.sal = salaire
        return self

    def set_localisation(self, localisation):
        self.loc = localisation
        return self

    def set_txt(self, txt):
        self.txt = txt
        return self

    def build(self):
        if self.dom != set():
            self.add_condition()
            for domaine in self.dom:
                self.ans += ' lower(secteur_activite) LIKE \'%'+domaine+'%\' OR lower(poste) LIKE \'%'+domaine+'%\' OR '
            self.ans = self.ans[:-3]
        if self.l != set():
            self.add_condition()
            for level in self.l:
                self.ans += ' niveau_etude_requis LIKE \'%' + level + '%\' OR '
            self.ans = self.ans[:-3]
        if self.sal != 0:
            self.add_condition()
            self.ans += ' salaire > ' + str(self.sal)
        if self.loc != '':
            self.add_condition()
            self.ans += ' pays LIKE \'%' + self.loc + '%\' '
        if self.txt != '':
            self.add_condition()
            txtSet = set(self.txt.replace('+', ' ').replace(',', ' ').split(' ')).discard(' ')
            for t in txtSet:
                self.ans += ' lower(nom) LIKE \'%' + t + '%\' OR lower(description) LIKE \'%' + t + '%\' OR lower(tags) \'%' + t + '%\' AND '
            self.ans = self.ans[:-3]
        return self

    def get(self):
        return self.ans

if __name__ == '__main__':
    db = sqlite3.connect(db_name)
    x = list_offres()
    x.set_localisation('France').build()
    print(x.get())
    r = db.execute(x.get())
    print(r.rowcount)
    for row in r:
        print(row)