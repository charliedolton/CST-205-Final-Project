from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from tmdbv3api import TMDb
import config
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

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/profile_edit")
def edit_profile():
    return render_template("edit_profile.html")

@app.route("/profile")
def view_profile():
    return render_template("view_profile.html")