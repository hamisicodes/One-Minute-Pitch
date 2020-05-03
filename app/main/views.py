from . import main
from flask import render_template,request
from flask_login import login_required

@main.route('/')
def index():
    title = 'Hello World'
    return render_template('index.html', title = title)


@main.route("/pitch" ,methods=["GET", "POST"])
@login_required
def pitch():
    return render_template("pitches.html")