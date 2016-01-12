from flask import Flask, request, redirect
import controller as c

app = Flask(__name__, static_folder='assets')

@app.route('/')
def index():
    return c.index()

@app.route('/search')
def search():
    if request.method == 'GET':
        return c.search(request.args)
    else:
        return c.search()

@app.route('/load/search.html', methods=['GET'])
def process_search():
    if request.method == 'GET':
        return c.process_search(request.args)
    else:
        return c.error(404)

@app.route('/entreprise')
def ent():
    if request.method == 'GET':
        return c.entreprise(request.args.get('id'))
    else:
        return c.error(404)

@app.route('/redirect')
def red():
    if request.method == 'GET':
        link = request.args.get('link') 
        if link[0:3] == 'www':
            link = 'http//'+link
        return redirect(link.replace('//', '://'), 301)

@app.route('/art')
def articles():
    return c.articles()

@app.route('/art/<int:id>')
def article(id):
    return c.article(id)

@app.errorhandler(404)
def page_not_found(error):
    return c.error(404)

if __name__ == '__main__':
    app.run(debug=True)
