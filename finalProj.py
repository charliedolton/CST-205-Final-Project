from flask import Flask, flash, redirect, render_template, request, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap
from tmdbv3api import TMDb
from config import Config
from User import User
from ErrorMsg import ErrorMsg
import json

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

## site forms ##
class LoginForm(FlaskForm):
    username = StringField( 'Username', validators=[DataRequired()] )
    password = PasswordField( 'Password', validators=[DataRequired()] )
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
# ## end of pseudo db methods using pickle ##

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
    # splash page
    if authenticate() is False:
        print('index: No one is logged in.')
    else:
        print(f'index: { User.current_username } is logged in.')
    return render_template('index.html', username=User.current_username)

@app.route('/login', methods=['GET', 'POST'])
def login():
    # show login form
    form = LoginForm()
    if form.validate_on_submit():
        user_id = User.user_to_id_map.get(form.username.data, ErrorMsg.bad_login)
        if (user_id == ErrorMsg.bad_login):
            flash(ErrorMsg.bad_login, 'error')
            return redirect(url_for('login'))
        else:
            if (User.id_to_user_map.get(user_id)[1] == form.password.data):
                username = User.id_to_user_map.get(user_id)[0]
                User.current_username = username
                User.current_user_id = user_id
                User.is_authenticated = True

                print(f'/user/auth: username: {User.current_username}\n')
                return redirect(url_for('index'))
            else:
                flash(ErrorMsg.bad_login, 'error')
                return redirect(url_for('login'))

    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    User.current_username = None
    User.current_user_id = None
    User.is_authenticated = False
    return redirect(url_for('index'))

## interal APIs ##
def authenticate():
    return User.is_authenticated
## end interal APIs ##
## end of routes ##