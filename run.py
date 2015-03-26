from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
	return render_template("home.html")
	# return "Hello"

@app.route('/mol/<key>')
@app.route('/mol/<key>/')
def molecule(key):
	return "Test: " + key

@app.route('/news')
@app.route('/news/')
def news():
	return "PQR: News"

@app.route('/browse')
@app.route('/browse/')
def browse():
	return "PQR: Browse"

@app.errorhandler(404)
def page_not_found(e):
	return "404"

if __name__ == '__main__':
	app.run()
