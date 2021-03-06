from flask import render_template
from sqlite3 import *
from db_config import *
from offre import offre
from article import Article, ArticlesListe
from smtplib import *

def index():
    return render_template('index.html')

def search(args=None):
    if args == None:
        return render_template('search.html')
    else:
        return render_template('search.html', args=args)

def process_search(args):

    search = list_offres()

    def process_arg_dom(nom, on):
        if on == 'on':
            search.add_domaine(nom)
            print(nom)
        else:
            search.remove_domaine(nom)

    def process_arg_level(nom, on):
        if on == 'on':
            search.add_level(nom)
        else:
            search.remove_level(nom)
    domaines = {'prog','reseau','web','ios', 'games', 'bdd'}
    for dom in domaines:
        if args.get('chk'+dom): process_arg_dom(dom, args.get('chk'+dom))

    if args.get('chk2'): process_arg_level('2', args.get('chk2'))
    if args.get('chk3'): process_arg_level('3', args.get('chk3'))
    if args.get('chk5'): process_arg_level('5', args.get('chk5'))
    if args.get('chk8'): process_arg_level('8', args.get('chk8'))

    if args.get('txt:salaire'):
        try:
            search.set_salaire(int(args.get('txt:salaire')))
        except:
            print('error')

    if args.get('txt:localisation'):
        search.set_localisation(args.get('txt:localisation'))

    if args.get('txt:txt'):
        search.set_txt(args.get('txt:txt'))

    # querry time !
    q = search.build().get()
    print(q)
    ans = []
    r = sqlite3.connect(db_name).execute(q)
    row = r.fetchone()
    while row:
        ans.append({table_list[i] : tuple(row)[i] for i in range(12)})
        ans[-1]['image'] = ans[-1]['image'].replace('//', '://')
        ans[-1]['lien'] = ans[-1]['lien'].replace('//', '://')
        ans[-1]['sources'] = ans[-1]['sources'].replace('//', '://')
        limit = 370
        while limit < len(ans[-1]['description']) and ans[-1]['description'][limit] != ' ':
            limit += 1
        ans[-1]['description'] = ans[-1]['description'][:limit]+' ...'
        row = r.fetchone()

    return render_template('results.html', results=ans)

def entreprise(entreprise_id):
    return render_template('entreprise.html', data=offre(entreprise_id))

def articles():
    return render_template('articlesList.html', data=ArticlesListe().get())

def article(id):
    return render_template('article.html', data=Article(id))

def contact():
    return render_template('contact.html')

def who():
    return render_template('who.html')

def send(args):
    db = sqlite3.connect(db_name)
    req = "INSERT INTO mail VALUES ('" + args.get('sender') + "' , '" + args.get('content') + "');"
    db.execute(req)
    db.commit()
    return render_template('sent.html')

def error(error_id):
    if error_id == 404:
        return render_template('404.html')
    else:
        return 'Error not Found'
