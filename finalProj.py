from flask import Flask, render_template
from flask_bootstrap import Bootstrap
# from tmdbv3api import TMDb
# from config import config
from User import User
from ErrorMsg import ErrorMsg
import pickle

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

# tmdb = TMDb()
# # hide API_KEY from github!
# # config.py should be ignored on git push
# tmdb.api_key = config.api_key
# tmdb.language = 'en'
# tmdb.debug = True

## site forms ##
class LoginForm(FlaskForm):
    username = StringField( 'Username', validators=[DataRequired()] )
    password = StringField( 'Password', validators=[DataRequired()] )
## end of site forms ##

## pseudo db methods ##
def load_users():
    with open('id_to_user', 'rb') as my_file:
        saved_data = pickle.load(my_file)
        User.id_to_user_map = saved_data
    with open('user_to_id', 'rb') as my_file:
        saved_data = pickle.load(my_file)
        User.id_to_user_map = saved_data

def write_db():
    with open('id_to_user', 'wb') as my_file:
        pickle.dump(User.id_to_user_map, my_file)
    with open('user_to_id', 'wb') as my_file:
        pickle.dump(User.user_to_id_map, my_file)
## end of pseudo db methods ##

# # write_db() needs to run once so 'pickled' exists
# write_db()
load_users()
print(f'User.user_to_id_map:\n{User.user_to_id_map}')
print(f'User.id_to_user_map:\n{User.id_to_user_map}')

## routes ##
@app.route('/')
def index(username):
    # splash page 
    return render_template('index.html', username=username)

@app.route('/login')
def login():
    # show login form    
    print('login page route')

## interal APIs ##
@app.route('/user/auth', methods=('POST'))
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