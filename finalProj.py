from flask import Flask, render_template
from flask_bootstrap import Bootstrap
tmdbv3api import TMDb
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

@app.route("/search")
def search():
    return render_template("search.html")