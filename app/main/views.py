from . import main
from flask import render_template,request,redirect
from flask_login import login_required
from .. models import User

@main.route('/')
def index():
    title = 'Hello World'
    return render_template('index.html', title = title)


@main.route("/pitch" ,methods=["GET", "POST"])
@login_required
def pitch():
    if request.method == "POST":
        req = request.form
        print(req)

        pitch = req.get('pitch')
        new_pitch = Pitch(description = pitch , user = current_user)
        new_pitch.save_pitch()


        # return redirect(request.url)



    return render_template("pitches.html")