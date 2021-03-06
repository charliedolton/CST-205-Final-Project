## 
# GitHub link: https://github.com/charliedolton/CST-205-Final-Project
##
from flask import Flask, flash, redirect, render_template, request, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, SelectField, TextAreaField
from wtforms.validators import DataRequired, EqualTo
from flask_bootstrap import Bootstrap
from tmdbv3api import TMDb
from config import Config
from user import User
from movie import MovieObj
from database import Database
from error_msg import ErrorMsg
from pseudo_session import PseudoSession
import json
from tmdbv3api import Movie, Search
import requests, random, math
from user_info import user_info

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
base_img_url = 'https://image.tmdb.org/t/p/original'

#Get an object for the movie API
movie = Movie()

#Gloal variables for passing variables into the ProfileForm
username_field = "You should not be seeing this"
kind_field = "You should not be seeing this"
about_me_field = "You should not be seeing this"

#Methods for the same reason as above
def get_username():
    return username_field

def get_kind():
    return kind_field

def get_info():
    return about_me_field

## site forms ##
class LoginForm(FlaskForm):
    username = StringField( 'Username', validators=[DataRequired()] )
    password = PasswordField( 'Password', validators=[DataRequired()] )

class SignupForm(FlaskForm):
    username = StringField( 'Username', validators=[DataRequired()] )
    password = PasswordField( 'Password', validators=[DataRequired(),
                                                        EqualTo('confirm', message='Passwords must match.')] )
    confirm = PasswordField( 'Confirm Password', validators=[DataRequired()])

class ProfileForm(FlaskForm):
    #print(get_username)
    username = StringField( 'username', default = get_username, validators=[DataRequired()] )
    #print(get_kind)
    kind = SelectField( 'kind', default = get_kind, choices=("Critic", "Audience", "Test") )
    #print(get_info)
    about_me = TextAreaField( 'about_me', default = get_info, validators=[DataRequired()] )

class ReviewForm(FlaskForm):
    #print(get_username)
    username = StringField( 'username', default = get_username, validators=[DataRequired()] )
    #print(get_kind)
    rating = SelectField( 'rating', default = 3, choices=(1,2,3,4,5) )
    #print(get_info)
    text = TextAreaField( 'text', default = "Write text here", validators=[DataRequired()] )
    
class SearchForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    year = StringField('year')
## end of site forms ##

## pseudo db methods using json ##
def load_users():
    # print('----- load_users() -----')
    with open('id_to_user.json', 'r') as my_file:
        saved_data = json.load(my_file)
        Database.id_to_user_map = saved_data
        # print(f'id_to_user_map:\n{saved_data}')
        my_file.close()
    with open('user_to_id.json', 'r') as my_file:
        saved_data = json.load(my_file)
        Database.user_to_id_map = saved_data
        # print(f'user_to_id_map:\n{saved_data}')
        my_file.close()
    with open('user_favorites.json', 'r') as my_file:
        saved_data = json.load(my_file)
        Database.user_favorites = saved_data
        # print(f'user_favorites:\n{saved_data}')
        my_file.close()
    # print('----- end of load_users() -----\n')

def write_db():
    # https://realpython.com/lessons/serializing-json-data/
    with open('id_to_user.json', 'w') as write_file:
        json.dump(Database.id_to_user_map, write_file, indent=4)
        write_file.close()
    with open('user_to_id.json', 'w') as write_file:
        json.dump(Database.user_to_id_map, write_file, indent=4)
        write_file.close()
    with open('user_favorites.json', 'w') as write_file:
        json.dump(Database.user_favorites, write_file, indent=4)
        write_file.close()

# write_db()
## end of pseudo db methods using json ##

if fresh == True:
    load_users()
    print('----- db check -----')
    # print(f'User.user_to_id_map:\n{Database.user_to_id_map}')
    # print(f'User.id_to_user_map:\n{Database.id_to_user_map}')
    # print(f'Movie.user_favorites:\n{Database.user_favorites}')
    print(f'current number of users: {Database.get_num_users()}')
    #print('----- end of db check -----\n')

    ## pseudo session variables ##
    PseudoSession.current_username = None
    PseudoSession.current_user_id = None
    PseudoSession.is_authenticated = False
    ## end of pseudo session variables ##
    fresh = False

