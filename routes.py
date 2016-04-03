from flask import Flask, render_template, request, session, flash, redirect, url_for, g
import requests
import rauth
import json

# import pdb

app = Flask(__name__)

app.config["DEBUG"] = True
app.config.from_object(__name__)

@app.route("/")
def main():
	return render_template('main.html')	

@app.route("/city", methods=["GET", "POST"])
def city_search():
	get_location = request.form["location"]
	params = {"term": "sushi", "radius_filter": "2000"}
	params["location"] = [get_location]
	
	#Obtain these from Yelp's manage access page
	consumer_key = "QQ7L1p_3MkFRgpX-hzt7rg"
	consumer_secret = "uNmAp-I10ojRR21PF1po2ozOPL0"
	token = "ZL2T198lJWyMlVunsfbEUpFsZQgreh6H"
	token_secret = "gbBImwNN0DoJ-Z0BcE0Yt8r_Hq0"

	session = rauth.OAuth1Session(
	consumer_key = consumer_key
	,consumer_secret = consumer_secret
	,access_token = token
	,access_token_secret = token_secret)
 
	get_data = session.get("http://api.yelp.com/v2/search",params=params)

#Transforms the JSON API response into a Python dictionary
	data = get_data.json()
	session.close()
	return render_template('results.html', data=data)
# start the development server using the run() method

@app.route("/jiro_movie")
def jiro():
    return render_template("jiro.html")

@app.route("/map")
def map():
	return render_template('map.html')	


if __name__== "__main__":
	app.run(debug=True)

# def get_search_parameters(lat,long):
#   #See the Yelp API for more details
#   params = {}
#   params["term"] = "sushi"
#   params["ll"] = "{},{}".format(str(lat),str(long))
#   params["radius_filter"] = "2000"
#   params["limit"] = "10"
 
#   return params

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