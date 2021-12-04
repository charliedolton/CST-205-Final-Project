from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from tmdbv3api import TMDb
from tmdbv3api import Movie
import config
import requests, json
import random, math

from user_info import user_info
# from PIL import Image
# from image_info import image_info
# import random

# for windows:
# $env:FLASK_APP="finalProj.py"
# $env:FLASK_ENV="development"
# flask run

app = Flask(__name__)
app.config['DEBUG'] = True
bootstrap = Bootstrap(app)

tmdb = TMDb()
# hide API_KEY from github!
# config.py should be ignored on git push
tmdb.api_key = config.api_key
tmdb.language = 'en'
tmdb.debug = True

movie = Movie()

@app.route("/")
def index():
    id = math.ceil(random.random() * 200)
    print(id)
    recommendations = movie.recommendations(movie_id=id)
    #print(recommendations)
    movies = []
    for a in range(3):
        movies.append((recommendations[a].title, recommendations[a].id))
    print(movies)
    return render_template("index.html", titles=movies)

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/profile_edit/<name>")
def edit_profile(name):
    #print(name)
    for x in user_info:
        print("name=" + x['name'])
        #print("----")
        if x['name'] == name.lower():
            print("Smeckledorf!")
            #x[id] = id
            return render_template('edit_profile.html', user=x)
    return render_template("error.html")

@app.route("/profile/<name>")
def view_profile(name):
    for x in user_info:
        print("name=" + x['name'])
        #print("----")
        if x['name'] == name.lower():
            print("Smeckledorf!")
            #x[id] = id
            return render_template('view_profile.html', user=x)
    return render_template("error.html")