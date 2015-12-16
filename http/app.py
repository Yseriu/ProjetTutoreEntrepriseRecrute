from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def main():
	return render_template("header.html") 


@app.route('/pages/entreprises/')
def ent():
	return render_template("entreprises.html")


@app.errorhandler(404)
def page_not_found(error):
	return  "slt c est l erreur 404"



if __name__ == '__main__':
	app.run(debug=True)