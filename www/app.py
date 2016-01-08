from flask import Flask, request
import controller as c

app = Flask(__name__, static_folder='assets')

@app.route('/')
def index():
    return c.index()

@app.route('/search')
def search():
    return c.search()

#@app.route('/search/process', methods=['GET'])
@app.route('/load/search.html', methods=['GET'])
def process_search():
    if request.method == 'GET':
        return c.process_search(request.args)
    else:
        return c.error(404)

@app.route('/pages/entreprise/<int:entreprise_id>')
def ent():
    return c.entreprise(entreprise_id)

@app.route('/load/search.html')
def loader():
    return c.loader()

@app.errorhandler(404)
def page_not_found(error):
    return c.error(404)

if __name__ == '__main__':
    app.run(debug=True)
