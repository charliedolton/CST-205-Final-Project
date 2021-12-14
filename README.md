## CST-205-Final-Project: **The Movie Social**
- Due Thur. Dec. 16, 2021

### Members:
---
- [Barbara Kondo](https://github.com/bKondo)
- [Charlie Dolton](https://github.com/charliedolton)
- [Daniel Kufer](https://github.com/lizardgai4)

### Description:
---
This project uses Flask to create a webpage. The webpage itself uses The Movie Database API to retrieve and display movies the user searches for and can also add movies to a users favorites list. We chose to challenge ourselves by creating a mock database for user information and lists of movies, instead of using TMDb's api, Flask-Login, and Flask-Session.

- [GitHub link](https://github.com/charliedolton/CST-205-Final-Project)
- Coding languages:
    - Python
    - HTML

### How to install and run:
---
1. start your virtual environment (venv)

2. install requirements
    - for Mac/OS:
        - `python -m pip install -r requirements.txt`

    - for Windows:
        - `py -m pip install -r requirements.txt`

3. You will need to provide your own config.py in the root folder with the following:
    - a TMDb account is needed to apply for [a TMDb apikey](https://www.themoviedb.org/settings/api)
```
class Config:
    api_key = "your_TMDb_api_key"
    secret = "a_flask_secret_key"
```
4. set Flask environment variables
    - for Mac/OS:
        - `export FLASK_APP=finalProj.py`
        - `export FLASK_DEBUG=1`
        - `export FLASK_ENV=development`
        - `flask run`
    - for Windows:
        - `$env:FLASK_APP="finalProj.py"`
        - `$env:FLASK_DEBUG="1"`
        - `$env:FLASK_ENV="development"`
        - `flask run`
    - Note: for production run of app (remove stack trace in browser)
        - set FLASK_DEBUG to 0
        - set FLASK_ENV to production

### Libraries:
---
- [Boostrap-Flask](https://pypi.org/project/Bootstrap-Flask/)
- [Flask](https://pypi.org/project/Flask/)
- [Flask-WTF](https://pypi.org/project/Flask-WTF/)
- [requests](https://pypi.org/project/requests/)
- [tmdbv3api](https://pypi.org/project/tmdbv3api/)
- [WTForms](https://pypi.org/project/WTForms/)

### References:
---
- [markdown guide](https://www.markdownguide.org/cheat-sheet/)
- [The Movie Database API](https://developers.themoviedb.org/3/getting-started/introduction)
- [The Flask Mega Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
- [W3Schools: Python JSON](https://www.w3schools.com/python/python_json.asp)
  - [Kite: update a json file](https://www.kite.com/python/answers/how-to-update-a-json-file-in-python)

### What we'd change:
---
- connect to an actual database
    - that would have saved a lot of time and headaches
- use more than basic forms