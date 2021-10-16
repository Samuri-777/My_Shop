from My_Shop_J7 import app
from flask import render_template

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/property")
def property():
    return render_template('property.html')