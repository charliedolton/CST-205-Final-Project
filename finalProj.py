from flask import Flask, flash, redirect, render_template, request, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, SelectField, TextAreaField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap
from tmdbv3api import TMDb
from config import Config
from user import User
from movie import MovieObj
from ErrorMsg import ErrorMsg
import json
from tmdbv3api import Movie
import requests, random, math
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
app.config['SECRET_KEY'] = Config.secret
bootstrap = Bootstrap(app)
fresh = True

tmdb = TMDb()
# hide API_KEY from github!
# config.py should be ignored on git push
tmdb.api_key = Config.api_key
tmdb.language = 'en'
tmdb.debug = True

movie = Movie()

## site forms ##
class LoginForm(FlaskForm):
    username = StringField( 'Username', validators=[DataRequired()] )
    password = PasswordField( 'Password', validators=[DataRequired()] )
## end of site forms ##

class ProfileForm(FlaskForm):
    username = StringField( 'username', validators=[DataRequired()] )
    kind = SelectField( 'kind', choices=("Critic", "Audience") )
    about_me = TextAreaField( 'about_me', validators=[DataRequired()] )

## pseudo db methods using json ##
def load_users():
    # print('----- load_users() -----')
    with open('id_to_user.json', 'r') as my_file:
        saved_data = json.load(my_file)
        User.id_to_user_map = saved_data
        # print(f'id_to_user_map:\n{saved_data}')
        my_file.close()
    with open('user_to_id.json', 'r') as my_file:
        saved_data = json.load(my_file)
        User.user_to_id_map = saved_data
        # print(f'user_to_id_map:\n{saved_data}')
        my_file.close()
    # print('----- end of load_users() -----\n')

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

if fresh == True:
    load_users()
    print('----- db check -----')
    print(f'User.user_to_id_map:\n{User.user_to_id_map}')
    print(f'User.id_to_user_map:\n{User.id_to_user_map}')
    print('----- end of db check -----\n')

    ## pseudo session variables ##
    User.current_username = None
    User.current_user_id = None
    User.is_authenticated = False
    ## end of pseudo session variables ##
    fresh = False

## routes ##
@app.route('/')
def index():
    #Get recommended movies
    id = math.ceil(random.random() * 200)
    print(id)
    recommendations = movie.recommendations(movie_id=id)
    #print(recommendations)
    movies = []
    for a in range(3):
        movies.append((recommendations[a]))

    # splash page? or general list of movies
    if authenticate() is False:
        print('index: No one is logged in.')
    else:
        print(f'index: { User.current_username } is logged in.')
    return render_template('index.html', username=User.current_username, titles=movies)

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    print("----- inside login route -----")
    # show login form
    form = LoginForm()
    if form.validate_on_submit():
        try:
            user_id = User.user_to_id_map[form.username.data]
            print(f'username: {form.username.data}\nuser_id: {str(user_id)}')
            print(f'User.id_to_user_map[str(user_id)][\'password\']: {User.id_to_user_map[str(user_id)]["password"]}')
            print(f'form password: {form.password.data}')
            print(f'User.id_to_user_map[str(user_id)][\'password\'] == form.password.data: {User.id_to_user_map[str(user_id)]["password"] == form.password.data}')
            if (User.id_to_user_map[str(user_id)]['password'] == form.password.data):
                username = User.id_to_user_map[str(user_id)]['username']
                PseudoSession.current_username = username
                PseudoSession.current_user_id = user_id
                PseudoSession.is_authenticated = True
                print(f'/user/auth: username: {PseudoSession.current_username}\n')
                return redirect(url_for('index'))
            else:
                flash(ErrorMsg.bad_login, 'error')
                return redirect(url_for('login'))
        except KeyError:
            flash(ErrorMsg.bad_login, 'error')
            return redirect(url_for('login'))
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    User.current_username = None
    User.current_user_id = None
    User.is_authenticated = False
    return redirect(url_for('index'))

@app.route("/profile/<name>")
def view_profile(name):
    for x in user_info:
        print("name=" + x['name'])
        if x['name'] == name.lower():
            return render_template('view_profile.html', user=x)
    return render_template("error.html")

@app.route("/profile_edit/<name>", methods=['GET', 'POST'])
def edit_profile(name):
    form = ProfileForm()
    print(form.validate_on_submit())
    if form.validate_on_submit():
        user_id = User.user_to_id_map.get(form.username.data, ErrorMsg.bad_login)
        print("The ID is")
        print(user_id)
        if (user_id == ErrorMsg.bad_login):
            flash(ErrorMsg.bad_login, 'error')
            return redirect(url_for('login'))
        else:
            #modify the form
            with open("id_to_user.json", "w+") as read_file:
                data = json.load(read_file)
                data[User.user_to_id_map.get(form.name.data, ErrorMsg.bad_login)] = {
                    "kind" : form.kind,
                    "about" : form.about_me,
                    "favorites" : data[form.name].favorites
                }
                print(form.name.data)
                #json.dump(data)
    else:
        for x in user_info:
            if x['name'] == name.lower():
                return render_template('edit_profile.html', user=x, form=form)
        return render_template("error.html")
  
@app.route("/search")
def search():
    return render_template("search.html")

## end of routes ##

## internal APIs ##
def authenticate():
    return User.is_authenticated
## end internal APIs ##


