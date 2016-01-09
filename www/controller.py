from flask import render_template
from sqlite3 import *
from db_config import *
from jinja import *

def index():
    return render_template('index.html')

def search():
    return render_template('search.html')

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
    domaines = {'securite','environnement','bdd','telephonie'}
    for dom in domaines:
        if args.get('chk'+dom): process_arg_dom(dom, args.get('chk'+dom))

    if args.get('chk2'): process_arg_level('2', args.get('chk2'))
    if args.get('chk3'): process_arg_level('3', args.get('chk3'))
    if args.get('chk5'): process_arg_level('5', args.get('chk5'))
    if args.get('chk8'): process_arg_level('8', args.get('chk8'))

    if args.get('txt:salaire'):
        print('salaire')
        try:
            search.set_salaire(int(args.get('txt:salaire')))
        except:
            print('error')

    if args.get('txt:localisation'):
        search.set_localisation(args.get('txt:localisation'))

    # querry time !
    q = search.build().get()
    print(q)
    ans = []
    r = sqlite3.connect(db_name).execute(q)
    row = r.fetchone()
    while row:
        ans.append({['titre', 'localisation', 'taille', 'poste', 'secteur_activite', 'salaire', 'niveau_etudes_requis', 'tags', 'sources', 'lien', 'image', 'description'][i] : tuple(row)[i] for i in range(12)})
        ans[-1]['image'] = ans[-1]['image'].replace('//', '://')
        row = r.fetchone()

    return render_template('results.html', results = ans)

def loader():
    return render_template('to_load.html')

def entreprise(entreprise_id):
    return render_template('entreprise.html')

def error(error_id):
    if error_id == 404:
        return render_template('404.html')
    else:
        return 'Error not Found'
