from flask import Flask, render_template, request, session, flash, redirect, url_for, g

app = Flask(__name__)

app.config["DEBUG"] = True
app.config.from_object(__name__)

@app.route("/")
def main():
	return render_template('main.html')





# start the development server using the run() method
if __name__== "__main__":
	app.run(debug=True)

# @app.route("/test/<search_query>")
# def search(search_query):
# 	return search_query

# @app.route("/integer/<int:value>")
# def int_type(value):
# 	print value + 1
# 	return "correct!"

# @app.route("/float/<float:value>")
# def float_type(value):
# 	print value + 1
# 	return "correct!"

# @app.route("/path/<path:value>")
# def path_type(value):
# 	print value
# 	return "correct!"	

# @app.route("/name/<name>")
# def index(name):
# 	if name.lower() == "michael":
# 		return "Hello, {}".format(name), 200
# 	else:
# 		return "Not Found", 404	