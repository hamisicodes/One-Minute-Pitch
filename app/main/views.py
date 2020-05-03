from . import main
from flask import render_template,request,redirect
from flask_login import login_required,current_user
from .. models import User,Pitch
from .. import db

@main.route('/')
def index():
    title = 'Hello World'
    return render_template('index.html', title = title)


@main.route("/pitch" ,methods=["GET", "POST"])
@login_required
def pitch():
    pitches = Pitch.query.all()


    if request.method == "POST":
        req = request.form
        print(req)

        pitch = req.get('pitch')
        new_pitch = Pitch(description = pitch , user = current_user)
        db.session.add(new_pitch)
        db.session.commit()
        pitches = Pitch.query.all()

        
        

        # return redirect(request.url)
       

  

    return render_template("pitches.html" ,pitches = pitches)

@main.route('/user/<int:id>')
def profile(id):
    user = User.query.filter_by(id=id).first()
    pitches = Pitch.query.filter_by(user_id = id).all()

    if user is None:
        abort(404)

    return render_template("profile.html", user=user , pitches = pitches)