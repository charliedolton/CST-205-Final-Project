from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap
# from tmdbv3api import TMDb
# from config import config
# from secrets import secrets
from User import User
from ErrorMsg import ErrorMsg
import pickle
import json

# from PIL import Image
# from image_info import image_info
# import random

# for windows:
# $env:FLASK_APP="finalProj.py"
# $env:FLASK_ENV="development"
# flask run

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'sneak_from_the_stars_to_the_moon'
bootstrap = Bootstrap(app)


# tmdb = TMDb()
# # hide API_KEY from github!
# # secrets.py should be ignored on git push
# tmdb.api_key = secrets.api_key
# tmdb.language = 'en'
# tmdb.debug = True

## site forms ##
class LoginForm(FlaskForm):
    username = StringField( 'Username', validators=[DataRequired()] )
    password = StringField( 'Password', validators=[DataRequired()] )
## end of site forms ##

# ## pseudo db methods using pickle ##
# def load_users():
#     with open('id_to_user', 'rb') as my_file:
#         saved_data = pickle.load(my_file)
#         User.id_to_user_map = saved_data
#         my_file.close()
#     with open('user_to_id', 'rb') as my_file:
#         saved_data = pickle.load(my_file)
#         User.user_to_id_map = saved_data
#         my_file.close()

# def write_db():
#     with open('id_to_user', 'wb') as my_file:
#         pickle.dump(User.id_to_user_map, my_file)
#         my_file.close()
#     with open('user_to_id', 'wb') as my_file:
#         pickle.dump(User.user_to_id_map, my_file)
#         my_file.close()


# # write_db() needs to run once so 'pickled' exists
# write_db()
# load_users()
# ## end of pseudo db methods using pickle ##

## pseudo db methods using json ##
def load_users():
    print('----- load_users() -----')
    with open('id_to_user.json', 'r') as my_file:
        saved_data = json.load(my_file)
        User.id_to_user_map = saved_data
        print(f'id_to_user_map:\n{saved_data}')
        my_file.close()
    with open('user_to_id.json', 'r') as my_file:
        saved_data = json.load(my_file)
        User.user_to_id_map = saved_data
        print(f'user_to_id_map:\n{saved_data}')
        my_file.close()
    print('----- end of load_users() -----\n')

def write_db():
    # https://realpython.com/lessons/serializing-json-data/
    with open('id_to_user.json', 'w') as write_file:
        json.dump(User.id_to_user_map, write_file)
        write_file.close()
    with open('user_to_id.json', 'w') as write_file:
        json.dump(User.user_to_id_map, write_file)
        write_file.close()

# write_db()
## end of pseudo db methods using json ##

load_users()
print('----- db check -----')
print(f'User.user_to_id_map:\n{User.user_to_id_map}')
print(f'User.id_to_user_map:\n{User.id_to_user_map}')
print('----- end of db check -----\n')

## routes ##
@app.route('/', defaults={'username': None})
def index(username):
    # splash page 
    return render_template('index.html', username=username)

@app.route('/login')
def login():
    # show login form
    form = LoginForm()
    return render_template('login.html', form=form)

## interal APIs ##
@app.route('/user/auth', methods=['POST'])
def auth():
    # check for valid user
    form = LoginForm()
    if form.validate_on_submit():
        user_id = User.user_to_id_map.get(form.username.data, ErrorMsg.bad_login)
        if ( user_id == ErrorMsg.bad_login):
            return ErrorMsg.bad_login
        else:
            if (User.id_to_user_map.get(user_id)[1] == form.password.data):
                redirect(url_for('/', username=User.id_to_user_map.get(user_id)[0]))
            else:
                return ErrorMsg.bad_login
## end interal APIs ##
## end of routes ##