## routes ##
@app.route('/')
def index():
    #Get recommended movies from a random one
    id = math.ceil(random.random() * 200)
    try:
        print(f'random movie_id: {id}')
        recommendations = movie.recommendations(movie_id=id)
    except:
        print(f'on except movie_id: 329')
        recommendations = movie.recommendations(movie_id=329)
    movies = []
    
    #provide movie recommendations to homepage
    for a in range(len(recommendations)):
        # print(f'rec {a} title: {recommendations[a]["title"]}, adult: {recommendations[a]["adult"]}')
        if recommendations[a]["adult"] == False:
            movies.append(recommendations[a])

    # splash page? or general list of movies
    if authenticate() is False:
        print('index: No one is logged in.')
    else:
        print(f'index: { PseudoSession.current_username } is logged in.')
    return render_template('index.html', username=PseudoSession.current_username, titles=movies, base_img_url=base_img_url)

@app.route('/signup', methods=['GET','POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        newUser = User(form.username.data, None, form.password.data, None)
        if add_newUser(newUser):
            form=LoginForm()
            return render_template('login.html', form=form)
        else:
            flash(ErrorMsg.user_taken, 'error')
            return redirect(url_for('signup'))
    return render_template('signup.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    print("----- inside login route -----")
    # show login form
    form = LoginForm()
    print(form.validate_on_submit())
    if form.validate_on_submit():
        try:
                        #Get user info
            user_id = Database.user_to_id_map[form.username.data]
            #print(f'username: {form.username.data}\nuser_id: {str(user_id)}')
            #print(f'Database.id_to_user_map[str(user_id)]["password"]: {Database.id_to_user_map[str(user_id)]["password"]}')
            #print(f'form password: {form.password.data}')
            #print(f'Database.id_to_user_map[str(user_id)]["password"] == form.password.data: {Database.id_to_user_map[str(user_id)]["password"] == form.password.data}')

            #login successful
            if (Database.id_to_user_map[str(user_id)]["password"] == form.password.data):
                username = Database.id_to_user_map[str(user_id)]["username"]
                PseudoSession.current_username = username
                PseudoSession.current_user_id = user_id
                PseudoSession.is_authenticated = True

                print(f'/user/auth: username: {PseudoSession.current_username}\n')
                return redirect(url_for('index'))
            else:
                #login unsuccessful
                flash(ErrorMsg.bad_login, 'error')
                return redirect(url_for('login'))
        except KeyError:
            #Invalid login
            flash(ErrorMsg.bad_login, 'error')
            return redirect(url_for('login'))

    #If all else fails
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    PseudoSession.current_username = None
    PseudoSession.current_user_id = None
    PseudoSession.is_authenticated = False
    return redirect(url_for('index'))

@app.route("/profile/<name>")
def view_profile(name):
    #Search for a user
    x = Database.id_to_user_map[get_user_id(name)]
    if x["username"] == name:
        return render_template('view_profile.html', user=x)
    #If not found, render an error
    return render_template("error.html")

@app.route("/profile_edit/<name>", methods=['GET', 'POST'])
def edit_profile(name):
    form = ProfileForm()
    #print(form.validate_on_submit())

    if form.validate_on_submit():
        #For POST method
        user_id = Database.user_to_id_map[form.username.data]

        if (user_id == ErrorMsg.bad_login):
            flash(ErrorMsg.bad_login, 'error')
            return redirect(url_for('login'))
        else:
            #Open file to modify
            a_file = open("id_to_user.json", "r")
            data = json.load(a_file)
            a_file.close()

            #with open("id_to_user.json", "r+") as read_file:
            #    data = json.load(read_file)

            #modify the file
            data[get_user_id(form.username.data)]['kind'] = form.kind.data
            data[get_user_id(form.username.data)]["about"] = form.about_me.data

            #Save modified file
            a_file = open("id_to_user.json", "w")
            json.dump(data, a_file)
            a_file.close()
            load_users()

            return render_template('view_profile.html', user=Database.id_to_user_map[get_user_id(name)])
    else:
        #For non-POST
        #Search for a user
        user_id = Database.user_to_id_map[name]
        x = Database.id_to_user_map[str(user_id)]
        print(x)
        if x["username"] == name:
            #Pass global variables to set defaults in a WTForm
            global username_field
            username_field = name
            global kind_field
            kind_field = x['kind']
            global about_me_field
            about_me_field = x['about']

            #Make a new ProfileForm so the defaults show up properly
            return render_template('edit_profile.html', user=x, form=ProfileForm())

        return render_template("error.html")
  
@app.route("/search", methods = ["GET", "POST"])
def search():
    if request.method == "POST":
        form = SearchForm()
        if form.validate_on_submit():
            searchTerms = {
                "query" : form.title.data,
                "year" : form.year.data,
            }
            print(searchTerms)
            search = Search()
            movie = search.movies(searchTerms)
            movie_id = str(movie[0].id)
            
            return redirect("/movie/" + movie_id)
    else:
        return render_template("search.html", form=SearchForm(), username=PseudoSession.current_username)

@app.route("/favorites/<username>")
def favorites(username):
    if authenticate():
        user_id = Database.user_to_id_map[username]
        try:
            favorites = Database.user_favorites[user_id]
            # print(f'-- type of favorites to send: {type(favorites)}')
            # print(f'-- favorites to send: {favorites}')
        except KeyError:
            Database.user_favorites[user_id] = []
            favorites = Database.user_favorites[user_id]
        return render_template('user_favorites.html', user=username, favorites=favorites)
    else:
        return redirect(url_for('login'))

@app.route("/favorites/<username>/add/<movie_id>")
def add_favorite(username, movie_id):
    if authenticate():
        m = movie.details(movie_id)
        movieObj = MovieObj(m["id"], m["title"], m["release_date"], m["overview"], base_img_url + m["poster_path"])
        if add_favorite(PseudoSession.current_user_id, movieObj):
            return redirect(url_for('favorites', username=PseudoSession.current_username))
    return redirect(url_for('index'))


#See one movie on its own page with reviews
@app.route("/movie/<movie_id>")
def reviews(movie_id):
    #Get movie
    m = movie.details(movie_id)

    #Find reviews if any
    try:
        a_file = open("storage/reviews/" + movie_id + ".json", "r")
        data = json.load(a_file)
        a_file.close()
    except FileNotFoundError:
        data=[]

    return render_template("reviews.html", reviews=data, movie=m, username=PseudoSession.current_username)

@app.route("/write_review/<movie_id>", methods=['GET','POST'])
def write_review(movie_id):
    form = ReviewForm()
    if form.validate_on_submit():
        user_id = Database.user_to_id_map[form.username.data]
        print("The ID is")
        print(user_id)
        if (user_id == ErrorMsg.bad_login):
            flash(ErrorMsg.bad_login, 'error')
            return redirect(url_for('login'))
        else:
            #Load file to modify
            try:
                a_file = open("storage/reviews/" + movie_id + ".json", "r")
                data = json.load(a_file)
                a_file.close()
            except FileNotFoundError:
                data=[]

            #Make a review to appent
            review = {
                "user": PseudoSession.current_username,
                "kind": "Critic",
                "text": form.text.data,
                "score": form.rating.data
            }

            #Add the new revies
            data.insert(len(data),review)

            #Save and overwrite file
            a_file = open("storage/reviews/" + movie_id + ".json", "w")
            json.dump(data, a_file)
            a_file.close()

            return render_template("reviews.html", movie = movie.details(movie_id), reviews=data, username=PseudoSession.current_username)
    else:
        #Load the page to write a review
        m = movie.details(movie_id)
        global username_field
        username_field = PseudoSession.current_username
        return render_template("write_review.html", form=ReviewForm(), movie_id=movie_id, movie=m, user=PseudoSession.current_username)
## end of routes ##

## internal APIs ##
def add_newUser(newUser):
    print("===== in add_newUser(newUser) =====")
    print(f"    newUser.get_username(): {newUser.get_username()}")
    print(f"    type(newUser): {type(newUser)}")
    print(f"    Database.user_to_id_map.keys(): {Database.user_to_id_map.keys()}")
    print(f"isinstance(newUser, User) and (newUser.get_username() not in Database.user_to_id_map.keys()): {isinstance(newUser, User) and (newUser.username not in Database.user_to_id_map.keys())}")
    if isinstance(newUser, User) and (newUser.get_username() not in Database.user_to_id_map.keys()):
        Database.id_to_user_map[newUser.get_str_id()] = {
                "username": newUser.get_username(),
                "email": newUser.get_email(),
                "password": newUser.get_password(),
                "iconUrl": newUser.get_icon_url(),
                "kind": "Audience",
                "about": "About the user."
            }
        Database.user_to_id_map[newUser.get_username()] = newUser.get_str_id()
        Database.user_favorites[newUser.get_str_id()] = []
        write_db()
        load_users()
        return True
    else:
        return False

def add_favorite(str_user_id, movieObj):
    if isinstance(movieObj, MovieObj):
        movieObj.print_info()
        Database.user_favorites[str_user_id].append({
            "movie_id": movieObj.get_id()[0],
            "title": movieObj.get_title()[0],
            "release_date": movieObj.get_release_date()[0],
            "overview": movieObj.get_overview()[0],
            "img_url": movieObj.get_img_url()
        })
        write_db()
        load_users()
        return True
    else:
        return False

def authenticate():
    return PseudoSession.is_authenticated

def get_user_id(username):
    return Database.user_to_id_map[username]
## end internal APIs ##
