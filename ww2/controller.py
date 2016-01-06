from flask import render_template


def index():
	return "Bonjour"
	
def entreprise(entreprise_id):
	pass


def error(error_id):
	if error_id == 404:
		return '404 - Not Found'
	else:
		return 'Error not Found'
