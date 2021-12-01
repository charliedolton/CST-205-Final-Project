from flask import Flask, render_template
from flask_bootstrap import Bootstrap
tmdbv3api import TMDb
import config
import User
import pickle

ID_TO_USER_MAP = 0
USER_TO_ID_MAP = 1
USER_FAVORITES = 2
USER_REVIEWS = 3

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

# write_db() needs to run once so 'pickled' exists
write_db()
# users = load_users()

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/login')
def login():
    # check for valid user

## interal api ##
def load_users():
    with open('pickled', 'rb') as my_file:
        saved_data = pickle.load(my_file)
        User.user_to_id_map = saved_data[0]

def write_db():
    with open('pickled', 'wb') as my_file:
        pickle.pickle(User.user_to_id_map, User.id_to_user_map, )