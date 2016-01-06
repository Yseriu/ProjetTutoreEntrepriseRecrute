from flask import render_template
from db_config import *


def index():
	return render_template('index.html')

def search():
	return render_template('search.html')

def process_search(args):
	
	search = list_offres()
	
	def process_arg_dom(nom, on):
		if on == 'on':
			search.add_domaine(arg[0])
		else:
			search.remove_domaine(arg[0])
	
	def process_arg_level(nom, on):
		if on == 'on':
			search.add_level(arg[0])
		else:
			search.remove_level(arg[0])
	
	if args.get('chk:Securite'): process_arg_dom('securite', args.get('chk:Securite'))
	if args.get('chk:Environnement'): process_arg_dom('environnement', args.get('chk:Environnement'))
	if args.get('chk:BDD'): process_arg_dom('bdd', args.get('chk:BDD'))
	if args.get('chk:Telephonie'): process_arg_dom('telephonie', args.get('chk:Telephonie'))
	
	if args.get('chk:+2'): process_arg_level('2', args.get('chk:+2'))
	if args.get('chk:+3'): process_arg_level('3', args.get('chk:+3'))
	if args.get('chk:+5'): process_arg_level('5', args.get('chk:+5'))
	if args.get('chk:+8'): process_arg_level('8', args.get('chk:+8'))
	
	if args.get('txt:salaire'):
		try:
			search.set_salaire(int(args.get('txt:salaire')))
		except:
			pass
	
	if args.get('txt:localisation'):
		search.set_localisation(args.get('txt:localisation'))
	
	# querry time !
	q = search.get()
	

def entreprise(entreprise_id):
	pass


def error(error_id):
	if error_id == 404:
		return '404 - Not Found'
	else:
		return 'Error not Found'
