from flask import Flask
import controller as c

app = Flask(__name__, static_folder='assets')

@app.route('/')
def index():
	return c.index()
	
@app.route('/pages/entreprise/<int:entreprise_id>')
def ent():
	return c.entreprise(entreprise_id)

@app.errorhandler(404)
def page_not_found(error):
	return c.error(404)

if __name__ == '__main__':
	app.run(debug=True)
