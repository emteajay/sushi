from flask import Flask, render_template, request, session, flash, redirect, url_for, g

app = Flask(__name__)

app.config.from_object(__name__)

@app.route("/")
def main():
	return render_template('main.html')


if __name__== "__main__":
	app.run(debug=True)
