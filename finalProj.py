from flask import Flask, render_template
from flask_bootstrap import Bootstrap
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

@app.route("/")
def index():
    return render_template("index.html")