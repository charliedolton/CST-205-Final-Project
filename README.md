## CST-205-Final-Project: **The Movie Social**
- Group 794
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
- [Design Doc](https://docs.google.com/document/d/1Nvu_1FSIolBz-cQ35ItZUtLRtezXWrJweXjIKqPbO0E/edit?usp=sharing&resourcekey=0-GKhs52vyGuavIhP14LwiSw)
- Coding languages:
    - Python
    - HTML
    - JSON

### How to install and run:
---
1. start your virtual environment (venv)
    - create and start venv for macOS:
        - `python3.9 -m venv venv`
        - `source venv/bin/activate`
    - create and start venv for Windows:
        - `py -m venv venv`
        - `.\venv\Scripts\Activate.ps1`

2. install requirements
    - for macOS:
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
- [WTForms documentation](https://wtforms.readthedocs.io/en/2.3.x/fields/)
- [Jinja documentation](https://jinja.palletsprojects.com/en/3.0.x/templates/)
- [pass variables through Jinja include statements](https://stackoverflow.com/questions/9404990/how-to-pass-selected-named-arguments-to-jinja2s-include-context)
- [markdown guide](https://www.markdownguide.org/cheat-sheet/)
- [The Movie Database API](https://developers.themoviedb.org/3/getting-started/introduction)
- [The Flask Mega Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
- [W3Schools: Python JSON](https://www.w3schools.com/python/python_json.asp)
  - [Kite: update a json file](https://www.kite.com/python/answers/how-to-update-a-json-file-in-python)

### Final Work distribution:
---
route logic was a group effort

- Daniel
    - home page
    - review pages (2)
    - profile pages (2)
    - basic API retrieval
    - reviews JSON pseudo database
    - dummy user data

- Barbara
    - home page
    - login and signup pages
    - favorites list page
    - user and favorites JSON pseudo database
    - nav bar

- Charlie
    - search page
    - API documentation and key

### What we'd change:
---
- connect to an actual database
    - that would have saved a lot of time and headaches
    - add security checks
- use more than basic forms
- use the provided filters on movie listings to ensure everything is school acceptable
  - thankfully, there were no large mishaps, just small easily scroll-pass ones
- finish hooking up search page logic
- finish hooking up review pages to main website
