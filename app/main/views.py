from . import main
from flask import render_template,request,redirect
from flask_login import login_required,current_user
from .. models import User,Pitch,Comment
from .. import db

@main.route('/')
def index():
    title = 'Welcome'
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

    title = f'{user.username}'

    return render_template("profile.html", user=user , pitches = pitches , title = title)


@main.route('/comment/<int:id>', methods=["GET", "POST"])
def comment(id):
    
    req = request.form
    print(req)

    pitch = req.get('pitch')

    post = Pitch.query.filter_by(id=id).first()
    # comment = Comment(description = req , pitch = post , user = current_user)

   
    title = 'comments'
    return render_template("comment.html" ,title = title , pitch = post)



